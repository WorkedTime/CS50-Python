meses = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]

def main():
    while True:
        try:
            data = input('Date: ').strip()

            if ',' in data:
                nome_do_mes, dia_do_ano = data.split(' ', 1)
                dia, ano = dia_do_ano.replace(',', '').split()
                mes = meses.index(nome_do_mes) + 1
            else:
                mes, dia, ano = map(int, data.split('/'))

            if not (1 <= int(mes) <= 12 and 1 <= int(dia) <= 31):
                raise ValueError

            print(f'{int(ano):04}-{int(mes):02}-{int(dia):02}')
            break

        except (ValueError, IndexError):
            continue

if __name__ == '__main__':
    main()
