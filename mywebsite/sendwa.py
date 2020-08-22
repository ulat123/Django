from tkinter import *


root = Tk()
root.title("Covid-19 Today")
root.geometry("500x500")

data = StringVar()

def tampil():
   
    from matplotlib import pyplot as plt
    import numpy as np
    import matplotlib.patches as wow
    from covid import Covid

    covid = Covid()
   

    cases = []
    confirmed = []
    active = []
    deaths = []
    recovered = []
   

try:
    root.update()
    countries = data.get()
    country_names = countries.strip()
    country_names = country_names.replace(" ", ",")
    country_names = country_names.split(",")

    for x in country_names:
        cases.append(covid.get_status_by_country_name(x))
        root.update()

    for y in cases:
        confirmed.append(y["confirmed"])
        active.append(y["active"])
        deaths.append(y["deaths"])
        recovered.append(y["recovered"])
    
    confirmed_patch = mpatches.Patch(color='green', label='confirmed')
    recovered_patch = mpatches.Patch(color='red', label='recovered')
    active_patch = mpatches.Patch(color='blue', label='active')
    deaths_patch = mpatches.Patch(color='black', label='deaths')

    plt.legend(handles=[confirmed_patch, recovered_patch, active_patch, deaths_patch])
    for x in range(len(country_names)):
        plt.bar(country_names[x], confirmed[x], color='green')
        if recovered[x] > active[x]:
            plt.bar(country_names[x], recovered[x], color='red')
            plt.bar(country_names[x], active[x], color='blue')
        else:
            plt.bar(country_names[x], active[x], color='blue')
            plt.bar(country_names[x], recovered[x], color='red')
        plt.bar(country_names[x], deaths[x], color='black')
        
    plt.title('Current Covid Cases')
    plt.xlabel('Country Name')
    plt.ylabel('Cases(in millions)')
    plt.show()
except Exception as e:
        data.set("Enter correct details again")
        
Label(root, text="Masukan nama negara\nUntuk menampilkan Data Covid-19", font="Consolas 15 bold").pack()
Label(root, text="Masukan Nama Negara:").pack()
data = StringVar()
data.set("Untuk menampilkan beberapa negara, gunakan Koma(,) Sebagai pemisah.")
entry = Entry(root, textvariable=data, width=80).pack()
Button(root, text="Ambil Data", command=tampil).pack()
root.mainloop()

# text.tag_add("here", "1.0", "1.5")
# text.tag_add("start", "1.6", "1.11")
# text.tag_config("here", background="yellow", foreground="blue")
# text.tag_config("start", background="black", foreground="white")


# covid =Covid()
# cases=covid.get_status_by_country_name("china")
# for x in cases:
#     print(x,":", cases[x])


# text.insert(EXTENDED, x, ":", cases[x])
# text.pack()

