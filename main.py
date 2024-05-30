from utils.db_actions import *
from config.settings import *

def main():

    cursor, conn = connect_db(USER, PASSWORD, HOST, 'mercado_db')
    cntn = True
    while (cntn):
        print("+===========BEM VINDO AO SISTEMA DE GERENCIAMENTO===========+")
        print("| 1 - Inserir produto                                       |")
        print("| 2 - Editar produto                                        |")
        print("| 3 - Consultar produto                                     |")
        print("| 4 - Excluir produto                                       |")
        print("| 5 - Sair                                                  |")
        print("+===========================================================+")
        print("O que deseja fazer hoje?")
        op = int(input(">>> "))

        if op == 1 :
            insert_data(cursor, conn)
        elif op == 2:
            update_data(cursor, conn)
        elif op == 3:
            filter_data(cursor, conn)
        elif op == 4:
            exclude_data(cursor, conn)
        elif op == 5:
            print("Volte sempre!")
            cntn = False
        else:
            print("Digite um opção válida")
    
    cursor.close()
if __name__ == "__main__":
    main()

