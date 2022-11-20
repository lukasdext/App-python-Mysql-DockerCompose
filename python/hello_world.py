from mysql.connector import connect

conexao = connect(
    passwd='root',
    port=3306,
    user='root',
    host='mysql',
    database= 'db'
)


sql = 'Select Mensagem FROM students'

cursor = conexao.cursor()
cursor.execute(sql)

result  = cursor.fetchall() # resultado da query

print("\n Mensagem do banco:", result)

conexao.close()
print("Fechando conexão com o banco")