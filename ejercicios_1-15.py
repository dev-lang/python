'''
OK1. Crear un programa que muestre por pantalla la cadena de texto “¡Hola Mundo!”

OK2. Crear un programa que almacene en una variable la cadena de texto “¡Hola Mundo!” y luego la muestre por pantalla.

OK3. Crear un programa que pida al usuario su nombre y su edad y luego muestre por pantalla los siguientes mensajes en renglones distintos:

> Hola {nombre}
Tu edad es {edad} años

OK4. Crear un programa que pida al usuario su nombre y muestre por pantalla cuántas letras tiene.

OK5. Crear un programa que realice la siguiente operación aritmética (3*8/2)2 y muestre por pantalla el resultado.

OK6. Crear un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n.

OK7. Crear un programa que pida al usuario el monto a invertir y calcular cuánto dinero tendrá en su cuenta al cabo de 6 meses si el interés mensual es de 5%. Mostrar el resultado por pantalla.

OK8. Crear un programa que pida al usuario su edad y muestre por pantalla si es mayor de edad o no.

OK9. Crear un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

OK10. Crear un programa que pida al usuario dos números y muestre por pantalla el cociente de la división entre ellos siempre que el segundo número sea distinto de 0.

OK11. Crear un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

OK12. Crear un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

OK13. Crear una lista con 6 elementos, luego recorrerla e imprimir elemento a elemento en renglones distintos.

OK14. Crear un programa que recorra un diccionario previamente creado y muestre por pantalla:

> clave → valor

OK15. Crear un programa que imprima por pantalla todo lo que el usuario ingresa hasta que ingresa la palabra “salir”.
'''

# 1 2 3 y 4

''' llamar en caso de querer comprobar registro /// DEPRECADO ///
def Debug:
    print(nombre)
    print(nombre2)
    print(edad) '''

oppcinco = (3*8/2)*2

# workarounds de none
numeroint = None


def Operacion(): # EJERCICIO 5
    print(mensaje.ej, "5")
    print(mensaje.separadors)
    print("La operación da", oppcinco)

def resuelto():
    print(mensaje.separadors)
    print(mensaje.resuelto)
    print(mensaje.separador)
    Reset()

def noresuelto():
    print(mensaje.separadors)
    print(mensaje.noresuelto)
    print(mensaje.separador)
    Reset()

class col: #sin module
    R = '\033[31m'
    G = '\033[32m'

def Reset():
    workaround = '\033[m' #RESET COLORES. lo mismo que cuando usaba colorama y termcolor en el otro pj
    print(workaround)

class mensaje:
    primero = "Hola mundo"
    separador = "======================================"
    separadorc = "--------------------"
    separadors = "--------------------------------------"
    reqname = "Ingresa tu nombre:"
    reqage = "-Tu edad:"
    solicitud = "Por favor ingresa tu nombre :)"
    solicitud2 = "Ahora ingresa tu edad!"
    repeticion = "Vuelve a ingresar tu nombre. Por favor"
    repeticion2 = "Ingresa nuevamente tu nombre:"
    ej = "Ejercicio número:"
    enteropos = 'Ingresa un numero ENTERO positivo'
    enteropos2 = "-numero entero positivo:"
    enteroin = "Ingresa un numero ENTERO:"
    resuelto = (col.G + "Ejercicio resuelto exitosamente!")
    noresuelto = (col.R + "Ejercicio NO resuelto o en proceso")
    ganancia = "Su ganancia total es de:"
    edadmayor = "Felicidades! Eres mayor de edad"
    edadmenor = ":( Aun no eres mayor de edad"
    loginok = "Usuario y Contraseña correctas"
    logusrok = "Usuario Correcto"
    logusrf = "Usuario Incorrecto"
    loginunpy = "Usuario Incorrecto, Contraseña correcta"
    loginuypf = "Usuario Correcto, Contraseña incorrecta"
    gword = "Ingresa una palabra:"
    notan = "Debe ser un numero!"
    firstn = "Ingrese el primer numero:"
    secndn = "Ingrese el segundo numero:"

class error:
    nofloat = 'no se aceptan flotantes.'
    notanumber = "NO es un numero."
    onlyposint = "NO es un numero válido\n(No se toman ni string, ni flotantes ni negativos"
    pwdf = "Contraseña incorrecta"
    loginf = "Usuario o contraseña incorrecta"


print(mensaje.ej, "1, 2, 3 y 4")
print(mensaje.primero)
print(mensaje.separador)
print(mensaje.solicitud)
print(mensaje.separadors)
nombre = input(mensaje.reqname)
print(mensaje.solicitud2)
while True:
    edad = input(mensaje.reqage)
    #   check si es numero o string:
    try:
        val = int(edad)
        # falta workaround para positivo que NO destruya el programa sino que loopee hasta ingresar
        # assert(edad > 0), 'no se aceptan negativos' 
        break
    except ValueError:
        try:
            float(edad)
            print(error.nofloat)
        except ValueError:
            print(error.notanumber)
