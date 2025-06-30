import sys
import random
import pyfiglet

def main():

    args = sys.argv[1:]

    if len(args) not in [0, 2]:
        sys.exit('Uso: python figlet.py [-f | --font] nome_da_fonte')

    if len(args) == 2:
        option, font_name = args

        if option not in ['-f', '--font']:
            sys.exit('Erro: opção inválida. Use -f ou --font.')

        if font_name not in pyfiglet.FigletFont.getFonts():
            sys.exit('Erro: fonte inválida.')
        
        figlet = pyfiglet.Figlet(font=font_name)

    else:
        random_font = random.choice(pyfiglet.FigletFont.getFonts())
        figlet = pyfiglet.Figlet(font=random_font)

    user_input = input('Texto: ')
    print(figlet.renderText(user_input))

if __name__ == '__main__':
    main()
