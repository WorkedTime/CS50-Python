def main():
    items = {}

    try:
        while True:
            item = input().strip().lower()
            if item:
                items[item] = items.get(item, 0) + 1

    except EOFError:
        print()

    for item in sorted(items):
        print(f'{items[item]} {item.upper()}')

if __name__ == '__main__':
    main()
