#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header

 
# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="904311392@qq.com"    #用户名
mail_pass="fqajmckxmzisbebi"   #口令
 

sender = '904311392@qq.com'
receivers = ['904311392@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')   #三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message['From'] = Header("dj", 'utf-8')
message['To'] =  Header("张三", 'utf-8')
 
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = t.SMTP_SSL(mail_host)  # SMTP over SSL 默认端口号为465
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件", e)
