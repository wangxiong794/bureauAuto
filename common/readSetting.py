import configparser
import os

from getRootPath import root_dir


def readUser(keyFlag,KeyName="username",filename="user.ini"):
    config_path = os.path.join(root_dir, "conf", filename)  # 获取配置文件路径
    cf = configparser.ConfigParser()
    cf.read(config_path, encoding="utf-8")

    # 获取配置文件中所有section
    secs = cf.sections()

    # 获取某个section名下所对应的键
    options = cf.options(keyFlag)

    # 返回配置文件中name所对应的值
    return cf.get(keyFlag, KeyName)


if __name__ == "__main__":
    a = readUser("工委办")
    print(a)