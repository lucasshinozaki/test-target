#5) Escreva um programa que inverta os caracteres de um string.
def inverter_string(s):
    resultado = ''
    for char in s:
        resultado = char + resultado
    return resultado

entrada = input("Digite uma string para inverter: ")
string_invertida = inverter_string(entrada)
print(f"String invertida: {string_invertida}")