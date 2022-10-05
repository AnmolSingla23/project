from tkinter import *

def click(event):   #WE NEED TO CREATE CLICK EVENT TO MAKE BUTTONS WORK.
    global scvalue
    text = event.widget.cget('text')  #TO TAKE OUT TEXTS FROM WIDGET
    print(text)
    if text == "=":               #EQULS(BUTTON)
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())   #EVALUATES THE STRING AND GETS RESULT

            except Exception as e:
                print(e)
                value = 'ERROR'

        scvalue.set(value)
        screen.update()

    elif text == 'c':      #WORKS AT CL BUTTON(CLEAR)
        scvalue.set("")   #TO CLEAR THE SCREEN.EMPTY SET
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)  #ADD TEXT IN SCVALUE AND PRINT IT IN WIDGET
        screen.update()                 #UPDATES SCREEN.

root = Tk()
root.geometry('600x700')      #to set the size of thw window.
root.title("Calculator")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue,font='lucida 40 bold')   #to create window to enter var
screen.pack(fill=X, ipadx=8, pady =10 ,padx =10)    #pad gives pading aroud the entry window

#CREATE FRAMES AND EACH FRAME HAS 4 BUTTONS
f = Frame(root, bg='black')
b = Button(f, text='9', padx = 28, pady=16, font='lucida 25 bold') #CREATING BUTTON.WITH DIM
b.bind("<Button-1>", click)  # BIND MAKES CLICK WORKS
b.pack(side=LEFT, padx=18, pady=5)   #SIDE IS USED TO ARRANGE BUTTONS IN A ROW IN LEFT ORDER

b = Button(f, text='8', padx = 28, pady=16, font='lucida 25 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)  #SIDE IS USED TO ARRANGE BUTTONS IN A ROW IN LEFT ORDER

b = Button(f, text='7', padx = 28, pady=16, font='lucida 25 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)  #SIDE IS USED TO ARRANGE BUTTONS IN A ROW IN LEFT ORDER

b = Button(f, text='+', padx = 28, pady=16, font='lucida 25 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)  #SIDE IS USED TO ARRANGE BUTTONS IN A ROW IN LEFT ORDER
f.pack()       #PACK EACH FRAME

f = Frame(root, bg='black')
b = Button(f, text='6', padx = 28, pady=16, font='lucida 25 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f, text='5', padx = 28, pady=16, font='lucida 25 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f, text='4', padx = 28, pady=16, font='lucida 25 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
b = Button(f, text='-', padx = 22, pady=4, font='lucida 35 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

f.pack()

f = Frame(root, bg='black')
b = Button(f, text='3', padx = 28, pady=16, font='lucida 25 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f, text='2', padx = 28, pady=16, font='lucida 25 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f, text='1', padx = 28, pady=16, font='lucida 25 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f, text='*', padx = 28, pady=16, font='lucida 25 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=21.2, pady=5)
f.pack()

f = Frame(root, bg='black')
b = Button(f, text='0', padx = 28, pady=16, font='lucida 25 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f, text='00', padx = 20, pady=16, font='lucida 25 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f, text='.', padx = 28, pady=16, font='lucida 25 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f, text='%', padx = 26, pady=12, font='lucida 25 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
f.pack()

f = Frame(root, bg='black')
b = Button(f, text='c', padx = 28, pady=16, font='lucida 25 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=25, pady=5)

b = Button(f, text='/', padx = 34, pady=16, font='lucida 25 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=17, pady=5)

b = Button(f, text='', padx = 28, pady=16, font='lucida 25 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

b = Button(f, text='=',bg ='green', padx = 28, pady=16, font='lucida 25 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
f.pack()

root.mainloop()
