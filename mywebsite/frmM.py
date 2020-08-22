from tkinter import *
from tkinter import Menu

root = Tk()
root.title("Personal Development System")
root.geometry('700x600')

main_frame = Frame(root)
main_frame.pack(pady=20)

playlist_box = Listbox(main_frame, bg="white", fg="green", width=60, selectbackground="green", selectforeground='black')
playlist_box.grid(row=0, column=0)
L1 = Label(main_frame, text='Input Nama :')
L1.grid(row=1, column=0)
inpu_text1 = Entry(main_frame, bd=5)
inpu_text1.grid(row=1, column=1)



root.mainloop()