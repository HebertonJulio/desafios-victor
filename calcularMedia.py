print("\nCalculadora de média escolar")


# SetVars
N1 = float(input("Informe a primeira nota: "))
N2 = float(input("Informe a segunda nota: "))
mediaAprovacao = 5.75
media = (N1 + N2) / 2


if media >= mediaAprovacao:
    print(f"\nA media do aluno é: {media:.2f}")
    print("Aluno esta aprovado.")
else:
    print(f"\nA media do aluno é: {media:.2f}")
    print("Aluno reprovado.")

