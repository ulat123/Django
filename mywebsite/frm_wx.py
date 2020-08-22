# # Import modul wxPython
# import wx

# # Buat Objek aplikasi

# app = wx.App()

# # Buat frame
# frm = wx.Frame(None, title="Hello buddy")


# # Tampilkan ke layar
# frm.Show()

# #Mulai terus tampilkan
# app.MainLoop()

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pygame
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk


root = Tk()
root.title("MP3 Player by OwnSelf")
root.geometry("450x450")

# Initialize Pygame
pygame.mixer.init()

# Create function to deal with time
def play_time():
    if stopped:
        return

    # Get current time
    current_time = pygame.mixer.music.get_pos() / 1000
    # converter time
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))
    # Reconstruct song with directory structure
    song = playlist_box.get(ACTIVE)
    song = f'C:/DEV/Tutorial Django/mywebsite/audio/{song}.mp3'
    # Find current Song length
    song_mut = MP3(song)
    global song_length
    song_length = song_mut.info.length
    # Convert to time format
    converted_song_length = time.strftime('%M:%S',  time.gmtime(song_length))
    # my_label.config(text=converted_song_length)
    # Set slider to length to song length
    # song_slider.config(to=song_length)
    # my_label.config(text=song_slider.get())
    
    # Check to see if song is over
    if int(song_slider.get()) == int(song_length):
        forward()

    elif paused:
    #   Check too see if paused, if so - pass
        pass
    else:
        #  Move slider a long1 second at a time
        next_time = int(song_slider.get()) + 1
        # output new time value to slider, and to length of song
        song_slider.config(to=song_length, value=next_time)
        # converter time
        converted_current_time = time.strftime('%M:%S', time.gmtime(int(song_slider.get())))
        # output
        status_bar.config(text=f'Waktu Berjalan  {converted_current_time} dari {converted_song_length}'  )
    
    # Add current time to status bar
    if current_time > 0:
        status_bar.config(text=f'Waktu Berjalan  {converted_current_time} dari {converted_song_length}'  )
    #  Create Loop to check the time every second
    status_bar.after(1000, play_time)
    



# Create Function to add One song to playlist
def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 files", "*.mp3"), ) )
    # my_label.config(text=song)
    # Strip out directory structure and .mp3 from song title
    song = song.replace("C:/DEV/Tutorial Django/mywebsite/audio/", "")
    song = song.replace(".mp3", "")
    playlist_box.insert(END, song)

# Create Function to add many songs to playlist
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 files", "*.mp3"), ) )
    # Loop thru song list and replace directory structure and mpe3 from song name
    for song in songs:
        # my_label.config(text=song)
        # Strip out directory structure and .mp3 from song title
        song = song.replace("C:/DEV/Tutorial Django/mywebsite/audio/", "")
        song = song.replace(".mp3", "")
        #  Add to End of playlist
        playlist_box.insert(END, song)


# Create function delete one song
def delete_song():
    # Delete Hilighted song from playlist
    playlist_box.delete(ANCHOR)
# Create function delete All song
def delete_all_song():
    # Delete all songs
    playlist_box.delete(0, END)

# Create Play function
def play():
    # Set stop to false since a song is now play
    global stopped
    stopped = False
    # Reconstruct song with directory structure
    song = playlist_box.get(ACTIVE)
    song = f'C:/DEV/Tutorial Django/mywebsite/audio/{song}.mp3'
    #  Load song with pygame mixer
    pygame.mixer.music.load(song)
    #  Play song with pygame mixer
    pygame.mixer.music.play(loops=0)
    # Ini hanya tambahan untuk tampilkan judul lagu di label
    song = song.replace("C:/DEV/Tutorial Django/mywebsite/audio/", "")
    song = song.replace(".mp3", "")
    my_label.config(text=song) 

    play_time()

# Create stopped variable
global stopped
stopped = False
# Create Stop Function
def stop():
    # Stop the song
    pygame.mixer.music.stop()
    # Clear Playlist Bar
    playlist_box.selection_clear(ACTIVE) 
    my_label.config(text="") 

    status_bar.config(text='')

    # Set our slider to zero
    song_slider.config(value=0)

    # Set Stop variable true
    global stopped
    stopped = TRUE


# Create pause variable
global paused
paused = False
# Create Pause Function
def pause(is_paused):
    # Pause the song
    global paused 
    paused = is_paused

    if paused:
        #Unpause
        pygame.mixer.music.unpause()
        paused = False
    else:
        #Puase
        pygame.mixer.music.pause()
        paused = True

