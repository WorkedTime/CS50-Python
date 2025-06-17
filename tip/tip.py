def main():
    dollar = input('Quanto custou a refeição? ')
    porcentagem = input('Qual a porcentagem de gorjeta você gostaria de deixar? ')

    valor = dollars_to_float(dollar)
    taxa = percent_to_float(porcentagem)

    gorjeta = valor * taxa
    print(f"O valor da gorjeta é de: ${gorjeta:.2f}")


def dollars_to_float(d):
    return float(d.replace('$', '').strip())


def percent_to_float(p):
    return float(p.replace('%', '').strip()) / 100


main()
