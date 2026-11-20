def calcular_media(notas: list[float]) -> float:
    total = sum(notas)
    quantidade = len(notas)
    media = total / quantidade

    return media


def main():
    notas = [8.5, 7.0, 9.5]

    resultado = calcular_media(notas)

    print(f"Notas: {notas}")
    print(f"Média: {resultado:.2f}")

    if resultado >= 7:
        print("Aprovado!")
    else:
        print("Reprovado!")


if __name__ == "__main__":
    main()
