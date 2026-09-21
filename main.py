sexo = input("Informe o sexo [M/F]: ").strip().upper()

while sexo != "M" and sexo != "F":
  print("Valor inválido. Por favor, digite novamente.")
  sexo = input("Informe o sexo [M/F]: ").strip().upper()

if sexo == "M":
  print("Sexo registrado com sucesso: Masculino.")
else:
  print("Sexo registrado com sucesso: Feminino.")
  


