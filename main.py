import pandas as pd
import datetime as dt
import smtplib
from random import randint

#Abra o arquivo birthdays.csv e coloque os dados de nome, email, data de nascimento.
#Escreva a mensagem que deseja nas cartas, arquivos letter_1,letter_2,letter_3, ou crie mais arquivos.

#Preencha seu e-mail e senha para o envio
MY_EMAIL = "#"
PASSWORD = "#"

#Recebe a data exata para ter o comparativo
now = dt.datetime.now()
today = (now.month, now.day)

# Recebe dados do arquivo csv
data = pd.read_csv("birthdays.csv")

# Dicionario criado para receber mês e dia do arquivo csv - utiliando Dict Comprehensions
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


#Faz o comparativo de data, dia de hoje com o dicionario criado com os dados do arquivo csv
if (today) in birthdays_dict:

    # Recebendo nome e e-mail
    name = birthdays_dict[today]['name']
    email = birthdays_dict[today]['email']
    #Confirmação de e-mail
    print(email)
    #Abre uma das cartas criadas para menssagem de "Feliz aniversario"
    with open(f"letter_templates/letter_{randint(1,3)}.txt") as letter:
        txt = letter.read()

        #Subistitui no texto colocando o nome da pessoa que faz aniversario
        new_letter = txt.replace("[NAME]", name)

        #Utilização do smtplib para envio de e-mail
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:Happy birthday!!\n\n {new_letter}")
