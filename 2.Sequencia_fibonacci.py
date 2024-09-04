"""
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), vamos informar um número que, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
"""

def pertence_fibonacci(n):
    #definido os valores iniciais de acordo com o enunciado
    constante_1 = 0
    constante_2 = 1
    #condição
    if n == constante_1 or n == constante_2:
        return f"O número {n} pertence à sequência de Fibonacci."

    #condição de que valor seja maior ou igual ao número informado
    while constante_2 < n:
        constante_1, constante_2 = constante_2, constante_1 + constante_2

    #verificação
    if constante_2 == n:
        return f"O número {n} faz parte da sequência de Fibonacci."
    else:
        return f"O número {n} não faz parte sequência de Fibonacci."

#input, digitar qualquer número inteiro, se o número estiver na sequencia dará uma resposta positiva, se não irá retornar uma negativa.
numero = int(input("Informe um número: "))
resultado = pertence_fibonacci(numero)
print(resultado)
