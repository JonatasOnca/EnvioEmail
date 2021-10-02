import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(user='email.chippe@gmail.com', password='@email.chippe#')
server.sendmail(from_addr='email.chippe@gmail.com',
                to_addrs=['jonatasonca@gmail.com', 'paulo.paulon@liran.com.br', 'milene.paulon@hotmail.com'],
                msg='Chippe Email: Teste de Email Chippe',
                rcpt_options='')
