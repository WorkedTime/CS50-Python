def main():
    valor_guardado= 50
    moedas_aceitas = [25, 10, 5]

    while valor_guardado > 0:
        print(f'Amount Due: {valor_guardado}')
        moeda = int(input('Insert Coin (5, 10 or 25): '))
        
        if moeda in moedas_aceitas:
            valor_guardado -= moeda
            
    alteração = abs(valor_guardado)
    print(f'Change Owed: {alteração}')

if __name__ == "__main__":
    main()
