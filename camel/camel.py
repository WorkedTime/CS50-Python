def camel_to_snake(n):

    snake = ''
    for c in n:
        if c.isupper():
            snake += '_' + c.lower()
        else:
            snake += c

    return snake

def main():

    camel_case = input('camelCase: ')
    snake_case = camel_to_snake(camel_case)
    print('snake_case: ', snake_case)

if __name__ == "__main__":
    main()
