import math

# Solicita os coeficientes ao usuário
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Calcula o discriminante
delta = b ** 2 - 4 * a * c

# Verifica se existem raízes reais
if delta >= 0:
    # Calcula as raízes
    x1 = (-b + math.sqrt(delta)) // (2 * a)
    x2 = (-b - math.sqrt(delta)) // (2 * a)

    # Imprime as raízes
    print("As raízes da equação são:")
    print("x1 =", int(x1))
    print("x2 =", int(x2))
else:
    print("A equação não possui raízes reais.")
