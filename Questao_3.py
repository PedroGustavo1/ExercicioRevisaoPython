print " 0 = NAO    1 = SIM "
resposta_positiva = 0
print "1 - Telefonou para a vitima?"
resposta_1 = int(raw_input())
if resposta_1 == 1:
    resposta_positiva+=1
print "2 - Esteve no local do crime?"
resposta_2 = int(raw_input())
if resposta_2 == 1:
    resposta_positiva+=1
print "3 - Mora perto da vítima?"
resposta_3 = int(raw_input())
if resposta_3 == 1:
    resposta_positiva+=1
print "4 - Devia para a vítima?"
resposta_4 = int(raw_input())
if resposta_4 == 1:
    resposta_positiva+=1
print "5- Já trabalhou com a vítima?"
resposta_5 = int(raw_input())
if resposta_5 == 1:
    resposta_positiva+=1

if resposta_positiva == 2:
    print "A pessoa é suspeita"
elif resposta_positiva >=3 and resposta_positiva  <=4:
    print "A pessoa é cúmplice"
else:
    print "A pessoa é assasina"
