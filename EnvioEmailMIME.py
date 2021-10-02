import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
msg['From'] = 'email.chippe@gmail.com'
msg['To'] = 'jonatasonca@gmail.com'
msg['Subject'] = 'Chippe Email: Teste de Email Chippe'

body = 'Chippe Email: Teste de Email Chippe'
msg.attach(MIMEText(body, 'plain'))

text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(user='email.chippe@gmail.com', password='@email.chippe#')
server.sendmail(from_addr='email.chippe@gmail.com',
                to_addrs=['jonatasonca@gmail.com', 'paulo.paulon@liran.com.br', 'milene.paulon@hotmail.com'],
                msg=text)
server.quit()
