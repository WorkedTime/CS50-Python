def main():
    valor_guardado= 50
    moedas_aceitas = [25, 10, 5]

    while valor_guardado > 0:
        print(f"Valor devido: {valor_guardado} centavos")
        moeda = int(input("Insira uma moeda (5, 10 ou 25 centavos): "))
        
        if moeda in moedas_aceitas:
            valor_guardado -= moeda
        else:
            print("Moeda não aceita.")

    alteração = abs(valor_guardado)
    print(f"Troco: {alteração} centavos")

if __name__ == "__main__":
    main()
