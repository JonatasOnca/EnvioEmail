import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(user='email.chippe@gmail.com', password='password')
server.sendmail(from_addr='email.chippe@gmail.com',
                to_addrs=['email.chippe@gmail.com'],
                msg='Chippe Email: Teste de Email Chippe',
                rcpt_options='')
