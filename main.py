def q1():
    """
    Dado um número inteiro x, retorne verdadeiro se x for um palíndromo, e falso caso contrário.

    """
    def is_palindromo(x):
        #convertendo o número para string
        str_x =str(x)

        #verificando se a string é igual á sua reversa
        return str_x == str_x[::-1] and x >= 0
    
   #Exemplos de uso

    print(is_palindromo(121)) # saida: True
    print(is_palindromo(-121)) # saida: False
    print(is_palindromo(10)) #saida: False


def q2():
    """
    Dado um numeral romano, converta-o para um número inteiro.
    """
def romanToInt(s: str) -> int:  
    # Mapeia os símbolos romanos para os respectivos valores  
    roman_values = {  
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
        # Obtemos o valor do símbolo atual  
        current_value = roman_values[s[i]]  
        
        # Se não é o último símbolo e o próximo é maior,  
        # subtraímos o valor atual ao invés de somá-lo.  
        if i < n - 1 and current_value < roman_values[s[i + 1]]:  
            total -= current_value  
        else:  
            total += current_value  
            
    return total  

# Exemplos de teste  
print(romanToInt("III"))      # Output: 3  
print(romanToInt("LVIII"))    # Output: 58  
print(romanToInt("MCMXCIV"))  # Output: 1994

