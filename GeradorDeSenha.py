

base = input("Digite a sua senha (apenas letras): ")
senha = ""


for letras in base:
    if letras in "Aa": 
        senha =  senha + "4"
    elif letras in "Ii":
        senha = senha + "1"
    elif letras in "Oo":
        senha = senha + "0"
    elif letras in "Ee":
        senha = senha + "3"
    elif letras in "Uu":
        senha = senha + "8"
    else:
        senha += letras           
                
print(senha)
                
                
                
            