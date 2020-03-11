---
layout: post
title: MacOS 删除灰色的ABC输入法
slug: ABC
date: 2020-03-11 09:44
status: publish
author: labulac
categories: 
  - 教程
tags: 
  - Mac
  - 设置
  - 输入法
  - ABC
excerpt: ABC

---

### 问题来源

总是很烦ABC输入法，明明不怎么需要

![](https://gitee.com/labulac/pic/raw/master/uPic/GPH9jG.png)

又是灰色的，如何删除呢？

### 解决

1.首先要关闭系统的完整性保护，即关闭SIP，方法是在重启电脑时按住 command + R 进入恢复模式，然后选择实用工具中的 终端，输入

```bash
csrutil disable 
```

回车，显示成功关闭SIP，之后重启电脑。

2.之后打开终端，在命令行输入

```bash
sudo open -a /Applications/Xcode.app ~/Library/Preferences/com.apple.HIToolbox.plist 
```

回车之后输入密码确认，之后便用Xcode打开了这个配置文件。

另：

若是使用PlistEdit Pro则输入这个：

```bash
sudo open -a /Applications/PlistEdit\ Pro.app ~/Library/Preferences/com.apple.HIToolbox.plist 
```

同样输入密码确认，之后便用PlistEdit Pro打开了这个配置文件。

3.删除红框键值下的子键中带有ABC字样的整个键值

![image-20200311095524398](/Users/labulac/Library/Application Support/typora-user-images/image-20200311095524398.png)

4.删除之后点击保存，如果不能直接保存则可以先将修改的后的文件另存为到桌面上，然后再将文件复制到 ~/Library/Preferences 此处，至此已经修改完成。

5.下面是将系统完整性保护打开：

重启，进入恢复模式，然后输入

```bash
csrutil enable
```

打开系统完整性保护。

**以上**