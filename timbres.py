numero = int(input("Ingresa un número a convertir en timbres: "))
 # Variables para contar cuántos timbres de cada valor se necesitan
de_50 = 0
de_10 = 0
de_5 = 0
de_1 = 0

if numero >= 10000:
    de_50 = numero // 10000  
    numero = numero % 10000  

if numero >= 2000:
    de_10 = numero // 2000  
    numero = numero % 2000  

if numero >= 1000:
    de_5 = numero // 1000  
    numero = numero % 1000  

if numero >= 200:
    de_1 = numero // 200  
    numero = numero % 200  

print("Total es:", end=" ")
if de_50 > 0:
    print(f"{de_50} de 50", end=", ")
if de_10 > 0:
    print(f"{de_10} de 10", end=", ")
if de_5 > 0:
    print(f"{de_5} de 5", end=", ")
if de_1 > 0:
    print(f"{de_1} de 1", end=", ")


if numero > 0:
    print(f"\nResiduo: {numero} (no se pudo descomponer con los valores de la tabla)")