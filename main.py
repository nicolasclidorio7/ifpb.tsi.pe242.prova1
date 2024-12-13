def q1():
    """
    Dado um número inteiro x, retorne verdadeiro se x for um palíndromo, e falso caso contrário.

    """

def eh_palindromo(x):  
    str_x = str(x)  
    return str_x == str_x[::-1]  

# Função para imprimir o resultado  
def verificar_palindromo(x):  
    if eh_palindromo(x):  
        print("True")  
    else:  
        print("False")  

# Teste  
verificar_palindromo(121)   # Saída esperada: True  
verificar_palindromo(-121)  # Saída esperada: False  
verificar_palindromo(10)    # Saída esperada: False


def q2():
    """
    Dado um numeral romano, converta-o para um número inteiro.
    """
    
def romano_para_inteiro(s):  
    valores = {  
        'I': 1,  
        'V': 5,  
        'X': 10,  
        'L': 50,  
        'C': 100,  
        'D': 500,  
        'M': 1000  
    }  
    
    total = 0  
    n = len(s)  
    
    for i in range(n):  
        if i < n - 1 and valores[s[i]] < valores[s[i + 1]]:  
            total -= valores[s[i]]  
        else:  
            total += valores[s[i]]  
            
    return total  

# Função para imprimir o resultado  
def imprimir_romano(s):  
    resultado = romano_para_inteiro(s)  
    print(resultado)  

# Testes  
print ("III")      # Saída esperada: 3  
print("MCMXCIV")  # Saída esperada: 1994