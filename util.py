#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 ciel <beijiu572@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Workflow 配置工具
"""

import os, re, subprocess
import ConfigParser
from tempfile import NamedTemporaryFile

CONFIG_FILE = 'config.ini'

def check_config_file():
    return os.path.exists(CONFIG_FILE)

def alert(msg, title="Warming!"):
    '''alrt user in notification center'''
    os.system('osascript -e \'display notification "%s" with title "%s"\'' % (msg, title))

def read_config():
    ''' read config from config.ini, return a tuple'''
    if not os.path.exists(CONFIG_FILE):
        return
    cf = ConfigParser.ConfigParser()
    cf.read(CONFIG_FILE)

    weibo_section = 'weibo'
    keys = ('username', 'password')
    try:
        res = map(lambda x: cf.get(weibo_section, x), keys)
    except ConfigParser.NoOptionError:
        return

    if not all(map(lambda x: re.match(r'\w+', x), res)):
        return
    return dict(zip(keys, res))

def open_with_editor():
    os.system('open -b "com.apple.TextEdit" "./%s"' % CONFIG_FILE)

def delete_config():
    os.system('/bin/rm "./%s"' % CONFIG_FILE)

def generate_config():
    import textwrap
    config_init_content = '''\
        ; 用做模拟登录，得到 cookie 后则删除配置文件
        [weibo]
        username=微博登录用户名
        password=微博密码
        '''
    with open(CONFIG_FILE, 'w') as fp:
            fp.write(textwrap.dedent(config_init_content))
