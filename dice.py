import random
from tkinter import *
from tkinter import ttk

dados = []
cant = int(input("How many dices do you wanna roll:?"))
root = Tk()
root.configure(bg="red")
root.title("Roll the dices")
ttk.Button(root, text='Exit', command=quit).pack(side=BOTTOM)
canvas = Canvas(root, width=650, height=650)
canvas.pack()
img1 = PhotoImage(file="dado1.png")
img2 = PhotoImage(file="dado2.png")
img3 = PhotoImage(file="dado3.png")
img4 = PhotoImage(file="dado4.png")
img5 = PhotoImage(file="dado5.png")
img6 = PhotoImage(file="dado6.png")


def tirar():
    i = 0
    if cant > 12:
        print("You can't roll that many...(max 12)")
    else:
        while i < cant:
            dados.append(random.randint(1, 6))
            i += 1
        print(dados)



def ima():
    i = 0
    while i < cant:
        x = random.randint(20, 530)
        y = random.randint(20, 530)

        if dados[i] == 1:
            canvas.create_image(x, y, anchor=NW, image=img1)

        if dados[i] == 2:
            canvas.create_image(x, y, anchor=NW, image=img2)

        if dados[i] == 3:
            canvas.create_image(x, y, anchor=NW, image=img3)

        if dados[i] == 4:
            canvas.create_image(x, y, anchor=NW, image=img4)

        if dados[i] == 5:
            canvas.create_image(x, y, anchor=NW, image=img5)

        if dados[i] == 6:
            canvas.create_image(x, y, anchor=NW, image=img6)

        i += 1


print(tirar())

print(ima())


mainloop()









