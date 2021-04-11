n = int(input("Ingrese un número:"))
lista = [x for x in range (1, n+1)if x % 7 ==0 or x % 10 ==7]
print (lista)
