# import  numpy as np
# te = np.array([0.11,0.09,0.03,0.008,0.0025,0.002,0.003,3,0,1,0])
# print(te)
# te.reshape(-1, )
# print(te.shape)
# print(te)
# x1 = 1+(1/10000)
# print(x1)
# x2 = x1-(1-1/10000)
# print(x2,1/10000)
#
#
# import numpy as np
#
# # 示例数据
# y = np.array([0, 1, 0, 2, 1, 2, 0, 1])
# class_label = 1
#
# # 使用 np.where 找出数组中等于特定类别标签的索引
# idx = np.where(y == class_label)
# print(idx[0])
import numpy as np
# from dataset.mnist import load_mnist


def softmax_train(train, target, alpha, num):
    xhat = np.concatenate((train, np.ones((len(train), 1))), axis=1)
    nparam = len(xhat.T)  # 785
    beta = np.random.rand(nparam, 10)  # 785x10
    for i in range(num):
        wtx = np.dot(xhat, beta)
        wtx1 = wtx - np.max(wtx, axis=1).reshape(len(train), 1)
        e_wtx = np.exp(wtx1)
        yx = e_wtx / np.sum(e_wtx, axis=1).reshape(len(xhat), 1)
        print('  #' + str(i + 1) + ' : ' + str(cross_entropy(yx, target)))
        t1 = target - yx
        t2 = np.dot(xhat.T, t1)
        beta = beta + alpha * t2

    return beta


def cross_entropy(yx, t):
    sum1 = np.sum(yx * t, axis=1)
    ewx = np.log(sum1 + 0.000001)
    return -np.sum(ewx) / len(yx)


def classification(test, beta, test_t):
    xhat = np.concatenate((test, np.ones((len(test), 1))), axis=1)
    wtx = np.dot(xhat, beta)
    output = np.where(wtx == np.max(wtx, axis=1).reshape((len(test), 1)))[1]

    print("Percentage Correct: ", np.where(output == test_t)[0].shape[0] / len(test))
    return np.array(output, dtype=np.uint8)


if __name__ == '__main__':
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

    nread = 60000
    train_in = x_train[:nread, :]
    train_tgt = np.zeros((nread, 10))

    test_in = x_test[:10000, :]
    test_t = t_test[:10000]

    for i in range(nread):
        train_tgt[i, t_train[i]] = 1

    beta = softmax_train(train_in, train_tgt, 0.001, 60)
    print(beta)
    result = classification(test_in, beta, test_t)
