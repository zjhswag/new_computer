def str_reverse(s):
    """
    功能是将字符串反转
    :param s: 需要反转的字符串
    :return:  反转后的字符串
    """
    return s[::-1]


def substr(s, x, y):
    """

    :param s: 需要切片的字符串
    :param x: 开始下标
    :param y: 结束下标
    :return: 返回
    """
    return s[x: y]


if __name__ == '__main__':
    print(str_reverse('fuck you'))
