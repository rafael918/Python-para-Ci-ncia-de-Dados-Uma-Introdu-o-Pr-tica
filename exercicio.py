# 1.Calculadora de Soma Simples

numero1 = 5
numero2 = 10

soma = numero1 + numero2

print(f"A soma de {numero1} e {numero2} é: {soma}")


# 2.Conversor de Medidas (Centímetros)

metros = 5

centimetros = metros * 100

print(f"{metros} metros equivalem a {centimetros} centímetros.")


# 3.Reajuste de Bolsa Auxílio

bolsa = 350

if bolsa < 400:
    novo_valor = bolsa * 1.15
else:
    novo_valor = bolsa * 1.10

print(f"O valor da bolsa após o reajuste é: R$ {novo_valor:.2f}")


# 4. Classificador de Triângulos

lado1 = 5
lado2 = 5
lado3 = 5

if lado1 == lado2 and lado2 == lado3:
    print("O triângulo é Equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é Isósceles.")
else:
    print("O triângulo é Escaleno.")