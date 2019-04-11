import string
import random

class Encryption():
    """
        SEED: Senha para descriptografar
        ENCRYPTION: Input a frase / palavra que queira criptografar, retorna a frase / palavra
        criptografada
        DESCRYPTION: Input a frase / palavra que queira descriptografar, INPUT o seed para liberar o código,
        retorna a frase descriptografada
    """

    mensagem = ''
    nova = ''

    def __init__(self, seed):
        self.codigo = seed

    def encryption(self, message):
        self.message = str(message).split()
        self.alfa_correto = list(string.ascii_lowercase)
        self.alfa_random = random.sample(self.alfa_correto, len(self.alfa_correto))

        for i in message:
            if i == ' ':
                Encryption.mensagem = Encryption.mensagem + ' ' + random.choice(self.alfa_random)
            if i in self.alfa_random:
                Encryption.mensagem = Encryption.mensagem + i + random.choice(self.alfa_random)
        Encryption.mensagem = Encryption.mensagem[::-1]

        for i in Encryption.mensagem:
            if i == ' ':
                Encryption.nova += ' '
            for z, x in enumerate(self.alfa_correto):
                for c, v in enumerate(self.alfa_random):
                    if i == x:
                        if z == c:
                            Encryption.nova += v

        print(Encryption.nova)

    def decryption(self, message, seed):
        mensagem_final = ''
        mensagem_meio = ''
        self.message = message
        self.seed = seed
        if self.seed == self.codigo:
            for i in self.message:
                if i == ' ':
                    mensagem_final += ' '
                for z, x in enumerate(self.alfa_random):
                    for c, v in enumerate(self.alfa_correto):
                        if i == x:
                            if z == c:
                                mensagem_final += v

            mensagem_final = mensagem_final[::-1]

            for k, i in enumerate(mensagem_final):
                if k % 2 == 0:
                    mensagem_meio += i

            print(mensagem_meio)

        else:
            print('Atenção, código de decriptação errado')