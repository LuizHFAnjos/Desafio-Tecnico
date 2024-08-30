palavra = str(input("Informe uma palavra: "))

contador = palavra.lower().count('a')

if contador > 0:
    print(f"Na palavra ({palavra}) tem {contador} letras 'A'")
else:
    print(f"Não existe letra 'A' na palavra {palavra} ")

