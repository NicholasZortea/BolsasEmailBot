import smtplib, ssl
from email.mime.text import MIMEText

class EnviaEmail:
    porta = 465
    password = 'senha do endereco que vai enviar o email' #como estou utilizando o gmail precisa ser a senha criada para apps e nao a senha da conta
    contaQueEnvia = "contaQueEnvia@gmail.com"
    contaQueRecebe = "contaQueRecebe@gmail.com"

    def enviaEmail(self, corpoDoEmail):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", self.porta, context=context) as server:
            server.login("contaQueEnvia@gmail.com", self.password)
            corpoDoEmail = MIMEText(corpoDoEmail,'plain','utf-8')
            server.sendmail(self.contaQueEnvia, self.contaQueRecebe, corpoDoEmail.as_string())
            server.close()
