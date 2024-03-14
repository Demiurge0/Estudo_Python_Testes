for n in range(10):
    print(n)

for n in range(10 , 15):
        print(n)

for n in range(15 , 0 , -1):
    print(n)

x = 1;
while x<=15:
    print(x);
    x=x+1

qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor:"))

while (valor > 0):
    soma = soma + valor
    qtd = qtd + 1
    #entrada dos valores.
    valor = float(input("Digite um valor:"))

#caso digite um valor negativo o laço se encerra.
media = soma / qtd
print("\n Total da soma: ", soma)
print("\n Quantidade dos valores digitados:", qtd)
print("\n Média dos valores:", media)