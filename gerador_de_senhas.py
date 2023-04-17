from random import randint

def gerar_senha():
    senha = []

    for _ in range(21):
        for caractere in chr(randint(33, 126)):
            senha.append(caractere)

    return ''.join(senha)

def main():
    senha = gerar_senha()
    print(senha)

if __name__ == '__main__':
    main()
