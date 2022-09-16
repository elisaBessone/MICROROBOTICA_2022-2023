l1 = [1, 2, "ciao", 5.0]

#?SLICING
print(l1[:1])
print(l1[1:3])

for x in l1:
    print(x)

#!ciclo for sulla posizione e sull'elemento
for i, elemento in enumerate(l1):
    print(f"Indice {i}: {elemento}")

l2 = [5, 4, 7, 8]

#!ciclo su liste di lunghezza uguale
for elementoL1, elementoL2 in zip(l1,l2):
    print(elementoL1, elementoL2)

#assegnazione multipla
a, b = 1, 2
print(a, b)
#per scambiare
a, b = b, a
print(a, b)

def somma(x, y):
    return x + y
print(somma(5, 3))

#parametri di default, se no passo nulla gli assegna quel valore
def somma(x, y=1):
    return x + y
print(somma(5))


def somma_e_prodotto(x, y):
    return (x + y, x*y)
print(f"SOMMA E PRODOTTO {somma_e_prodotto(5, 3)}")

#!non salvo la somma perchè non mi interessa --> _
_, p = somma_e_prodotto(5, 3)

#tutto è un oggetto, puntatatore alla cella di memoria
print(somma_e_prodotto)

