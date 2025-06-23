def main():

    while True:
        try:
            fracao = input('Fraction: ')
            x, y = fracao.split('/')

            x = int(x)
            y = int(y)

            # Valida os valores
            if y == 0 or x > y:
                raise ValueError

            percentagem = round((x / y) * 100)

            if percentagem <= 1:
                print('E')
            elif percentagem >= 99:
                print('F')
            else:
                print(f'{percentagem}%')
            break 

        except (ValueError, ZeroDivisionError):
            continue

if __name__ == '__main__':
    main()
