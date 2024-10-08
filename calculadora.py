def menu_calc():
    print("\nCalculadora")
    print("\nO que você deseja calcular?")
    print("1. Somar")
    print("2. Subtrair")
    print("3. multiplicar")
    print("4. dividir")
    print("5. Vizualizar histórico")
    print("6. Sair")

def somar():
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero: "))
    soma = num1 + num2
    print(f"O resultado é {soma}")
    hist_soma.append(soma)
    
    
def subtrair():
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero: "))
    sub = num1 - num2
    print(f"O resultado é {sub}")
    hist_sub.append(sub)
    
def multiplicar():
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero: "))
    mult = num1 * num2
    print(f"O resultado é {mult}")
    hist_mult.append(mult)

def dividir():
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero: "))
    div = num1 / num2
    print(f"o resultado é {div}")
    hist_div.append(div)


hist_soma = []
hist_sub = []
hist_mult = []
hist_div = []
   
while True:
    menu_calc()
    try:
        esc = int(input("Digite a opção: "))
    except ValueError:
        print("\nOpção invalida, tente novamente ")
        continue
    
    if esc == 1:
        somar()
        
    elif esc == 2:
        subtrair()
        
    elif esc == 3:
        multiplicar()
        
    elif esc == 4:
        dividir()
        
    elif esc == 5:
        print("\nHistorico de soma: ")
        for soma in hist_soma:
            print(soma)
       
        print("\nHistorico de subtrações: ")
        for sub in hist_sub:
            print(sub)
       
        print("\nHistorico de multiplicação: ")
        for mult in hist_mult:
            print(mult)
        
        print("\nHistorico de divisão: ")
        for div in hist_div:
            print(div)
            
    elif esc == 6:
        print("saindo da calculadora")
        break
    else:
        print("Opção invalida, tente novamente: ")


print("esse é o commit 1")
print("esse é o commit 2")