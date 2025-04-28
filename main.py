from tkinter import *

import tkintermapview

root = Tk()
root.title("MapBook_ow")
root.geometry("1024x768")

# RAMKI
ramka_lista_obiektów = Frame(root)
ramka_formularz = Frame(root)
ramka_szcegóły_obiektów = Frame(root)
ramka_mapa = Frame(root)

ramka_lista_obiektów.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szcegóły_obiektów.grid(row=1, column=0)
ramka_mapa.grid(row=2, column=0)


# RAMKA LISTA OBIEKTÓW

label_lista_obiektów = Label(ramka_lista_obiektów, text="LiStA ObIeKtÓw:")
label_lista_obiektów.grid(row=0, column=0, columnspan=3)
listbox_lista_obiektów = Listbox(ramka_lista_obiektów)
listbox_lista_obiektów.grid(row=1, column=0, columnspan=3)
button_pokaż_szczegóły = Button(ramka_lista_obiektów, text="Pokaż szczegóły")
button_pokaż_szczegóły.grid(row=2, column=0)
button_edytuj_obiekt = Button(ramka_lista_obiektów, text="Edytuj obiekt")
button_edytuj_obiekt.grid(row=2, column=1)
button_usuń_obiekt = Button(ramka_lista_obiektów, text="Usuń obiekt")
button_usuń_obiekt.grid(row=2, column=2)

# RAMKA FORMULARZ
label_formularz = Label(ramka_formularz, text="Formularz: ")
label_formularz.grid(row=0, column=0, columnspan=2)
label_name = Label(ramka_formularz, text="Imię:  ")
label_name.grid(row=1, column=0, sticky=W)
label_surname = Label(ramka_formularz, text="Nazwisko:   ")
label_surname.grid(row=2, column=0, sticky=W)
label_post = Label(ramka_formularz, text="Liczba postów:   ")
label_post.grid(row=3, column=0, sticky=W)
label_location = Label(ramka_formularz, text="Miejscowość: ")
label_location.grid(row=4, column=0, sticky=W)


entry_name = Entry(ramka_formularz)
entry_name.grid(row=1, column=1,)
entry_surname = Entry(ramka_formularz)
entry_surname.grid(row=2, column=1,)
entry_post = Entry(ramka_formularz)
entry_post.grid(row=3, column=1,)
entry_location = Entry(ramka_formularz)
entry_location.grid(row=4, column=1,)

button_dodaj_obiekt = Button(ramka_formularz, text="Dodaj obiekt")
button_dodaj_obiekt.grid(row=5, column=1, columnspan=2)

# RAMKA SZCZEGÓŁY OBIEKTU
label_szczegóły_obiektu = Label(ramka_szcegóły_obiektów, text="Szczegóły użytkownika:")
label_szczegóły_obiektu.grid(row=0, column=0, sticky=W)

label_name_szczegóły_obiektu = Label(ramka_szcegóły_obiektów, text="Imię:   ")
label_name_szczegóły_obiektu.grid(row=1, column=0,)

label_name_szczegóły_obiektu_wartość = Label(ramka_szcegóły_obiektów, text=".....   ")
label_name_szczegóły_obiektu_wartość.grid(row=1, column=1, )

label_surname_szczegóły_obiektu_ = Label(ramka_szcegóły_obiektów, text="Nazwisko:   ")
label_surname_szczegóły_obiektu_.grid(row=1, column=2,)

label_surname_szczegóły_obiektu_wartość = Label(ramka_szcegóły_obiektów, text=".....   ")
label_surname_szczegóły_obiektu_wartość.grid(row=1, column=3, )

label_post_szczegóły_obiektu_wartość = Label(ramka_szcegóły_obiektów, text="Liczba postów:   ")
label_post_szczegóły_obiektu_wartość.grid(row=1, column=4, )

label_post_szczegóły_obiektu_wartość = Label(ramka_szcegóły_obiektów, text=".....   ")
label_post_szczegóły_obiektu_wartość.grid(row=1, column=5, )

label_location_szczegóły_obiektu_wartość = Label(ramka_szcegóły_obiektów, text="Miejscowość:   ")
label_location_szczegóły_obiektu_wartość.grid(row=1, column=6, )

label_location_szczegóły_obiektu_wartość = Label(ramka_szcegóły_obiektów, text=".....   ")
label_location_szczegóły_obiektu_wartość.grid(row=1, column=7, )


# RAMKA MAPA
# map_vidget = tkintermapview.TkinterMapView(ramka_mapa, width=1024, height=400,)
# map_vidget.set_position(52.23,21)
# map_vidget.set_zoom(5)
# map_vidget.grid(row=0, column=0, columnspan=8)



root.mainloop()