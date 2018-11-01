nota_1 = float(raw_input("Digite a Primeira nota: "))
nota_2 = float(raw_input("Digite a Segunda nota: "))
nota_3 = float(raw_input("Digite a Terceira nota: "))

media = (nota_1+nota_2+nota_3)/3

if media == 10:
    print "Aprovado com Distinção"
elif media < 7:
    print "Reprovado"
elif media >= 7:
    print "Aprovado"

    
