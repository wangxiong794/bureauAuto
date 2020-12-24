# coding=utf-8
"""

"""
import os

root_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    print(root_dir)
    picture_path = os.path.join(root_dir,"pictures")
    print(os.path.join(picture_path,"123" + ".png"))
    print(os.path.join(os.path.join(root_dir, "elements"), "WebElement.ini"))