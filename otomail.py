import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders

####################################################################################
# "ÖNEMLİ: 2 Faktorlu doğrulamayı etkineleştirin ve uygulama şifreleri kısmına girip python isminde yeni bir uygulama erişim verin."
send_from =  "DLA"
persons_list = {"person1":'deneme0@gmail.com',
               "person2":'deneme1@gmail.com',
               "person3":'deneme2@gmail.com'}
subject = "Mail Başlığı"
body = (""" Buraya metin girilecek

""")

username  =  "mail adresiniz"
password =  "Alınan uygualama şifresi"
attachmentPath  = "/Users/emir/Desktop/Emir.cv3.2.pdf"   # uygulama hedef yolu       
####################################################################################

msg = MIMEMultipart()

msg['From'] = send_from
msg['To'] = persons_list
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = subject
server = "smtp.gmail.com"
port = 587
use_tls = True

msg.attach(MIMEText(body))
#msg.attach(MIMEText(emailBody ,'html'))

#### EK KODU ***** EKİ HARİÇ TUTMAK İÇİN AŞAĞIDAKİ YORUMDAN ÇIKIN *******

part = MIMEBase('application', "octet-stream")
with open(attachmentPath, 'rb') as file:
    part.set_payload(file.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',
                'attachment; filename="{}"'.format(Path(attachmentPath).name))
msg.attach(part)

#### EKİ HARİÇ TUTMAK İÇİN YUKARIDAKİ KODU YORUMLAYIN *******

smtp = smtplib.SMTP(server, port)
if use_tls:
    smtp.starttls()
smtp.login(username, password)
smtp.sendmail(send_from, persons_list, msg.as_string())
smtp.quit()

print ("Mail Gönderildi")