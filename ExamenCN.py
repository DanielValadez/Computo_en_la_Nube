import random
import string

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def siguiente_primo(n):
    primo_siguiente = n + 1
    while True:
        if es_primo(primo_siguiente):
            return primo_siguiente
        primo_siguiente += 1

def valor_medio(num1, num2, num3):
    suma = num1 + num2 + num3
    promedio = suma / 3
    return promedio

def gen_contrasena(n):
  contrasena = ""
  for i in range(1,n):
    contrasena += chr(random.randrange(33,126,1))
  return contrasena

def calcular_hipotenusa(lado1, lado2):
    hipotenusa = (lado1**2 + lado2**2)**0.5
    return hipotenusa