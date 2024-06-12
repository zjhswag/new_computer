"""
文件处理相关模块
"""


def print_file_info(file_name):
    """

    :param file_name:
    :return: 返回文件内容
    """
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        print(f.read())
    except Exception as e:
        print(f'出现异常，原因是{e}')
    finally:
        if f:        # 如果文件不存在可能不能调用close
            f.close()


if __name__ == '__main__':
    print_file_info(r"C:\Users\14601\Desktop\草稿1.txt")