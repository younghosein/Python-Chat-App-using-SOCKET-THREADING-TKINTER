from tkinter import *
#paszamine sakhtim
board = Tk()
#taghire title
board.title("Person1")
#X,Y(size)barname
board.geometry("400x200")
#bara inke abaadesh tghir konn ya na
board.resizable(width=True,height=True)
#sakhte label:1=safhe ii ke label baiad tosh bashe 2=matn
#3=range paszaminash 4=range khodesh 5=goshe ghalebe label
#6=noee border
lbl = Label(board, text="Soton Salam Wha'sup?",
            bg="darkgray", fg="white", borderwidth=2,
            relief="ridge")
#bara add krdn label be safhe:2=koja bashe(Zelle) 
#1=aya zell eio bposhone?age are kodom?x->ofogh y->amood
lbl.pack(fill=X ,side=BOTTOM)
#Tabeii ke ro btn click shod ejra mishe
def h():
    #matni ke az vorodi grftimo mirize to 'dg'
    dg = txt.get()
    print(dg)
    #pak kardan textbox
    txt.delete(0,END) 
#sakhte button:3:tabeii ke bade click ejra mishe
btn = Button(board, text="Click me", command=h)
btn.pack(side=BOTTOM)
#sakhte textbox
txt = Entry(board)
txt.pack(side=BOTTOM)
#bra inke paszamine bemone
board.mainloop()
