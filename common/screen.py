# coding=utf-8

from getRootPath import root_dir
import os


def getScreen(driver, caseName, fileName):
    picture_path = os.path.join(root_dir, "pictures")
    picture_path = os.path.join(picture_path, fileName)
    if os.path.exists(picture_path) is False:
        os.mkdir(picture_path)
    else:
        pass
    picture = os.path.join(picture_path, caseName + ".png")
    driver.save_screenshot(picture)