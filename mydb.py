import os
import mysql.connector
import dotenv

dataBase = mysql.connector.connect (
    host = os.environ.get('HOST'),
    user = os.environ.get('USER'),
    passwd = os.environ.get('PASSWRD')
)


# preparando um objeto cursor
cursorObject  = dataBase.cursor()
# Criando o banco de dados
cursorObject.execute('CREATE DATABASE JRG')

