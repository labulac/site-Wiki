# -*- coding: utf-8 -*-
"""Configuration for Wiki
"""

# For Maverick
site_prefix = "http://blog.labulac.top/"
source_dir = "../src/"
build_dir = "../dist/"
template = {
    "name": "Kepler",
    "type": "local",
    "path": "../Kepler"
}
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "labulac/site-Wiki@gh-pages"
}
category_by_folder = True
for_manual_build_trigger = 1

# 站点设置
site_name = "LABULAC'S BLOG"
site_logo = "${static_prefix}android-chrome-512x512.png"
site_build_date = "2019-02-22T12:00+08:00"
author = "D0raemon"
email = "vector051545@gmail.com"
author_homepage = "https://github.com/labulac"
description = "labulac的blog站点"
key_words = ['Maverick', 'labulac', 'Galileo', 'blog','D0raemon']
language = 'zh-CN'

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "2to78D9NRkvN8CTRtIneOcXL-gzGzoHsz",
    "appKey": "ws5n5WDCDFVg5rhvqPceRiuA",
    "visitor": True,
    "recordIP": True,
    "placeholder": "谈谈你的看法……"
}

external_links = [
    {
        "name": "GITHUB",
        "url": "https://github.com/labulac",
        "brief": "D0raemon的GitHub"
    },
    {
        "name": "CHANNEL",
        "url": "https://t.me/labu1ac",
        "brief": "D0raemon的telegram"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "历史归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "GitHub",
        "url": "https://github.com/labulac",
        "icon": "gi gi-github"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
