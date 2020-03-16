---
layout: post
title: MacOS 的 DS_Store
slug: DS_Store
date: 2020-03-16 13:44
status: publish
author: labulac
categories: 
  - 教程
tags: 
  - Mac
  - 设置
  - DS_Store
excerpt: DS_Store那些事

---

### 问题来源

.DS_Store文件是Mac OS系统自动生成的一个隐藏文件，主要用于存储文件夹的自定义属性，如果自己电脑上的文件夹自定义属性没有怎么改的话，这个文件其实是没有多大用的，每个文件夹下都有，外接硬盘或者网络硬盘Mac OS系统都会为其创建，在Windows系统下，这个文件可以清楚看到。所以这里说说如何删除全部的.DS_Store文件和禁止系统再次生成.DS_Store文件。

### 如何解决

##### 一、禁止.DS_Store文件的生成

通过下面命令可以让系统默认情况下不再生成.DS_Store文件

```
defaults write com.apple.desktopservices DSDontWriteNetworkStores true
```

如果希望系统生成.DS_Store文件，还是执行上面的命令，只不过把true改成false就可以了

##### 二、删除.DS_Store文件

通过终端命令行执行find命令找到并删除，命令需要root权限，而且不要输入错误，万一输入错误导致系统文件被删除，会非常的危险⚠️，所以这是一个比较危险的操作，操作者需要小心甚微，命令如下：

```
sudo find / -name ".DS_Store" -depth -exec rm {} \;
```

这个命令执行后，时间会比较长，请耐心！

**以上**