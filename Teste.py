codigo = int(input("Digite o código de funcionário:"))
nome = input("Digite o nome do funcionário:")
salario = float(input("Digite o  salário do funcionário:"))
situacao = True

tipo = type(salario)

print(salario)
print(tipo)

print("codigo:", codigo, "nome:", nome, "o salário atual é:", salario)

print("codigo: " + str(codigo) + "nome: " + str(nome) + "o salário atual é: " + str(salario))

print("código: %d" % codigo)
print("nome: %s" % nome)
print("salário: %.2f" % salario)
print("situação: %r" % situacao)

fruta = input("Qual sua fruta favorita?")
print(fruta)

