<div align="right">
   <strong>中文</strong> | <a href="README.md">English</a>
</div>

<img src="https://www.serv00.com/static/ct8/img/logo.jpg" alt="serv00 logo" width="100" height="100" align="right" />

<div align="center">

<h1> serv00-auto-scripts </h1>

<p>Serv00 - 免费主机自动续期（自动SSH以及PM2）及其他脚本。</p>

</div>

<hr/>

<div align="center">
<a href="https://panel.serv00.com/">面板</a> | 
<a href="https://www.serv00.com/">官网</a> | 
<a href="https://docs.serv00.com/">文档</a> | 
<a href="https://forum.serv00.com/">社区</a>
</div>

<hr/>

## 使用方法

1. 在 GitHub 仓库中，进入右上角`Settings`

2. 在侧边栏找到`Secrets and variables`，点击展开选择`Actions`，点击`New repository secret`
    
3. 然后[创建](https://lopins.github.io/serv00-auto-scripts/)一个名为`ACCOUNTS_JSON`的`Secret`，将 JSON 格式的账号密码字符串作为它的值，如下格式：  

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

## 其他服务

- PHP配置: <https://docs.serv00.com/PHP/#php-version>

- Memcached配置: <https://docs.serv00.com/Memcached/>

  启动：memcached -s /usr/home/LOGIN/domains/DOMAIN/memcached.sock -d

- Redis配置: <https://docs.serv00.com/Memcached/>

## 特别注意

serv00虽然有10年使用期，但无法清除Apache和其它服务产生的日志，在容量限制情况下，不建议大日志产生的高流量服务和高频次作业任务。

## Star趋势

[![Stargazers Over Time](https://starchart.cc/lopins/serv00-auto-scripts.svg?variant=adaptive)](https://starchart.cc/lopins/serv00-auto-scripts)

## JSON生成

- <https://lopins.github.io/serv00-auto-scripts/>
