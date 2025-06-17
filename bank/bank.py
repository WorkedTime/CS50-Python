resp = input('Greeting: ')
resp = resp.strip().lower()

if resp.startswith('hello'):
    print('$0')

elif resp.startswith(('hey', 'how')):
    print('$20')

elif resp.startswith(('what', "what's")):
    print('$100')

else:
    print('$0')
