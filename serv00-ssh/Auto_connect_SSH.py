#!/usr/bin/env python3
import os  
import requests  
import paramiko  
import socket  
from datetime import datetime  
import pytz  
  
# 预先定义的常量  
url = '你检测的地址，参考下一行注释'  
# 测试URL 这个URL是个凉了的 url = 'https://edwgiz.serv00.net/'
ssh_info = {  
    'host': 's3.serv00.com',    # 主机地址
    'port': 22,  
    'username': '你的用户名',       # 你的用户名，别写错了
    'password': '你的SSH密码'       # 你注册的时候收到的密码或者你自己改了的密码
}

WECHAT_ROBOT_KEY  = '你的企业微信机器人的Key部分'      # 需要替换成你的企业微信机器人的Webhook Key，参考 https://open.work.weixin.qq.com/help2/pc/14931
webhook_url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={WECHAT_ROBOT_KEY}'     # 企业微信机器人的Webhook地址

# 获取当前脚本文件的绝对路径
script_dir = os.path.dirname(os.path.abspath(__file__))

# 日志文件将保存在脚本所在的目录中
log_file_path = os.path.join(script_dir, 'Auto_connect_SSH.log')
wechat_message_sent = False     # 标记是否已经发送了成功的企业微信提醒消息
flush_log_message = []      # 用于存储日志信息的全局变量
# 写入日志的函数
def write_log(log_message):
    global flush_log_message
    if not os.path.exists(log_file_path):
        open(log_file_path, 'a').close()  # 创建日志文件
        os.chmod(log_file_path, 0o644)  # 设置#日志文件有可编辑权限（644权限）
    log_info = f"{log_message}"
    flush_log_message.append(log_info)

