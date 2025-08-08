#EX 01 

#Implemente um programa que receba a idade de uma pessoa e imprima mensagem de acordo com os critérios:
#● Menor de 16 anos: MENOR
#● Entre 16 e 18 anos: EMANCIPADO
#● Maior de 18 anos: MAIOR


# idade =  int(input("Digite a sua idade: "))

#if idade < 16:
#    print("Você ainda é menor de idade")
#elif idade == 16 or idade <= 18:
#    print("você é emancipado")
#else:
#    print("Você é maior de idade")

#-----------------------------------------------------------------------------------------------------------------

#EX 02


#while True: 
nadador = int(input("Digite a sua idade: "))

if nadador < 5:
        print("idade não é compativel com nenhuma categoria")
elif nadador == 5 or nadador <= 7:
        print("Infantil A")
elif nadador == 8 or nadador <= 10:
        print("Infantil B")
elif nadador == 11 or nadador <= 13:
        print("Juvenil A")
elif nadador == 14 or nadador <= 17:
        print("Juvenil B")
else:
        print("idade não é compativel com nenhuma categoria")