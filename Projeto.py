import random
import time

def input(*args, **kwargs):
    texto = " ".join(map(str, args))

    for letra in texto:
        __builtins__.print(letra, end="", flush=True)
        time.sleep(0.05)
    
    return __builtins__.input()

def print(*args, **kwargs):

    texto = " ".join(map(str, args))

    if texto.startswith("-") or texto.startswith(f"-"):
        __builtins__.print(texto, **kwargs)
        return

    end = kwargs.get("end", "\n")

    for letra in texto:
        __builtins__.print(letra, end="", flush=True)
        time.sleep(0.05)

    __builtins__.print(end=end)

print("oi pessoal, eu sou o dollynho")
dolly = input("seu amiguinho, vamos cantar? ")


