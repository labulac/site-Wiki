---
layout: post
title: Windows 上安装 Hexo
date: 2018-05-04
author: 熊猫小A
toc: true
categories: 
  - 建站
  - Hexo
tags:
  - 建站
  - 环境配置
  - Windows
---

首先，下载安装 Node.js ：[Download for Windows (x64)](https://nodejs.org/en/) 。

更改 NPM 镜像：

```
npm config set registry https://registry.npm.taobao.org
```

安装 Hexo：

```
npm install -g hexo
```

### 部署到远端

#### Git

```
npm install hexo-deployer-git --save
```

配置站点 _config.yml

```
deploy:
  type: git
  repo: <repository url>
  branch: [branch]
  message: [message]
```

#### SFTP

```
npm install hexo-deployer-sftp --save
```

配置站点 _config.yml

```
deploy:
  type: sftp
  host: <host>
  user: <user>
  pass: <password>
  remotePath: [remote path]
  port: [port]
  privateKey: [path/to/privateKey]
  passphrase: [passphrase]
  agent: [path/to/agent/socket]
```

