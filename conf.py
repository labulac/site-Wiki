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
author_homepage = "https://labulac.top"
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
    "placeholder": "谈谈你的看法…"
}

external_links = [
    {
        "name": "HOME",
        "url": "https://home.labulac.top",
        "brief": "D0raemon的导航页"
    },
    {
        "name": "DRIVER",
        "url": "https://driver.labulac.top",
        "brief": "D0raemon的云盘"
    },
    {
        "name": "CYDIA",
        "url": "https://repo.labulac.top",
        "brief": "D0raemon的越狱源"
    },
    {
        "name": "MUSIC",
        "url": "https://labulac3.herokuapp.com",
        "brief": "D0raemon的MUSIC"
    },
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
        "name": "归档",
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
<link rel="dns-prefetch" href="//blog.labulac.top" />



<script src="https://cdn.staticfile.org/jquery/1.10.2/jquery.min.js">
</script>


<script type="text/javascript"> 
/* 鼠标特效 */
var a_idx = 0; 
jQuery(document).ready(function($) { 
    $("body").click(function(e) { 
        var a = new Array("富强", "民主", "文明", "和谐", "自由", "平等", "公正" ,"法治", "爱国", "敬业", "诚信", "友善"); 
        var b = new Array("red","blue","yellow","green","pink","blue","orange");
        var $i = $("<span/>").text(a[a_idx]); 
        a_idx = (a_idx + 1) % a.length; 
        b_idx = (a_idx+1)%7;/* 七中颜色变色 */
        var x = e.pageX, 
        y = e.pageY; 
        $i.css({ 
            "z-index": 9999, 
            "top": y - 20, 
            "left": x, 
            "position": "absolute", 
            "font-weight": "bold", 
            "color": b[b_idx]
        }); 
        $("body").append($i); 
        $i.animate({ 
            "top": y - 180, 
            "opacity": 0 
        }, 
        1500, 
        function() { 
            $i.remove(); 
        }); 
    }); 
}); 
</script>



'''

footer_addon = r'''
<script src="//code.tidio.co/cdykkwfovmclocfai87icmljlygcos1w.js"></script>
'''

body_addon = ''
