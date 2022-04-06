from Libs.StarEmailLib import  *

emailData=EmailData();
emailData.MsgContent="哈哈哈啊"
emailData.MsgContent="<h1 style='color:blue'>哈哈哈啊</h1>"
emailData.IsHtml=True
emailData.MsgTo="1617070281@qq.com"
EmailInit(emailData).EmailSend();