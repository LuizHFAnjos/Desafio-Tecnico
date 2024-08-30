entrada = int(input("Informe um numero: "))

n1, n2 = 0, 1


if entrada == 0 or entrada ==1:
    Fibonacci = True 
else:
    Fibonacci = False
    while n2 < entrada:
        n1,n2 = n2, n1 + n2

    if n2 == entrada:
        Fibonacci = True

if Fibonacci:
    print(f" {entrada} pertence a sequência Fibonacci")
else:
    print(f"{entrada} NÃO pertence a sequência Fibonacci")