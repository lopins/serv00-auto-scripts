# Serv00 - 免费主机脚本集合（大水库）
## 当前脚本

|  脚本名称 |  用途 |备注 |
| :------------: | :------------: | :------------: |
|Auto_connect_SSH.py|自动SSH登录以续期||
|alist_freebsd_update.py|自动从uubulb/alist-freebsd拉取最新版本更新||

# 自动续期脚本说明

## 说明
　　本项目基于[LINUX DO](https://linux.do)论坛佬友`maohai`的[脚本](https://linux.do/t/topic/66483/15)进行修改，在其基础上增加了`发送通知`、以及`运行日志`功能。

## 发送说明

|  主机状态/设置条件 |  说明 |发送内容 |执行动作 |
| :------------: | :------------: | :------------: | :------------: |
|  200 |  正常 |不发送|无|
|   502|  机子凉了 |服务不可用|通过SSH执行PM2命令|
|   [Errno 1] Address family for hostname not supported| 解析凉了  |解析失败|无|
|  自定义日期 |  固定日启动连接 |每月固定SSH连接提醒|连接SSH|

## 使用方法

　　将脚本放到`domains`目录下，使用`chmod +x Auto_connect_SSH.py`给`Auto_connect_SSH.py`添加可执行权限。  
  
　　在Serv00控制台的定时任务里面新建一个定时任务，`命令`如下：

```shell
/home/你的用户名/domains/Auto_connect_SSH.py
```

#### 参考设置图

![参考图片](https://cdn.linux.do/uploads/default/optimized/3X/f/6/f6516994395858a19637f5acf5baeecec96ea3fa_2_690x445.png)

# Alist自动更新脚本说明

　　将脚本放到`domains`目录下你的 `Alist` 存储路径中，使用`chmod +x alist_freebsd_update.py`给`alist_freebsd_update.py`添加可执行权限。 
　　然后自己到控制台创建一个定时任务。

#### 运行效果图

  ![没有Alist文件](https://cdn.linux.do/uploads/default/original/3X/1/f/1f5b378d086d1935cfaf3927c9fc6c33d531eeb7.jpeg)
  ![已经是最新版](https://cdn.linux.do/uploads/default/original/3X/e/7/e72105ffe5f1ee572cca2ded4138472241553bdb.jpeg)
  ![正常更新](https://cdn.linux.do/uploads/default/original/3X/f/5/f58f94d755825005eae30df9dce0ad1f0b661f43.jpeg)
  
## 参考来源

|  名称 |来源|地址|
| :------------: | :------------: | :------------: |
|Saika|Github|https://github.com/k0baya|
|Eric Lee|Github|https://github.com/giturass|
|maohai|LINUX DO|https://linux.do/t/topic/66483/15|

## SSH登录不上

> 登录不上是因为Ban IP, 点击此处解锁： [Ban](https://www.serv00.com/ip_unban/)

> 还是登录不上的话： 请使用下方 `FinalShell`，并勾上 `智能海外加速`，登录失败在弹出框选择`取消`，在弹出框填入`[邮件中的SSH密码]`

## FinalShell

FinalShell是一体化的的服务器,网络管理软件,不仅是ssh客户端,还是功能强大的开发,运维工具,充分满足开发,运维需求.

### 特色功能:

云端同步,免费海外服务器远程桌面加速,ssh加速,本地化命令输入框,支持自动补全,命令历史,自定义命令参数

- Windows X64版,下载地址: <http://www.hostbuf.com/downloads/finalshell_windows_x64.exe>

- macOS Arm版,支持m1,m2,m3 cpu,下载地址: <http://www.hostbuf.com/downloads/finalshell_macos_arm64.pkg>

- macOS X64版,支持旧款intel cpu,下载地址: <http://www.hostbuf.com/downloads/finalshell_macos_x64.pkg>

- Linux X64版,下载地址: <http://www.hostbuf.com/downloads/finalshell_linux_x64.deb>

- Linux Arm64版,下载地址: <http://www.hostbuf.com/downloads/finalshell_linux_arm64.deb>

- Linux LoongArch64龙芯版,下载地址: <http://www.hostbuf.com/downloads/finalshell_linux_loong64.deb>