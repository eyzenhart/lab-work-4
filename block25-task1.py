from random import choice


def generate_password(m):
    ABC = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789'
    a = ''
    for i in range(m):
        symbol = choice(ABC)
        if symbol not in a:
            a += symbol
    return a


def main(n, m):
    passwords = []
    h = ''
    for i in range(n):
        h = generate_password(m)
        if h not in passwords:
            passwords.append(h)
    return passwords


print('Случайный пароль из 7 символов:', generate_password(7))
print('10 случайных паролей длиной 15 символов:')
print(*main(10, 15), sep='\n')
