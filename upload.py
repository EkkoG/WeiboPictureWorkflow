#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 ciel <beijiu572@gmail.com>
#
# Distributed under terms of the MIT license.

import util
import sys
from weibo import weibo
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

        try:
            weibo.login_with_username_and_password(username, password)
        except:
            util.alert('登录失败，请重试!')
            sys.exit(0)


        if weibo.check_login_status():
            util.delete_config()
        else:
            util.alert('登录失败，请重试!')
            sys.exit(0)

    img_file = get_paste_img_file()

    if img_file:
        try:
            url = weibo.request_image_url(img_file.name)
            return url
        except:
            util.delete_cookie()
            util.alert('Cookie 过期，请重新登录!')
            sys.exit(0)
            return None
    else:
        util.alert('您的剪切板里没有图片!')
        sys.exit(0)
