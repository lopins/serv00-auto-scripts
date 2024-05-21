# Serv00 - 控制面板自动登录脚本

## 使用方法

1. 在 GitHub 仓库中，进入右上角`Settings`

2. 在侧边栏找到`Secrets and variables`，点击展开选择`Actions`，点击`New repository secret`
    
3. 然后创建一个名为`ACCOUNTS_JSON`的`Secret`，将 JSON 格式的账号密码字符串作为它的值，如下格式：  

``` json
[  
  { "username": "qishihuang", "password": "zhanghao", "panelnum": "3" },  
  { "username": "zhaogao", "password": "daqinzhonggong", "panelnum": "1" },  
  { "username": "heiheihei", "password": "shaibopengke", "panelnum": "2" }  
]
```

> 其中`panelnum`参数为面板编号，即为你所收到注册邮件的`panel*.serv00.com`中的`*`数值。

## 贡献

|姓名|主页|内容|
| :------------: | :------------: | :------------: |
|linzjian666|https://github.com/linzjian666|增加多面板支持|

## 参考信息

|  名称 |来源|地址|
| :------------: | :------------: | :------------: |
|Limkon|Github|https://github.com/Limkon|

## SSH登录不上

> 登录不上是因为Ban IP, 点击此处解锁： [Ban](https://www.serv00.com/ip_unban/)

> 还是登录不上的话： 请使用下方 `FinalShell`，并勾上 `智能海外加速`，登录失败在弹出框选择`取消`，在弹出框填入`[邮件中的SSH密码]`

## FinalShell

FinalShell是一体化的的服务器,网络管理软件,不仅是ssh客户端,还是功能强大的开发,运维工具,充分满足开发,运维需求.

### 特色功能

云端同步,免费海外服务器远程桌面加速,ssh加速,本地化命令输入框,支持自动补全,命令历史,自定义命令参数

- Windows X64版,下载地址: <http://www.hostbuf.com/downloads/finalshell_windows_x64.exe>

- macOS Arm版,支持m1,m2,m3 cpu,下载地址: <http://www.hostbuf.com/downloads/finalshell_macos_arm64.pkg>

- macOS X64版,支持旧款intel cpu,下载地址: <http://www.hostbuf.com/downloads/finalshell_macos_x64.pkg>

- Linux X64版,下载地址: <http://www.hostbuf.com/downloads/finalshell_linux_x64.deb>

- Linux Arm64版,下载地址: <http://www.hostbuf.com/downloads/finalshell_linux_arm64.deb>

- Linux LoongArch64龙芯版,下载地址: <http://www.hostbuf.com/downloads/finalshell_linux_loong64.deb>

## PHP配置

https://docs.serv00.com/PHP/#php-version