print ("Hola", nombre, "!\nTu edad es de", edad, "años")
print(mensaje.separador)
print(mensaje.repeticion)
nombre2 = input(mensaje.repeticion2)
print(mensaje.separadors)
caracteres = len(nombre)
print ("Tu nombre es:", nombre2, "y tiene", caracteres, "caracteres")
print(mensaje.separador)
resuelto()

# EJERCICIO 5
Operacion()

resuelto()
Reset()

# EJERCICIO 6
print(mensaje.ej, "6")
print(mensaje.separadors)
while True:
    numeroint = input(mensaje.enteropos2)
    try:
        num = int(numeroint)
        if num <= 0:
            raise ValueError # CUALQUIER COSA que NO sea int es rechazada. funciona mejor que un try float porque abarca todo.
        break # rompe programa ver
    # SOLUCIONADO. Ya no da exception ni genera un loop repetitivo
    except ValueError: # workaround strings
        print(error.onlyposint)
# falta workaround para evitar strings, float e int negativos
''' LISTO '''
''' VER SI REUTILIZAR EN WHILE ANTERIOR O SI CONSERVAR AMBOS '''
# falta completar ejercicio
# muestre en pantalla la suma de todos los enteros desde 1 hasta n.
enteros6 = int(numeroint)
#print(enteros6) # check registro
#print(type(enteros6))
for sumaent in range(1, enteros6):
    print(sumaent)
resuelto()

# EJERCICIO 7

print(mensaje.ej, "7")
print(mensaje.separadors)

# Crear un programa que pida al usuario el monto a invertir
# y calcular cuánto dinero tendrá en su cuenta al cabo de 6 meses 
# si el interés mensual es de 5%. Mostrar el resultado por pantalla.

'''
definir una funcion no es eficaz
definir una class parece dar problemas con la variable. probar definir afuera, sino eliminar class
'''
#valor = ""

#class Interes():

# hay dos formas. una es multiplicar por ejemplo 10 por 0.5 para sacar el el 50% o 0.05% para el 5%
# aunque la correcta deberia ser (porcentaje * valor) / 100

# valor = 1 #workaround para valor. despues cambia
''' intmens = 0.05 '''
dias = 30
meses = dias * 6
''' valorop = valor * intmens * meses '''

valor = input("""Ingrese el monto a invertir.\nTenga en cuenta que por defecto\n Se tendra en cuenta\nque 1 (un) mes tiene 30 dias\ny es un interes del 5%: """)
valorfinal = (5 * int(valor)) / 100 # workaround provisorio de int. probar float mas tarde. o primero ver si crashea al ingresar float con int
print(mensaje.ganancia, valorfinal)

resuelto()

# EJERCICIO 8
print(mensaje.ej, "8")
print(mensaje.separadors)

# Crear un programa que pida al usuario su edad y muestre por pantalla si es mayor de edad o no.

print("Bienvenido!", nombre, "\nPor favor vuelve a ingresar tu edad:")
while True:
    edad = input("EDAD:")
    try:
        nume = int(edad)
        if nume <= 0:
            raise ValueError # CUALQUIER COSA que NO sea int es rechazada. funciona mejor que un try float porque abarca todo.
        break # rompe programa ver
    # SOLUCIONADO. Ya no da exception ni genera un loop repetitivo
    except ValueError: # workaround strings
        print(error.onlyposint)
if nume >= int(18):
    print(mensaje.edadmayor)
elif nume <= int(17):
        print(mensaje.edadmenor)

resuelto()

# EJERCICIO 9
print(mensaje.ej, "9")
print(mensaje.separadors)

# 9. Crear un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

class LogIn():
    USUARIO = "admin"
    PASSWORD = "None1"

class min():
    user = str.lower(LogIn.USUARIO)
    password = str.lower(LogIn.PASSWORD)

class locks():
    user = str.upper(LogIn.USUARIO)
    password = str.upper(LogIn.PASSWORD)

usuario = input("Ingrese su usuario:")
password = input("Ingrese su contraseña:")

# DOM 6 SEP 2020 CODIGO VIEJO ELIMINADO
# LUNES 7 RESOLVER 9 CON UN FOR
#   anadido
''' # VERSION 1925 
if (usuario == LogIn.USUARIO or usuario == min.user) and (password == LogIn.PASSWORD or password == min.password):
	print(mensaje.loginok)
elif (usuario != LogIn.USUARIO or usuario != min.user) and (password == LogIn.PASSWORD or password == min.password):
    print(mensaje.loginunpy)
elif (usuario == LogIn.USUARIO or usuario == min.user) and (password != LogIn.PASSWORD or password != min.password):
    print(mensaje.loginuypf)
elif (usuario != LogIn.USUARIO or usuario != min.user) and (password != LogIn.PASSWORD or password != min.password):
    print(mensaje.loginf)
'''
# VERSION 1928
if (usuario == LogIn.USUARIO or usuario == min.user or usuario == locks.user) and (password == LogIn.PASSWORD or password == min.password or password == locks.password):
	print(mensaje.loginok)
