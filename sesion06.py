# print("Tipos de datos booleanos")
# print(True)
# print(False)
# print(True + True)
# print(True * True)
# print(True * False)
# print(False + False)
# print(False * False)
#
# print("Números y booleanos")
# print(210 + True)
# print(210 + False)
# print(210 * True)
# print(210 * False)

# print("Declarar variables booleanas")
# var_booleana = True
# print(var_booleana)
# print(type(var_booleana))
# var_booleana = False
# print(var_booleana)
# print(type(var_booleana))
#
# print("Declarar mediante función bool()")
# var_booleana = bool(1)
# print(var_booleana)
# print(type(var_booleana))
# var_booleana = bool(0)
# print(var_booleana)
# print(type(var_booleana))
# var_booleana = bool(-15)
# print(var_booleana)
# print(type(var_booleana))

# print("Operadores de comparación")
# print(10 == 10)
# print(10 != 10)
# print(10 < 10)
# print(10 > 10)
# print(10 <= 10)
# print(10 >= 10)
# a = 10
# b = 10
# print(a is b)
# print(a is not b)

# print(type(diferente_de_10))

# print("Operadores lógicos")
# print(True and True)
# print(True and False)
# print(False or True)
# print(False or False)
# print(not True)
# print(not False)

# print("Operadores lógicos y prioridad")
# print(False and False or True)
# print(False and (False or True))
# print(not True and False or True)
# print(not (True and False or False))
# print(not True and (False or False))
# print(not True and False or False)

# print("Operador AND")
# print(11 > 10 and 5 > 0)
# print(11 > 10 and 5 < 0)
# print(5 < 0 and 11 > 10)
# print(5 < 0 and 5 < 0)

# print("Operador OR")
# print(10 != 0 or 10 != 0)
# print(10 != 0 or 3 + 5 > 10)
# print(3 + 5 > 10 or 10 != 0)
# print(3 + 5 > 10 or 3 + 5 > 10)

# print("Operador NOT")
# print(not 10 - 10)
# print(not 17**2)

# print("Operador NAND")
# print(not (True and True))
# print(not (True and False))
# print(not (False and True))
# print(not (False and False))

# print("Operador NOR")
# print(not (True or True))
# print(not (True or False))
# print(not (False or True))
# print(not (False or False))

# print("Operador XOR")
# a = False
# b = True
# print((a or b) and not (a and b))
# a = False
# b = False
# print((a or b) and not (a and b))

# print("Ejemplo de uso Sensor y Batería")
# sensor = True
# bateria = True
# print(sensor, "and", bateria, "=", sensor and bateria)
# sensor = True
# bateria = False
# print(sensor, "and", bateria, "=", sensor and bateria)
# sensor = False
# bateria = True
# print(sensor, "and", bateria, "=", sensor and bateria)
# sensor = False
# bateria = False
# print(sensor, "and", bateria, "=", sensor and bateria)
###Determinar si el número 20 está en el rango 0 a 100
# x = 20
# print(x >= 0 and x <= 100)
######
# numero = 20
#
# rango_inferior = numero >= 0
# rango_superior = numero <= 100
#
# resultado = rango_inferior and rango_superior
# print(resultado)

# Si es True está en este rango
# Si es False no está en este rango

# numero = 20
# print(numero > 0 and numero < 100)
#
# a = 20
# print(a >= 0 and a <= 100)
#
## print(20>=0and20<=100)
#
## numero = 20 print(numero >=0 and numero <=100)
#
# num = 20
# print(num > 0 and num < 100)
#
# print(20 >= 0 and 20 <= 100)
#
# g = 20 >= 0 and 20 <= 100
# if g:
#    print("El 20 esta entre 0 y 100")
# else:
#    print("El 20 no esta entre 0 y 100")
#
#
# print("Ejemplo 1 - Comparación y Lógicos")
# numero = 20
# print(numero >= 0 and numero <= 100)

