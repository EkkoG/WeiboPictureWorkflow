#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 ciel <beijiu572@gmail.com>
#
# Distributed under terms of the MIT license.

"""
得到图片的 URL
"""

from upload import upload_file
import util
import os
import sys


url = upload_file()
if url:
    os.system("echo '%s' | pbcopy" % url)
    util.alert('上传图片成功，图片 URL 已复制到剪切板！')
else:
    util.alrt('上传失败!')
    sys.exit(0)
