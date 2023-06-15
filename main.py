from tkinter import *

root = Tk()
root.title("复制小工具")
root.geometry('401x400+300+300')
label2 = Label(root, text='输入文字')
label3 = Label(root, text='复制的内容')
label2.pack(side=TOP)
entry = Entry(root)
entry.pack(side=TOP)
label3.pack(side=TOP)
text = Listbox()
text.pack(side=TOP)


def copy():
    text.insert(1, entry.get())


button = Button(root, text="复制", command=copy)
button.pack(side=TOP)
root.mainloop()
