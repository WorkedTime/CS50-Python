import emoji

def main():

    texto = input('Digite um texto com códigos de emoji: ')
    texto_emojizado = emoji.emojize(texto, language='alias')
    print('Texto com emojis:', texto_emojizado)

if __name__ == '__main__':
    main()
