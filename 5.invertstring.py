"""
inverta os caracteres de um string.
Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
"""

#entrada, palavra ou texto base, que ficará invertida
entrada = input("Digite alguma coisa: ")

#string vazia para armazenar a string invertida, como se fosse definir a base, quando definimos uma variável com inical zero
string_invertida = ""

for i in range(len(entrada) - 1, -1, -1):
    string_invertida += entrada[i]

print("Você digitou:", entrada)
print("Invertido o que você digitou fica assim:", string_invertida)
