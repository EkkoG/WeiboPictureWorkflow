#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 ciel <beijiu572@gmail.com>
#
# Distributed under terms of the MIT license.

import util
import os
import sys
import weibo
from clipboard import get_paste_img_file

def upload_file():
    if not weibo.check_login_status():
        if not util.check_config_file():
            util.generate_config()

        config = util.read_config()

        if not config:
            util.alert('请先设置你的微博账号')
            util.open_with_editor()
            sys.exit(0)

        username = config['username']
        password = config['password']
        weibo.login_with_username_and_password(username, password)
        if weibo.check_login_status():
            util.delete_config()
        else:
            util.alert('登录失败，请重试!')
            exit()
    img_file = get_paste_img_file()
    if img_file:
        url = weibo.request_image_url(img_file.name)
        if url:
            return url
        else:
            return None
    else:
        util.alert('您的剪切板里没有图片!')
