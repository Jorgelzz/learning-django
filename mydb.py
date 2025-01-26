import mysql.connector

dataBase = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    passwd = 'admin'
)


# preparando um objeto cursor

cursorObject  = dataBase.cursor()

# Criando o banco de dados

cursorObject.execute('CREATE DATABASE JRG')

