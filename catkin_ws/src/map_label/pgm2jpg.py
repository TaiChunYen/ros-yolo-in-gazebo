# -*- coding: utf-8 -*-
from __future__ import print_function

import cv2
import time
import os
import operator
import numpy as np
import argparse
from PIL import Image
import pdb

def is_pgm_file(in_path):
    if not os.path.isfile(in_path):
        return False
    if in_path is not str and not in_path.endswith('.pgm'):
        return False
    return True


def convert_pgm_P5(in_path, out_path):
    """
    将pgm文件转换成其它图像格式
    读取二进制文件，先读取幻数，再读取宽和高，以及最大值
    :param in_path: 输入pgm文件路径
    :param out_path: 输出文件路径
    """
    if not is_pgm_file(in_path):
        raise Exception("%s 不是一个PGM文件" % in_path)
    with open(in_path, 'rb') as f:
        # 读取两个字节 - 幻数，并解码成字符串
        magic_number = f.readline().strip().decode('utf-8')
        if not operator.eq(magic_number, "P5"):
            raise Exception("该图像有误")
        # 读取高和宽
        #
        f.readline().strip()
        #pdb.set_trace()
        width, height = 256,252
        width = int(width)
        height = int(height)
        # 读取最大值
        f.readline().strip()
        #pdb.set_trace()        
        maxval = f.readline().strip()
        # 每次读取灰度值的字节数
        if int(maxval) < 256:
            one_reading = 1
        else:
            one_reading = 2
        # 创建空白图像，大小为(行，列)=(height, width)
        img = np.zeros((height, width))
        img[:, :] = [[ord(f.read(one_reading)) for j in range(width)] for i in range(height)]
        cv2.imwrite(out_path, img)
        print('%s save ok' % out_path)



parser = argparse.ArgumentParser(description='Format Converter - PGM')

parser.add_argument('-i', '--input', type=str, help='Path to the pgm file')
parser.add_argument('-o', '--output', type=str, help='Path to the result file')
args = vars(parser.parse_args())

in_path = args['input']
out_path = args['output']

if in_path is not None and out_path is not None:
    # 转换单个pgm文件格式
    convert_pgm_P5(in_path, out_path)




