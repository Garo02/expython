def primo_o_no(numero):
    if numero < 2:
        return False, None, 0
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            count = 0
            t = numero
            while t % i == 0:
                t //= i
                count += 1
            return False, i, count
    return True, None, 0

lista_primi = []

x = False
while not x:
    nome = input("Inserisci il tuo nome: ")
    numero = int(input("Inserisci un numero: "))

    primo, divisore, conteggio = primo_o_no(numero)

    if primo:
        print(f"Ciao {nome}, il numero {numero} è primo.")
        lista_primi.append((nome, numero))
    else:
        print(f"Ciao {nome}, il numero {numero} non è primo. Il divisore più piccolo è {divisore} e il numero è divisibile {conteggio} volte per {divisore}.")

    sn = input("Vuoi continuare? (s/n): ")
    if sn.lower() == "n":
        x = True

if lista_primi:
    print("\nLista di nomi e numeri primi salvati:")
    for item in lista_primi:
        print(f"Nome: {item[0]}, Numero primo: {item[1]}")
else:
    print("\nNon ci sono numeri primi salvati.")

