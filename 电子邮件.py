#需要准备  发送方地址   发送方客户端授权码  SMTP服务器地址  smtp.126.com

#qq授权码  byxuwqafuyodbacg 
#按照邮件发送模块  pip install pyemail
import smtplib
from email.mime.text import MIMEText 


#构造邮件
msg=MIMEText("哈哈哈啊")
msg["Subject"]="phton系统自动发生邮件"
msg["From"]="1245902155@qq.com"
msg["To"]="1245902155@qq.com"
#准备发送
emailEntity=smtplib.SMTP_SSL("smtp.qq.com",465)
emailEntity.login("1245902155@qq.com","byxuwqafuyodbacg")
emailEntity.sendmail("1245902155@qq.com","1617070281@qq.com",msg.as_string())