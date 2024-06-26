from mysql.connector import Error
import mysql.connector

def connect_db(user, pswd, host, database):
    try:
        cnx = mysql.connector.connect(
            user =  user,
            password = pswd,
            host = host,
            database = database
        )
        if cnx.is_connected():
            print("Conexão com sucesso!")
    except Error as e:
        print("Falha na conexão!")

    return cnx.cursor(), cnx

def insert_data(cursor, conn):
    query_insert = "INSERT INTO produto (nome_produto, valor, quantidade, desconto) VALUES (%s, %s, %s, %s)"
    try:
        product = input("Insira o nome do produto: ")
        value = input("Insira o valor do produto: ")
        quantity = input("Digite a quantidade em estoque do produto:")
        quest = input("O produto possui desconto? (s/n)")

        if quest.lower() == 's':
            discount = input("Digite o valor do desconto: ")
        else:
            discount = 0

        values = [product, value, quantity, discount]
        cursor.execute(query_insert, values)
        conn.commit()
        print("Produto inserido com sucesso!")
    except Exception as err:
        raise Exception(f"Não foi posível inserir o produto! {err}")

def exclude_data(cursor, conn):
    try:
        cursor = conn.cursor()
        id_prod = input("Digite o id do produto que deseja excluir")
        query_delete = "DELETE FROM produto WHERE id_produto = %s"

        cursor.execute(query_delete, (id_prod,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Dados excluidos com sucesso")

    except Error as e:
        print(f"Ocorreu um erro ao deletar {e}")

def update_data(cursor, conn):
    try:
        id_prod = input("Digite o ID do produto: ")
        print("+===========O QUE DESEJA EDITAR?===========+")
        print("| 1 - Nome                                 |")
        print("| 2 - Valor                                |")
        print("| 3 - Quantidade                           |")
        print("| 4 - Dar/Retirar desconto                 |")
        print("+==========================================+")
        op = int(input(">>> "))

        if op == 1:
            new_value = input("Digite o novo nome: ")
            query_update = """
                UPDATE produto SET nome_produto = %s WHERE id_produto = %s
            """
        elif op == 2:
            new_value = input(" Digite o novo preço: ")
            query_update = """
            UPDATE produto SET valor = %s WHERE id_produto = %s
            """
        elif op == 3:
            new_value = input("Digite a nova quantidade: ")
            query_update = """
                UPDATE produto SET quantidade = %s WHERE id_produto = %s
            """
        elif op == 4:
            new_value = input("Digite o valor do desconto: ")
            query_update = """
                UPDATE produto SET desconto = %s WHERE id_produto = %s
            """
        else:
            print("Selecione uma opção válida")

        
        values = [new_value, id_prod]

        cursor.execute(query_update, values)
        conn.commit()

    except Error as e:
        print(f"Erro ao atualizar dados {e}")

def filter_data(cursor, conn):
    print("+===========OPÇÕES DE FILTRO===========+")
    print("| 1 - Filtrar por Nome                 |")
    print("| 2 - Filtrar por Valor                |")
    print("| 3 - Filtrar por Quantidade           |")
    print("| 4 - Filtrar por Desconto             |")
    print("| 5 - Mostrar todos os produtos        |")
    print("+======================================+")
    op = int(input(">>> "))

    if op == 1:
        filtro = input("Digite o nome do produto para filtrar: ")
        query_select = "SELECT * FROM produto WHERE nome_produto LIKE %s"
        values = (f"%{filtro}%",)
    elif op == 2:
        filtro = float(input("Digite o valor máximo do produto para filtrar: "))
        query_select = "SELECT * FROM produto WHERE valor <= %s"
        values = (filtro,)
    elif op == 3:
        filtro = int(input("Digite a quantidade mínima do produto para filtrar: "))
        query_select = "SELECT * FROM produto WHERE quantidade >= %s"
        values = (filtro,)
    elif op == 4:
        filtro = float(input("Digite o valor mínimo do desconto para filtrar: "))
        query_select = "SELECT * FROM produto WHERE desconto >= %s"
        values = (filtro,)
    elif op == 5:
        query_select = "SELECT * FROM produto"
        values = ()
    else:
        print("Selecione uma opção válida")
        return

    try:
        cursor.execute(query_select, values)
        results = cursor.fetchall()
        if results:
            for row in results:
                print(row)
        else:
            print("Nenhum dado encontrado com os critérios fornecidos")
    except Error as e:
        print(f"Erro ao filtrar dados {e}")
