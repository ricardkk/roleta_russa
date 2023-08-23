from random import randint
import emoji

print(emoji.emojize("Bem-vindo a roleta_russa.py :smiling_face_with_horns:"))

bala = randint(1,6)

for i in range(1,6+1):
    print(emoji.emojize(f"Disparando o número {i}... :water_pistol:"))
    input("Aperte enter para puxar o gatilho! ")
    if i != bala:
        print("Se safou... por enquanto...")
        print("-"*30)
    elif i == bala:
        print(emoji.emojize("BOOM! :collision: :skull:"))
        break
        
    