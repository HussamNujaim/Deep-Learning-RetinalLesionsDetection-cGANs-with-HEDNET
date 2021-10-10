#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************
# @Author  : Qiqi Xiao & Jiaxu Zou
# @Email     : xiaoqiqi177@gmail.com & zoujx96@gmail.com
# @File    : config.py
# **************************************
LESION_IDS = {'EX':0, 'HE':1, 'MA':2, 'SE':3}

#Modify the general parameters.
IMAGE_DIR = 'drive/MyDrive/DRsegmentation/HEDNet_cGAN/data'
NET_NAME = 'hednet'
IMAGE_SIZE = 512

#Modify the parameters for training.
EPOCHES = 5000
TRAIN_BATCH_SIZE = 4
G_LEARNING_RATE = 0.001
LESION_DICE_WEIGHT = 0.
ROTATION_ANGEL = 20
CROSSENTROPY_WEIGHTS = [0.1, 1.]
RESUME_MODEL = None
