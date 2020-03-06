---
layout: post
title: 在 Mac 中配置 Nginx + MySQL + PHP 环境
date: 2019-03-21
author: 熊猫小A
toc: true
categories: 
  - 编程开发
  - 环境配置
  - Mac
tags:
 - Mac
 - 环境配置
 - 建站
---

## 安装 Homebrew

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

检查 Homebrew：

```bash
brew doctor
```

## 安装 wget

```bash
brew install wget
```

## 安装 MySQL

```bash
brew install mysql
```

**启动服务**

```bash
brew services start mysql
```

**初始化**

```bash
mysql_secure_installation
```

注意：这一步中最好不要使用 `VALIDATE PASSWORD COMPONENT`，并且允许 remote 登陆 root。其它就按需要选择就行。

检查 MySQL：

```bash
mysql -uroot -p
```

输入密码可连接上 MySQL。若遇到 MySQL 8 的新密码机制导致的连接问题：

```mysql
use mysql;
ALTER USER 'user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'yourpasswd';
```

## 安装 PHP 7.2

```bash
brew install php72
# The php.ini and php-fpm.ini file can be found in:
#     /usr/local/etc/php/7.2/
```

**配置环境变量，替换默认 PHP 版本**

```bash
echo 'export PATH="$(brew --prefix php72)/bin:$PATH"' >> ~/.bash_profile
echo 'export PATH="$(brew --prefix php72)/sbin:$PATH"' >> ~/.bash_profile
echo 'export PATH="/usr/local/bin:/usr/local/sbib:$PATH"' >> ~/.bash_profile
source ~/.bash_profile

```

**启动服务**

```bash
brew services start php@7.2

```

验证

```bash
php -v
# PHP 7.2.15 (cli)
php-fpm -v
# PHP 7.2.15 (fpm-fcgi)

```

## 安装 Nginx

```bash
brew install nginx
# nginx will load all files in /usr/local/etc/nginx/servers/
# the default port is 8080
# the default web dir is /usr/local/var/www/

```

**启动服务**

```bash
brew services start nginx

```

**创建 Server**

可以在 /usr/local/etc/nginx/servers/ 下新建配置，也可以配置原来的 server。

macOS 禁止非系统服务访问 1024 以下端口，因此使用 4433 与 8080 端口

```nginx
server {
        listen       8080;
        server_name  localhost;

        index        index.html index.htm index.php default.html default.htm default.php;
        root         /usr/local/var/www;

        #error_page  404              /404.html;

        # rewrite for typecho
        if (!-e $request_filename) {
            rewrite ^(.*)$ /index.php$1 last;
        }
  
        # php-pathinfo
        location ~ [^/]\.php(/|$)
        {
            fastcgi_pass  127.0.0.1:9000;
            fastcgi_index index.php;
            include fastcgi.conf;
            fastcgi_split_path_info ^(.+?\.php)(/.*)$;
            set $path_info $fastcgi_path_info;
            fastcgi_param PATH_INFO       $path_info;
            try_files $fastcgi_script_name =404;
        }

        location ~ \.php$ {
           fastcgi_pass   127.0.0.1:9000;
           fastcgi_index  index.php;
           fastcgi_param  SCRIPT_FILENAME  /usr/local/var/www$fastcgi_script_name;
           include        fastcgi_params;
        }
    }

```

**重载配置**

```bash
nginx -r reload

```

测试

在 /usr/local/var/www 下创建 index.php：

```php
<?php
  phpinfo();
```

浏览器访问即可。

## 使 Nginx 监听低端口

首先停止当前服务：

```bash
launchctl unload ~/Library/LaunchAgents/homebrew.mxcl.nginx.plist
```

移除默认的自启动服务（删除链接）：

```bash
rm ~/Library/LaunchAgents/homebrew.mxcl.nginx.plist
```

建立连接到 `/Library/LaunchDaemons`：

```bash
sudo ln -sfv /usr/local/opt/nginx/*.plist /Library/LaunchDaemons
```

设置正确的权限：

```bash
sudo chmod 644 /Library/LaunchDaemons/homebrew.mxcl.nginx.plist
sudo chown wheel /Library/LaunchDaemons/homebrew.mxcl.nginx.plist
```

启动：

```bash
sudo launchctl load -w /Library/LaunchDaemons/homebrew.mxcl.nginx.plist
```

