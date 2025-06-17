def convert(texto):
    return texto.strip().replace(':)', '🙂').replace(':(', '🙁')

def main():
    entrada = input('Digite o texto que deseja: ')
    convertido = convert(entrada)
    print(convertido)

main()
