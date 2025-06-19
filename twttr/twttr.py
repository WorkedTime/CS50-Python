def remove_vogais(texto):
    
    vogais = "aeiouAEIOU"
    resultado = ""

    for caractere in texto:
        if caractere not in vogais:
            resultado += caractere
    return resultado

def main():

    texto = input("Input: ")
    texto_sem_vogais = remove_vogais(texto)
    print('Output:', texto_sem_vogais)

if __name__ == "__main__":
    main()
