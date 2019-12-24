import tkinter

win=tkinter.Tk()
win.title("Writor")

def do_open():
    pass

def do_save():
    pass
entry_file=tkinter.Entry(win)
entry_file.pack()

btn_open=tkinter.Button(win,text='Open',command=do_open)
btn_save=tkinter.Button(win,text='Save',command=do_save)

btn_open.pack()
btn_save.pack()



text=tkinter.Text(win)
text.pack()

win.mainloop()
