from requests import get  # get请求方法
from json import dumps  # json序列处理
from random import randint  # 随机数
from os.path import exists  # 检测文件夹是否存在
from os import mkdir  # 创建文件夹

# 下载的爬虫
def download(path):
    url = "https://api.ixiaowai.cn/api/api.php"  # 请求URL
    content = get(url)  # 发送网络请求
    number = randint(100000, 999999)  # 生成随机数
    print("保存图片 >>> ./%s/%d.jpg" % (path, number))  # 输出保存信息
    with open("%s/%d.jpg" % (path, number), "wb") as f:  # 保存图片信息
        f.write(content.content)

# 主函数
def main(path):
    # 下载
    for i in range(1, int(input("您需要多少张图片 >>> ")) + 1):
        download(path)
    # 保留解释器窗口
    input("下载完成。")

# 保存路径的程序
if __name__ == "__main__":
    try:  # 包含异常
        folder = input("您需要将图片保存到哪里（输入相对路径） >>> ")
        if exists(folder):  # 有这个文件夹就直接保存
            main(folder)  # 下载
        else:  # 如果没有这个文件夹
            mkdir(folder)  # 创建文件夹
            main(folder)  # 下载
    except Exception as e:  # 提取异常基类
        print("ERROR:%s" % e)  # 输出异常
