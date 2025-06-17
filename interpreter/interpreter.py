entrada = input("Expression ").strip()
xs, y, zs = entrada.split()

x = int(xs)
z = int(zs)

match y:
    case '+':
        resultado = x + z
    case '-':
        resultado = x - z
    case '*':
        resultado = x * z
    case '/':
        resultado = x / z

print(f"{resultado:.1f}")
