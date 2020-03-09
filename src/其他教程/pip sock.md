---
layout: post
title: Python pip3 运行出错：Missing dependencies for SOCK
slug: pip安装报错 Could not install packages due to an EnvironmentError
date: 2020-03-09 10:48
status: publish
author: labulac
categories: 
  - 教程
tags: 
  - Python
  - pip
excerpt: pip
---

### 问题

pip安装报错Could not install packages due to an EnvironmentError: Missing dependencies for SOCK

![Wnaa3a](https://gitee.com/labulac/pic/raw/master/uPic/Wnaa3a.png)

### 解决方法

终端输入以下：

```bash
unset all_proxy && unset ALL_PROXY
```

**以上**

