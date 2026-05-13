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
dolly = input("seu amiguinho, vamos cantar? Sim / Não: ").lower()
print()
if dolly == "sim":
    print(f'''DOLLY, DOLLY GUARANÁ, DOLLY, O MELHOR!
DOLLY GUARANÁ, O SABOR BRASILEIRO
DOLLY, DOLLY GUARANÁ, DOLLY, O MELHOR!
DOLLY GUARANÁ, DOLLY GUARANÁ''')
{time.sleep(2)}
if dolly == "sim":
    print('''DOLLY GUARANÁ, DOLLY GUARANÁ
DOLLY, DOLLY, DOLLY, DOLLY
DOOOOOOOLLY, DOLLY!''')