elif (usuario != LogIn.USUARIO or usuario != min.user or usuario != locks.user) and (password == LogIn.PASSWORD or password == min.password  or password == locks.password):
    print(mensaje.loginunpy)
elif (usuario == LogIn.USUARIO or usuario == min.user or usuario == locks.user) and (password != LogIn.PASSWORD or password != min.password  or password != locks.password):
    print(mensaje.loginuypf)
elif (usuario != LogIn.USUARIO or usuario != min.user or usuario != locks.user) and (password != LogIn.PASSWORD or password != min.password  or password != locks.password):
    print(error.loginf)

resuelto()

# EJERCICIO 10
print(mensaje.ej, "10")
print(mensaje.separadors)

# 10. Crear un programa que pida al usuario dos números y muestre por pantalla 
# el cociente de la división entre ellos siempre que el segundo número sea distinto de 0.

''' while not x.isdigit():
    print(mensaje.notan)
    break '''


'''while not x.isdigit():
    print(mensaje.notan)
    break '''

while True:
    x = input(mensaje.firstn)
    try:
        #x.isdigit()
        x = float(x)
        break
    except ValueError:
        print(mensaje.notan)

while True:
    y = input(mensaje.secndn)
    try:
        #x.isdigit()
        y = float(y)
        break
    except ValueError:
        print(mensaje.notan)

# muestre por pantalla 
# el cociente de la división 
# entre ellos siempre que el segundo número sea distinto de 0.

while True:
    y != 0
    try:
        print(x % y)
        break
    except:
        print("Numeros:\nPrimero: ", str(x),  "Segundo: ", str(y)) #workaround str para que no lo muestre como float solamente
        break


''' PROBLEMA: FINALIZA sin loopear pidiendo valor correcto '''
#SOLUCIONADO 

#                               AHORA QUEDA LA PARTE 2:
#                               Y CORREGIR LOOP
#if (x != 0) and (y != 0):
#    print(float(x) % float(y))
#else:
#    PRINT("ERROR")
#    pass'''
#INCOMPLETO

noresuelto()

# EJERCICIO 11
print(mensaje.ej, "10")
print(mensaje.separadors)



# 11. Crear un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

enteroin = None
while True:
    enteroin = input(mensaje.enteroin)
    try:
        nument = int(enteroin)
        break
    except ValueError:
        try:
            float(enteroin)
            print(error.nofloat)
        except ValueError:
            print(error.notanumber)

''' USAR MODULO % '''

if int(enteroin) % 2 == 0:
    print("PAR")
elif int(enteroin) % 2 != 0:
        print("IMPAR")

resuelto()

# 12. Crear un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

gword = input(mensaje.gword)
numdatag = [] # una lista vacia para almacenar lo del for
''' CODIGO DEPRECADO
for gwordc in range(0, 10):
    gwordc + 1 '''

for numdatags in range(0, 10):
    numdatags + 1
    numdatag.append(gword)

for contargw, listagw in enumerate(numdatag):
    # print(contargw, "- " "palabra:", gword, "\n", mensaje.separadorc) 
    # ERROR con el separadorc UN ESPACIO DE MAS
    print(contargw, "- " "palabra:", gword)
    print(mensaje.separadorc)

resuelto()

#13. Crear una lista con 6 elementos, luego recorrerla e imprimir elemento a elemento en renglones distintos.

print(r"""
       __
      /
   .-/-.
   |'-'|
   |   |
   |   |   .-'''"-.
   \___/  /' .  '. \   \|/\//
         (`-..:...-')  |`""`|
          ;-......-;   |    |
           '------'    \____/
""")

anvorguesa = ['pan', 'carne', 'queso', 'tomate', 'mayonesa', 'lechuga'] # LISTA OK

for anvorcon, listanv in enumerate(anvorguesa):
    # print(anvorcon, "- " "Ingrediente:", anvorguesa)
    print(anvorcon, "- " "Ingrediente:", listanv)

resuelto()

# 
# 
# 14. Crear un programa que recorra un diccionario previamente creado y muestre por pantalla:
#

diccionario = {
    'Nombre': 'Melanie',
    'Apellido': 'Gold',
    'Edad': '30',
    'Profesion': 'Psicologa',
    'Universidad': 'UBA',
}

for a, b in diccionario.items():
    print(a, "→", b)
    print("")

resuelto()

# 
# 
# 15. Crear un programa que imprima por pantalla todo lo que el usuario ingresa hasta que ingresa la palabra “salir”.
# 
#

memw = None

exitw = "Salir"
exitmin = str.lower(exitw)
exitlok = str.upper(exitw)

if memw != exitw or memw != exitmin or memw != exitlok:
    memw = input(gword)
    print(memw)
elif memw == exitw or memw == exitmin or memw == exitlok:
    pass

resuelto()
