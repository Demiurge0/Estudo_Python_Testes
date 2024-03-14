notaA=float(input("Digite sua nota A: "))
notaB=float(input("Digite sua nota B: "))

#calcular media
mediaFinal = (notaA + notaB) / 2

#verificação
if mediaFinal >=7:
    print("Sua média é: %.1f - Aprovado." % mediaFinal)
else:
    print("Sua média é: %.1f - Reprovado." % mediaFinal)