#qq授权码  byxuwqafuyodbacg 
#按照邮件发送模块  pip install pyemail
import smtplib
from email.mime.text import MIMEText 

class EmailData(object):
    def __init__(self):
      
        self.MsgSubject="Python系统发送"
        self.MsgContent=""
        self.MsgTo=""
        self.IsHtml=False

class EmailInit(object):

    #初始化邮件信息
    def __init__(self,emailData):
       self.__MsgFrom="1245902155@qq.com"
       self.__MsgPwd="byxuwqafuyodbacg"   
       if emailData.IsHtml:
          self.msg=MIMEText(emailData.MsgContent,"html","utf-8")
       else:
          self.msg=MIMEText(emailData.MsgContent)
       self.msg["From"]=self.__MsgFrom    
       self.msg["Subject"]=emailData.MsgSubject
       self.msg["To"]=emailData.MsgTo

    #发送邮件
    def EmailSend(self):
        try:
            emailEntity=smtplib.SMTP_SSL("smtp.qq.com",465)
            emailEntity.login(self.__MsgFrom,self.__MsgPwd)
            emailEntity.sendmail(self.__MsgFrom,self.msg["To"],self.msg.as_string())
            return "发送成功."
        except Exception as e:
            return "发送失败."