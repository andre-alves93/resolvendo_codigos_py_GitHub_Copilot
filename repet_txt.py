# Solicita uma string
texto = input("Digite uma string: ")

# Solicita um número inteiro
numero = int(input("Digite um número inteiro: "))

# Repete a string pelo número de vezes especificado, com espaço entre as repetições
resultado = (texto + " ") * numero

# Exibe o resultado, removendo o espaço extra ao final
print("Resultado:", resultado.strip())
