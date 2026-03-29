from random import choice
from services.item_service import ItemService
from services.box_service import BoxService
from services.report_service import ReportService
import os

def menu():
    while True:
        clear_screen()
        print("\n" + "=" * 30)
        print("REGISTRO E GERENCIAMENTO DE PEÇAS")
        print("=" * 30 + "\n")
        print("1 - Produção em massa (max 15)")
        print("2 - Registrar uma peça")
        print("3 - Listar peças")
        print("4 - Listar caixas fechadas")
        print("5 - Listar peças por caixas")
        print("6 - Listar peças inválidas")
        print("7 - Excluir uma peça")
        print("8 - Exibir relatório")
        print("0 - Fechar menu")
        print('\n')

        actionType = input("Escolha uma opção: ")
       
        if actionType == '1':
            start_production()

        elif actionType == '2':
            register_single_item()

        elif actionType == '3':
            items_index()
     
        elif actionType == '4':
            closed_boxes_index()

        elif actionType == '5':
            box_index()

        elif actionType == '6':
            invalid_items_index()
    
        elif actionType == '7':
            delete_item()
    
        elif actionType == '8':
            report()
       
        elif actionType == '0':
            print("\n" + "=" * 30)
            print("Encerrando...")
            print("=" * 30 + "\n")
            break

        else:
            print('Código inválido')
            continue

        if not return_or_close_menu():
            clear_screen()
            print("\n" + "=" * 30)
            print("Encerrando...")
            print("=" * 30 + "\n")
            break

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_production():
   # simula produção com dados aleatórios (inclui peças inválidas)
   qtyOfParts = int(input('insira a quantidade de pecas a serem confeccionadas: '))
   if qtyOfParts < 1 or qtyOfParts > 15:
       return print('Não é possível produzir a quantidade requerida!')

   for _ in range(qtyOfParts):
        service = ItemService()
        service.store_part(
            choice([70, 99, 105]),
            choice(['azul', 'verde', 'vermelho']),
            choice([7, 10, 17])
      )
  
def register_single_item():
    weight_g = int(input("Peso (g): "))
    color = input("Cor: ")
    length_cm = int(input("Tamanho (cm): "))
    service = ItemService()
    service.store_part(weight_g, color, length_cm)

def items_index():
    service = ItemService()
    service.list_items()

def invalid_items_index():
    service = ItemService()
    service.list_invalid_items()

def closed_boxes_index():
    service = BoxService()
    service.list_closed_boxes()

def box_index():
    service = BoxService()
    service.list_boxes()
    service.show_box_items()

def delete_item():
    service = ItemService()
    service.delete_item()

def report():
    service = ReportService()
    service.generate()

def return_or_close_menu():
    print("\n" + "=" * 30)
    close_menu = input("Pressione ENTER para voltar ao menu ou 0 para finalizar: ")
    print("=" * 30)

    if close_menu == "0":
        return False 

    clear_screen() 
    return True 
  
menu()