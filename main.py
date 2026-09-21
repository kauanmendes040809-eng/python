valor1 = float(input("digite o primeiro valor: "))
valor2 = float(input("digite o segundo valor: "))

while True:
    print("\n--- MENU DE OPÇÕES ---")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - maior ")
    print("5 - Sair")
  
    opcao = input("Escolha uma opção (1 a 4): ")

    if opcao == "1":
      soma = valor1 + valor2
      print(f"o resultado da soma é: {soma}")

    elif opcao == "2":
      substração = valor1 - valor2 
      print(f"o resultado da substração é: {substração}")

    elif opcao == "3": 
      multiplicação = valor1 * valor2
      print(f"o resultado da multiplicação é: {multiplicação}")

    elif opcao == "4":
       if valor1 > valor2:
            maior = valor1
       else:
          maior = valor2
       print(f" entre [] e [] o maior valor é: {maior}")

    elif opcao == "5":
       print("finalizado")
    else: 
       print("opcao invalida. Tente novamente")
    print('=-= *10')
print("fim do programa! volte sempre! ")


    