# Create forward button function
def forward():
    # Reset slider position and status bar
    status_bar.config(text='')
    song_slider.config(value=0)
    # Get current song number
    forward_song = playlist_box.curselection()
    # print(forward_song)
    # my_label.config(text=forward_song)
    
    # Add on the current song number tuple
    forward_song = forward_song[0] + 1
    
    # Grab the song title from the playlist
    song = playlist_box.get(forward_song)
    
    # Add directory structure stuff to the song
    song = f'C:/DEV/Tutorial Django/mywebsite/audio/{song}.mp3'
    
    #  Load song with pygame mixer
    pygame.mixer.music.load(song)
    
    #  Play song with pygame mixer
    pygame.mixer.music.play(loops=0)

    # Clear active Bar in playlist box
    playlist_box.selection_clear(0, END)

    # Move active bar to next song
    playlist_box.activate(forward_song)

    # Set active bar to next song
    playlist_box.selection_set(forward_song, last=None)

    # Ini hanya tambahan untuk tampilkan judul lagu di label
    song = song.replace("C:/DEV/Tutorial Django/mywebsite/audio/", "")
    song = song.replace(".mp3", "")
    my_label.config(text=song) 


# Create back button function
def back():
    # Reset slider position and status bar
    status_bar.config(text='')
    song_slider.config(value=0)
     # Get current song number
    forward_song = playlist_box.curselection()
    # print(forward_song)
    # my_label.config(text=forward_song)
    
    # Add on the current song number tuple
    forward_song = forward_song[0] - 1
    
    # Grab the song title from the playlist
    song = playlist_box.get(forward_song)
    
    # Add directory structure stuff to the song
    song = f'C:/DEV/Tutorial Django/mywebsite/audio/{song}.mp3'
    
    #  Load song with pygame mixer
    pygame.mixer.music.load(song)
    
    #  Play song with pygame mixer
    pygame.mixer.music.play(loops=0)

    # Clear active Bar in playlist box
    playlist_box.selection_clear(0, END)

    # Move active bar to next song
    playlist_box.activate(forward_song)

    # Set active bar to next song
    playlist_box.selection_set(forward_song, last=None)

    # Ini hanya tambahan untuk tampilkan judul lagu di label
    song = song.replace("C:/DEV/Tutorial Django/mywebsite/audio/", "")
    song = song.replace(".mp3", "")
    my_label.config(text=song) 

# Create volume function
def volume(x):
    # my_label.config(text=volume_slider.get())
    pygame.mixer.music.set_volume(volume_slider.get())

# Create slide function for song position
def slide(x):
     # Reconstruct song with directory structure
    song = playlist_box.get(ACTIVE)
    song = f'C:/DEV/Tutorial Django/mywebsite/audio/{song}.mp3'
    #  Load song with pygame mixer
    pygame.mixer.music.load(song)
    #  Play song with pygame mixer
    pygame.mixer.music.play(loops=0, start=song_slider.get())

# =======================================================================================================================================

# Create main frame
main_frame =  Frame(root)
main_frame.pack(pady=20)

# Create Playlist Box
playlist_box = Listbox(main_frame, bg="black", fg="green", width=60, selectbackground="green", selectforeground='black')
playlist_box.grid(row=0, column=0)

# Create volume slider frame
volume_frame = LabelFrame(main_frame, text="Volume")
volume_frame.grid(row=0, column=1, padx=10)

# Create Volume Slider
volume_slider  = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, length=125, value=1, command=volume )
volume_slider.pack(pady=10)

# Create song slider
song_slider = ttk.Scale(main_frame, from_=0, to=100, orient=HORIZONTAL, length=360, value=0, command=slide )
song_slider.grid(row=2, column=0, pady=20)

#crete Button Frame
control_frame = Frame(main_frame)
control_frame.grid(row=1, column=0, pady=20)

# Define Button Images for Controls
back_btn_img = PhotoImage(file='images/back50.png')
forward_btn_img = PhotoImage(file='images/forward50.png')
play_btn_img = PhotoImage(file='images/play50.png')
pause_btn_img = PhotoImage(file='images/pause50.png')
stop_btn_img = PhotoImage(file='images/stop50.png')

# Create Play/Stop etc Buttons
back_button = Button(control_frame, image=back_btn_img, borderwidth=0, command=back)
forward_button = Button(control_frame, image=forward_btn_img, borderwidth=0, command=forward )
play_button = Button(control_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(control_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(control_frame, image=stop_btn_img, borderwidth=0, command=stop)

#Posisi letak buttons
back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10) 
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

#Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Create Add song menu Dropdowns
add_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Tambah Lagu", menu=add_song_menu 
)
# Add one Song to playlist
add_song_menu.add_command(label="Tambah satu lagu ke Playlist", command=add_song)
# Add Many Songs to playlist
add_song_menu.add_command(label="Tambah banyak lagu ke Playlist", command=add_many_songs)

# Delete Song Menu
remove_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Hapus Lagu", menu=remove_song_menu)
remove_song_menu.add_command(label="Hapus satu lagu di playlist", command=delete_song)
remove_song_menu.add_command(label="Hapus semua lagu di playlist", command=delete_all_song)

# Create Status Bar 
status_bar = Label(root, text='nothing', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)



# Temporary Label
my_label = Label(root, text='')
my_label.pack(pady=20)


# def hello():
#    messagebox.showinfo("Say Hello", "Hello buddys")

# B1 = Button(root, text = "Say Hello", command = hello)


# B1.place(x = 10,y = 50)

root.mainloop()