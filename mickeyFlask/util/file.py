import codecs
import os

def mkdirs(file_name):
    if not os.path.exists:
        print(os.path.abspath(os.path.dirname(file_name)))
        os.makedirs(os.path.abspath(os.path.dirname(file_name)))
    
def write(message, file_name):
    """
    写入文件

    :param message          字符串数据

    :param file_name        文件名
    """
    mkdirs(file_name)
    t = codecs.open(file_name, "w", encoding='utf-8')
    t.write(message)
    t.close()