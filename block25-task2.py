from random import choice


def generate_password(m):
    ABC = ['ABCDEFGHJKLMNPQRSTUVWXYZ', 'abcdefghijkmnpqrstuvwxyz', '23456789']
    ABC1 = [0, 1, 2]
    a = choice(ABC[0]) + choice(ABC[1]) + choice(ABC[2])
    for i in range(m-3):
        symbol = choice(ABC[choice(ABC1)])
        a += symbol
    return a


def main(n, m):
    passwords = []
    h = ''
    for i in range(n):
        h = generate_password(m)
        passwords.append(h)
    return passwords


print('Случайный пароль из 7 символов:', generate_password(7))
print('10 случайных паролей длиной 15 символов:')
print(*main(10, 15), sep='\n')
