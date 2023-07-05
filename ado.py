import pyautogui

while True:
    print("Menu:")
    print("1 - Opção 1")
    print("2 - Opção 2")
    print("3 - Opção 3")
    print("0 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        print("Opção 1 selecionada")
    elif escolha == "2":
        print("Opção 2 selecionada")
    elif escolha == "3":
        print("Opção 3 selecionada")
    elif escolha == "0":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida, tente novamente.")