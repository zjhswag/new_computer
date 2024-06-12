def main():
    zhao = [10, 10]  # 创建一个包含两个元素的列表
    with open("hao3", "wb+") as fp:  # 以二进制写入模式打开文件
        for number in zhao:
            fp.write(number.to_bytes(4, 'little'))  # 将每个数字转换为4字节的小端格式并写入文件

if __name__ == "__main__":
    main()
