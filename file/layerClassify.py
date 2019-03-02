import os
import re
import shutil


class FrameFile(object):
    def __init__(self, path, file):
        self.full_path = path + '/' + file
        self.path = path
        self.name = os.path.splitext(file)[0]
        self.suffix = os.path.splitext(file)[1]

    def move(self, path):
        dst = path + '/' + self.name + self.suffix
        # print(dst)
        shutil.move(self.full_path, dst)

    def rename(self, name):
        pass

    def layerName(self, pattern=r'[._]\d+$'):
        layer = re.sub(pattern, '', self.name)
        return layer


def main():
    folder_dir = r'D:\works\Git_Repos\Study\file\testlayer'
    frameFiles = {}
    for root, dirs, files in os.walk(folder_dir):
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        # print(files)  # 当前路径下所有非目录子文件
        for file in files:
            frame = FrameFile(root, file)
            layer = frame.layerName()
            if layer in frameFiles.keys():
                frameFiles[layer].append(frame)
            else:
                frameFiles[layer] = [frame]

    # print(frameFiles)

    for key, value in frameFiles.items():
        newdir = folder_dir + '/' + key
        if not os.path.exists(newdir):
            os.mkdir(newdir)
        for frame in value:
            frame.move(newdir)


if __name__ == "__main__":
    main()