# 把所有的日志信息写入日志文件
def flush_log():
    global flush_log_message
    # 获取当前系统时间、北京时间、星期以及 SSH 用户名，然后将所有信息合并为一行写到日志里面
    username = ssh_info['username']
    system_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    beijing_time = datetime.now(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
    current_day = datetime.now(pytz.timezone('Asia/Shanghai')).weekday()
    weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    current_weekday_name = weekdays[current_day]
    flush_log_messages = f"{system_time} - {beijing_time} - {current_weekday_name} - {url} - {username} - {' - '.join(flush_log_message)}"
    # 写入日志文件，并添加换行符
    with open(log_file_path, "a", encoding="utf-8") as log_file:
        log_file.write(flush_log_messages + '\n')
    # 清空累积的日志信息列表
    flush_log_message.clear()      # 清空累积的消息，避免下一次会有重复消息

# 发送企业微信消息的函数  
def send_wechat_message(message):  
    global wechat_message_sent  # 声明为全局变量
    headers = {'Content-Type': 'application/json'}  
    try:  
        response_wechat = requests.post(webhook_url, json=message, headers=headers)  
        response_wechat.raise_for_status()
        wechat_status = "企业微信提醒消息发送成功"  
        print("温馨提醒：企业微信提醒消息发送成功。")  
    except requests.RequestException as e:
        wechat_status = f"企业微信提醒消息发送失败，错误码: {e}"  
        print(f"警告：企业微信提醒消息发送失败！\n错误码: {e}")  
    finally:
        # 测试的时候发现如果碰到又是规定的定期执行时间还有碰巧主机凉了会写两遍日志，改为只有在消息尚未发送的情况下才记录日志
        if not wechat_message_sent:
            write_log(f"{wechat_status}")
            wechat_message_sent = True  # 消息发送后，将标记设置为 True
  
# 尝试通过SSH恢复PM2进程的函数  
def restore_pm2_processes():  
    transport = paramiko.Transport((ssh_info['host'], ssh_info['port']))  
    try:  
        transport.connect(username=ssh_info['username'], password=ssh_info['password'])  
        # 创建SSH通道
        ssh = paramiko.SSHClient()  
        ssh._transport = transport  
        try:    # 执行pm2 resurrect命令
            stdin, stdout, stderr = ssh.exec_command('/home/你的用户名/.npm-global/bin/pm2 resurrect')  
            print("STDOUT: ", stdout.read().decode())  
            print("STDERR: ", stderr.read().decode())  
            stdout.channel.recv_exit_status()  # 等待命令执行完成
            if stdout.channel.exit_status == 0:
                write_log("通过SSH执行PM2命令成功")
                print("温馨提醒：PM2进程恢复成功。")
            else:
                write_log(f"通过SSH执行PM2命令时出错，错误信息：{stderr.read().decode()}")
                print("警告：PM2进程恢复失败！\n错误信息：", stderr.read().decode())
        except Exception as e:  
            write_log(f"通过SSH执行PM2命令时出错: {e}")
            print(f"通过SSH执行命令时出错: {e}")  
    finally:  
        ssh.close()  # 关闭SSHClient
        transport.close()    # 关闭Transport连接

# 尝试通过SSH连接的函数
def ssh_connect():
    try:
        transport = paramiko.Transport((ssh_info['host'], ssh_info['port']))
        transport.connect(username=ssh_info['username'], password=ssh_info['password'])
        ssh_status = "SSH连接成功"
        print("SSH连接成功。")
    except Exception as e:
        ssh_status = f"SSH连接失败，错误信息: {e}"
        print(f"SSH连接失败: {e}")
    finally:
        transport.close()
        write_log(f"{ssh_status}")

# 检查是否为每月的1号
def is_first_day_of_month():
    now = datetime.now(pytz.timezone('Asia/Shanghai'))      # 机子时间是UTC时间，为了便于识别这里需要使用东八区北京时间
    print("本来应该是系统时间，但是我要改成北京时间增强辨识度：",now)
    current_day = now.day    # 获取当前的天数
    return current_day == 1 or current_day == 15    # 设置每个月的哪一天或哪几天为每月固定SSH日期（如果只想每个月第一天就只需要保留return current_day == 1即可）        

# 返回当前的天、月和一年中的第几天
def get_day_info():
    now = datetime.now(pytz.timezone('Asia/Shanghai'))      # 使用东八区北京时间
    print("北京时间：",now)
    current_day = now.day
    current_month = now.month
    current_year_day = now.timetuple().tm_yday  # 今年中的第几天
    current_weekday = now.weekday()  # 返回一个 0-6 的整数，0 是星期一，6 是星期日
    weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    current_weekday_name = weekdays[current_weekday]
    return current_day, current_month, current_year_day, current_weekday_name

# 每个月发送仅包含URL和时间的提醒消息
def send_monthly_reminder():
    current_day, current_month, current_year_day, current_weekday_name = get_day_info()
    system_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    beijing_time = datetime.now(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
    message = {
        "msgtype": "text",
        "text": {
            "content": f" [鼓掌]每月固定SSH提醒[鼓掌] \n-------------------------------------\n检测地址:\n{url}\n-------------------------------------\n　　今天是{current_month}月{current_day}日( {current_weekday_name} )，本月的第 {current_day} 天，今年的第 {current_year_day} 天，例行SSH连接已经成功执行，以防万一空了可以到后台查看记录！\n-------------------------------------\n系统时间: {system_time}\n北京时间: {beijing_time}"
        }
    }
    return message

# 每月一次检查提醒
if is_first_day_of_month():
    message = send_monthly_reminder()
    send_wechat_message(message)
    ssh_connect()

# 检查URL状态和DNS的函数  
def check_url_status_and_dns():  
    try:  
        # 尝试解析URL的域名  
        host = socket.gethostbyname(url.split('/')[2])  
        print(f"解析成功，IP地址为: {host}")
        write_log(f"{host}")
    except socket.gaierror as e:  
        # 解析失败，发送通知  
        write_log(f"Error: {e}")
        system_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
        beijing_time = datetime.now(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')  
        message = {  
            "msgtype": "text",  
            "text": {  
                "content": f"----- [炸弹]解析失败提醒[炸弹] -----\n地址: {url}\n错误: {e}\n[恐惧]抓紧尝试检查解析配置或联系管事的老铁。\n-------------------------------------\n系统时间: {system_time}\n北京时间: {beijing_time}"  
            }  
        }  
        send_wechat_message(message)  
        return  
  
    # 尝试获取URL的状态码  
    response = requests.get(url, timeout=10)  
    if response.status_code != 200:  
        # URL状态码不是200，发送通知并尝试恢复PM2进程  
        system_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
        beijing_time = datetime.now(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')  
        message = {  
            "msgtype": "text",  
            "text": {  
                "content": f"----- [裂开]当前服务不可用[裂开] -----\n地址: {url}\n状态码: {response.status_code}\n[加油]正在尝试通过SSH恢复PM2进程，请稍后手动检查恢复情况！\n-------------------------------------\n系统时间: {system_time}\n北京时间: {beijing_time}"  
            }  
        }
        write_log(f"主机状态码: {response.status_code}")  
        send_wechat_message(message)  
        restore_pm2_processes()  
    else:  
        write_log(f"主机状态码: {response.status_code}")
        print(f"主机状态码: {response.status_code}")  

if __name__ == '__main__':
    # 检查URL状态和DNS
    check_url_status_and_dns()
    # 所有日志信息已经收集完成，写入日志文件
    flush_log()
