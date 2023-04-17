from random import randint

def gerar_senha():
    senha = []; caracteres = []

    for indice in range(33, 127):
        caracteres.append(chr(indice))
    for _ in range(21):
        for caractere in caracteres[randint(0, len(caracteres)-1)]:
            senha.append(caractere)

    return ''.join(senha)

if __name__ == '__main__':
    senha = gerar_senha()
    print(senha)
