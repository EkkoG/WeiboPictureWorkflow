#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 ciel <ciel@cieldeMBP>
#
# Distributed under terms of the MIT license.

"""
从剪切板读取图片
"""

import os
import tempfile
import imghdr
import shutil
from AppKit import NSPasteboard, NSPasteboardTypePNG,\
    NSPasteboardTypeTIFF, NSPasteboardTypeString,\
    NSFilenamesPboardType


def get_paste_img_file_path():
    pb = NSPasteboard.generalPasteboard()
    data_type = pb.types()

    supported_image_format = (NSPasteboardTypePNG, NSPasteboardTypeTIFF)
    if NSFilenamesPboardType in data_type:
        # file in clipboard
        img_path = pb.propertyListForType_(NSFilenamesPboardType)[0]
        img_type = imghdr.what(img_path)
        if not img_type:
            # not image file
            return None

        if img_type not in ('png', 'jpeg', 'gif'):
            # now only support png & jpg & gif
            return None
        return img_path


