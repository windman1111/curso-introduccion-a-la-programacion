numeroif = int(input("Escribe un número: 1"))

if numeroif < 0:
    print(f"El número {numeroif} es menor que cero")
elif numeroif == 0:
    print(f"El número {numeroif} es igual a cero")

else:
    print(f"El número {numeroif} es mayor que cero")