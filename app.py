import requests
import smtplib
import schedule
import time
from email.message import EmailMessage

# Credenciais do email que vai mandar as mensagens
meu_email = "xxxxxxxxxxxxx"
password  = "xxxxxxxxxxxxx"

# Solicitar valor e email do usuario
valor_bitcoin = float(input("Digite o valor limite do bitcoin (em USD): "))
email_usuario = input("Digite seu email para notificações: ")

# Função para obter preço atual do Bitcoin
def preço_bitcoin():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data["bitcoin"]["usd"]

# Função para enviar email
def enviar_email(assunto, meu_email, email_usuario, corpo):
    mail = EmailMessage()
    mail["Subject"] = assunto
    mail["from"] = meu_email
    mail["To"] = email_usuario
    mail.set_content(corpo)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as email:
        email.login(meu_email, password)
        email.send_message(mail)

# Função principal      
def main():
    def checar_preço():
        preço_atual = preço_bitcoin()
        print(f"Preço atual do Bitcoin: U$ {preço_atual}")
        if preço_atual < valor_bitcoin:
            enviar_email("Alerta de preço do Bitcoin", meu_email, email_usuario, f"O preço do Bitcoin caiu para U$ {preço_atual}")

 # Fazer a verificação a cada 10 minutos   
    schedule.every(10).minutes.do(checar_preço)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
