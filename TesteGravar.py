#Criação da Gravação do Arquivo de Texto
arquivo = open('arqText.txt', 'w')

arquivo.write('Curso Python \n')
arquivo.write('Aula Prática')
arquivo.close()

#Leitura da Gravação do Arquivo de Texto
leitura = open('arqText.txt', 'r')
print(leitura.read())
leitura.close()