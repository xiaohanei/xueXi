import string
import random


def random_str(num):
    #获取26个英文字母大小写字符串
    str1 = string.ascii_letters
    print(str1)
    #获取阿拉伯数字字符串
    str2 = string.digits
    print(str2)
    #从字符串里，随机取出num个字符。因为random.sample生成的是一个列表，需要将每个元素连接起来
    ren_str = "".join(random.sample(str1 + str2,num))
    print(ren_str)
    return ren_str

if __name__ == '__main__':
    random_str(5)
