<div align="right">
   <strong>中文</strong> | <a href="README.md">English</a>
</div>

<img src="https://www.serv00.com/static/ct8/img/logo.jpg" alt="serv00 logo" width="50" height="50" align="right" />

<div align="center">

<h1> serv00-auto-scripts </h1>

<p>Serv00/CT8 - 免费主机自动续期（自动SSH以及PM2）及其他脚本。</p>

</div>

<hr/>

<div align="center">
<a href="https://panel.serv00.com/">serv00面板</a> | 
<a href="https://www.serv00.com/">serv00官网</a> | 
<a href="https://docs.serv00.com/">serv00文档</a> | 
<a href="https://forum.serv00.com/">serv00社区</a>
</div>

<hr/>

<div align="center">
<a href="https://panel.ct8.pl/">CT8面板</a> | 
<a href="https://www.ct8.pl/">CT8官网</a> | 
<a href="https://wiki.mydevil.net/">CT8文档</a> | 
<a href="https://forum.ct8.pl/">CT8社区</a>
</div>

<hr/>

## 使用方法

1. 在 GitHub 仓库中，进入右上角`Settings`

2. 在侧边栏找到`Secrets and variables`，点击展开选择`Actions`，点击`New repository secret`
    
3. 然后[创建](https://lopins.github.io/serv00-auto-scripts/)一个名为`ACCOUNTS_JSON`的`Secret`，将 JSON 格式的账号密码字符串作为它的值，如下格式：  

``` json
[  
  { "username": "qishihuang", "password": "zhanghao", "panel": "panel3.serv00.com" },  
  { "username": "zhaogao", "password": "daqinzhonggong", "panel": "panel1.serv00.com" },  
  { "username": "heiheihei", "password": "shaibopengke", "panel": "panel.ct8.pl" }  
]
```

> 其中`panel`参数为面板域名，即为你所收到注册邮件的`panel*.serv00.com`值。

4. **非必须** 创建Telegram 机器人两个参数的 `Secret`：`TELEGRAM_BOT_TOKEN` 和  `TELEGRAM_CHAT_ID`

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

## TG机器人

### 创建 Telegram Bot 并获取 Chat ID

#### 步骤 1: 创建 `Telegram Bot`

1. **打开 `Telegram` 应用**：

   - 打开你的 `Telegram` 应用程序。

2. **搜索 `BotFather`**：

   - 在搜索栏中搜索 `@BotFather` 并点击进入。

3. **创建新机器人**：

   - 发送 `/start` 命令启动 BotFather。
   - 发送 `/newbot` 命令创建一个新的机器人。
   - 按照提示输入机器人的名称（可以是你喜欢的任何名称）。
   - 输入机器人的用户名（必须以 `bot` 结尾，例如 `MyBotNameBot`）。
   - BotFather 会生成一个 API token 并提供给你。请保存这个 token，后续会用到。

#### 步骤 2: 获取 Chat ID

为了能够向特定的用户或群组发送消息，你需要知道他们的 `Chat ID`。你可以通过创建一个简单的 `Telegram Bot` 来获取 `Chat ID`。

1. **创建一个简单的 Bot**：

   - 使用你刚刚生成的 `API token` 创建一个简单的 `Bot`。

2. **设置 Webhook 或轮询**：

   - 你可以选择设置 `Webhook` 或使用轮询来接收消息。这里我们使用轮询方式。

3. **获取 Chat ID**：

   - 当用户发送消息给你的 `Bot` 时，你可以从消息中提取 `Chat ID`。
