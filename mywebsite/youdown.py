
from tkinter import *
from pytube import YouTube

root= Tk()
root.geometry("400x500")
root.title("Ayo .. Download YOUTUBE")

def download():
    try:
        myVar.set("Downloading ...")
        root.update()
        YouTube(link.get()).streams.first().download()
        myVar.set("Video Berhasil di download")
    except Exception as e:
        myVar.set("Kesalahan Hakiki")
        root.update()
        link.set("Masukan Link yang bener cok!")

Label(root, text="Selamat datang di Youtube Downloader Aplikasi\nSemoga Kalian betah", font="Consolas 15 bold").pack()
myVar = StringVar()
myVar.set("Masukan Link disini")
Label(root, textvariable=myVar, width=40).pack(pady=10)
link = StringVar()
Entry(root, textvariable=link, width=40).pack(pady=10)
Button(root, text="Download Video", command=download).pack()

root.mainloop()