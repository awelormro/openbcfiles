# Cosas
print("Dame tu peso en kg:")

peso = float(input())

print("Dame tu altura en m:")
altura = float(input())
imc=str(round(peso/altura, 2))
print("Tu imc es de " + imc)
