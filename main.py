import operaciones

# un espacio de input para pedirle los números al usuario.
num1 = float(input("Favor ingresar el primer número: "))
num2 = float(input("Favor ingresar el segundo número: "))

# se le pregunta al usuario que tipo de operación desea realizar.
print("¿Que operación desea ejecutar?:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Por favor, ingrese el número que coincide con la operación que quiere ejecutar: ")

# El código procede a ejecutar la operación
if opcion == "1":
    resultado = operaciones.add(num1, num2)
    operacion = "suma"

elif opcion == "2":
    resultado = operaciones.subtract(num1, num2)
    operacion = "resta"

elif opcion == "3":
    resultado = operaciones.multiply(num1, num2)
    operacion = "multiplicación"

elif opcion == "4":
    resultado = operaciones.divide(num1, num2)
    operacion = "división"

else:
    resultado = "Esta opción no es válida."
    operacion = "operación"

# Luego de hacer la operación, le imprime el resultado.
print(f"La {operacion} entre {num1} y {num2} es: {resultado}")
