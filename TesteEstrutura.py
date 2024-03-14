A = input("Informe o valor da Variável A: ")
B = input("Informe o valor da Variável B: ")

if (A>B):
    aux=A;
    A=B;
    B=aux;

print("O valor da Variável A agora é:", A);
print("O valor da Variável B agora é:", B);