# nota_1 = 15
# nota_2 = 20
# nota_3 = 16
# nota_aprobacion = 50
# print(nota_1 + nota_2 + nota_3 > nota_aprobacion)
#
# primer_examen = 15
# segundo_examen = 20
# tercer_examen = 16
# suma_examen = primer_examen + segundo_examen + tercer_examen
# print(suma_examen > 50)
#
# nota1 = 15
# nota2 = 20
# nota3 = 16
# nota_final = nota1 + nota2 + nota3
# print(nota_final > 50)
#
# nota_a = 15
# nota_b = 20
# nota_c = 16
# nota_final = (nota_a + nota_b + nota_c) > 50
# print(nota_final)
#
# nota_1 = 15
# nota_2 = 20
# nota_3 = 16
# nota_total = nota_1 + nota_2 + nota_3
# print(f"{nota_total=},", nota_total > 50)
#
# notas = [15, 20, 16]
# suma_notas = sum(notas)
# aprobado = suma_notas > 50
# print(f"Suma total de notas: {suma_notas}")
# print(f"Aprobo con nota superior a 50? {aprobado}")
#
# primer_puntaje = 15
# segundo_puntaje = 20
# tercer_puntaje = 16
#
# suma_total_puntaje = primer_puntaje + segundo_puntaje + tercer_puntaje
#
# print(suma_total_puntaje > 50)  # Aprobo si es True
#
# nota_1 = 15
# nota_2 = 20
# nota_3 = 16
# suma_notas = nota_1 + nota_2 + nota_3
# print(suma_notas > 50)
#
# print("Ejemplo 2 - Aritméticos y comparación")
# nota1 = 15
# nota2 = 20
# nota3 = 16
# print((nota1 + nota2 + nota3) > 50)

## Determinar si el número 15 es divisible por 3 y 5, pero no por 2
# numero15 = 15
# modulo_3 = numero15 % 3 == 0
# modulo_5 = numero15 % 5 == 0
# modulo_2 = numero15 % 2 != 0
# print(modulo_3 and modulo_5 and modulo_2)
#
# numero = 15
# div_3 = 15 % 3 == 0
# div_5 = 15 % 5 == 0
# div_2 = 15 % 2 == 0
#
# print("divisible entre 3", div_3)
# print("divisible entre 5", div_5)
# print("divisible entre 2", div_2)
#
# numero = 15
# divisible_por_3 = numero % 3 == 0
# divisible_por_5 = numero % 5 == 0
# divisible_por_2 = numero % 2 == 0
# print(divisible_por_3 and divisible_por_5 and not (divisible_por_2))
#
# numero = 15
# condicion = (numero % 3 == 0) and (numero % 5 == 0) and (numero % 2 != 0)
# print(condicion)  # true o false
#
# numero = 15
# divisible_3 = numero % 3 == 0
# divisible_5 = numero % 5 == 0
# no_divisible_2 = numero % 2 != 0
# verificacion = divisible_3 and divisible_5 and no_divisible_2
# print(verificacion)
#
# numero_eval = 15
# divisor_1 = 3
# divisor_2 = 5
# divisor_3 = 2
# print(
#    numero_eval % divisor_1 == 0
#    and numero_eval % divisor_2 == 0
#    and not (numero_eval % divisor_3 == 0)
# )
#
# num = 15
# divisible_1 = num % 3 == 0
# divisible_2 = num % 5 == 0
# divisible_3 = num % 2 == 1
# print(divisible_1 and divisible_2 and divisible_3)
#
# numero = 15
# divisible_tres = numero % 3 == 0
# divisible_cinco = numero % 5 == 0
# divisible_dos = numero % 2 != 0
# resultado = (divisible_tres and divisible_cinco) and divisible_dos
# print(resultado)
#
# print("Ejemplo 3 - Aritméticos, comparación y lógicos")
# numero = 15
# print((numero % 3 == 0) and (numero % 5 == 0) and (numero % 2 != 0))

# print("Cortocircuito con operador and")
# x = 3 + 5
# y = 0
# print(x < 2 and (x / y) > 2)
# print(x > 0 and (x / y) > 0)

print("Cortocircuito con operador or")
x = 1
y = 0
print(x > 0 or (x / y) > 0)
# print(x > 2 or (x / y) > 2)
