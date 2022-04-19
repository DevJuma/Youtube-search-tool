from tkinter import *
import urllib
import urllib.request
import re

root = Tk()
root.title('YT_searcher')
root.geometry("240x120+500+200")


def button_command1():
    text = entry1.get()
    i = int(entry2.get()) - 1
    if (i < 0) or (i > 19):
        lb4 = Label(root, text="Number between 1 and 20")  # error message
        lb4.place(x=80, y=60)
    else:
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + text)
        vidid = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        linktovid = "https://www.youtube.com/watch?v=" + vidid[i]
        root.clipboard_clear()
        root.clipboard_append(linktovid)
        lb4 = Label(root, text=linktovid)
        lb4.place(x=80, y=60)
        entry1.delete(0, END)
        entry2.delete(0, END)
        return None


btn1 = Button(root, text="Search", fg='Purple', bg='Yellow', command=button_command1)
lb1 = Label(root, text='Keyword:')
lb2 = Label(root, text='Video no.:')
lb3 = Label(root, text='result:')
entry1 = Entry(root, width=20)
entry2 = Entry(root, width=2)

btn1.place(x=10, y=85)
lb1.place(x=10, y=10)
lb2.place(x=10, y=35)
lb3.place(x=10, y=60)
entry1.place(x=80, y=10)
entry2.place(x=80, y=35)


root.mainloop()
