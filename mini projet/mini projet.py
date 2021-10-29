from tkinter import *
from random import randint
import os

chemin = os.getcwd()
print(chemin)


def nom():
    global frame_setup, bouton_setup, label_setup
    ps = pseudo.get()
    frame_pseudo.destroy()

    bouton_setup = Button(fenetre, bg="#66CC66", text="JOUER", command=jeu)
    bouton_setup.config(width=10, height=10, font=('helvetica', 50))
    label_setup = Label(fenetre, text=("Bonjour " + ps + "! Nous allons jouer à chifoumi."), bg="#66CC66")
    label_setup.config(font=("helvetica", 40))

    label_setup.pack()
    bouton_setup.pack(pady=275)


def setup():
    global fenetre, pseudo, frame_pseudo

    frame_pseudo = LabelFrame(fenetre, text="Quel est votre nom?", bg="#66CC66", bd=0, font=("helvetica", 30))
    pseudo = Entry(frame_pseudo)

    pseudo.pack()
    bouton_pseudo.pack()
    frame_pseudo.pack(pady=200)


def reset():
    if scoreJ == 5 or scoreAd == 5:
        frame_choix_final.destroy()
        bouton_reset.destroy()
        frame_choix_final_Ad.destroy()
        frame_score.destroy()
        fin_jeu()
    else:
        frame_choix_final.destroy()
        bouton_reset.destroy()
        frame_choix_final_Ad.destroy()
        frame_score.destroy()
        jeu()


def fin_jeu():
    if scoreJ == 5:
        frame_win = Frame(fenetre, bg="#66CC66")
        label_win = Label(fenetre, bg="#66CC66", text=("vous avez gagné la partie! " + str(scoreJ) + "-" + str(scoreAd)))
        label_win.config(font=("helvetica", 50))
        label_win.pack(pady=300)
        frame_win.pack()
    else:
        frame_lost = Frame(fenetre, bg="#66CC66")
        label_lost = Label(fenetre, bg="#66CC66", text=("vous avez perdu la partie " + str(scoreJ) + "-" + str(scoreAd)))
        label_lost.config(font=("helvetica", 50))
        label_lost.pack(pady=300)
        frame_lost.pack()


def graph_choixAd():
    global imageAd, texteAd, frame_choix_final_Ad, image_choix_final_Ad, texte_choix_final_Ad
    if choixAd == pierre:
        imageAd = pierre_image
        texteAd = 'pierre'
    elif choixAd == feuille:
        imageAd = feuille_image
        texteAd = 'feuille'
    else:
        imageAd = ciseaux_image
        texteAd = 'ciseaux'

    frame_choix_final_Ad = Frame(fenetre, bg="#66CC66")
    image_choix_final_Ad = Label(frame_choix_final_Ad, image=imageAd, bg="#66CC66")
    texte_choix_final_Ad = Label(frame_choix_final_Ad, text="l'adversaire a choisi " + texteAd, bg="#66CC66",)
    texte_choix_final_Ad.config(font=("serif", 20))


def score():
    global scoreJ, scoreAd, frame_score, texte_score
    frame_score = Frame(fenetre, bg="#66CC66")

    if choix == pierre and choixAd == ciseaux:
        scoreJ += 1
        texte_score = Label(frame_score, bg="#66CC66", text="Vous gagnez 1 point! le score est " + str(scoreJ) + "-" + str(scoreAd))

    elif choix == ciseaux and choixAd == pierre:
        scoreAd += 1
        texte_score = Label(frame_score, bg="#66CC66", text="Vous avez perdu cette manche, l'adversaire gagne 1 point! le score est " + str(scoreJ) + "-" + str(scoreAd))

    elif choix == choixAd:
        texte_score = Label(frame_score, bg="#66CC66", text="egalité, personne de gagne de points! le score est toujours " + str(scoreJ) + "-" + str(scoreAd))

    elif choix > choixAd:
        scoreJ += 1
        texte_score = Label(frame_score, bg="#66CC66", text="Vous gagnez 1 point! le score est " + str(scoreJ) + "-" + str(scoreAd))

    else:
        scoreAd += 1
        texte_score = Label(frame_score, bg="#66CC66", text="Vous avez perdu cette manche, loader's gagne 1 point! le score est " + str(scoreJ) + "-" + str(scoreAd))


def choix_pierre():
    global frame_choix_final, bouton_reset, choix
    frame_choix.destroy()
    choix = pierre
    graph_choixAd()
    score()

    frame_choix_final = Frame(fenetre, bg="#66CC66")
    image_choix_final = Label(frame_choix_final, image=pierre_image, bg="#66CC66")
    texte_choix_final = Label(frame_choix_final, text="vous avez choisi pierre", bg="#66CC66", font=("serif", 20))
    bouton_reset = Button(fenetre, text="recommencer", command=reset, bg="#66CC66", font=('helvetica', 30))

    bouton_reset.pack(side='bottom')
    image_choix_final.pack()
    texte_choix_final.pack()
    image_choix_final_Ad.pack()
    texte_choix_final_Ad.pack()
    texte_score.pack()

    frame_choix_final_Ad.pack(side='right')
    frame_choix_final.pack(side='left')
    frame_score.pack()
    print('pierre')


def choix_feuille():
    global frame_choix_final, bouton_reset, choix
    frame_choix.destroy()
    choix = feuille
    graph_choixAd()
    score()

    frame_choix_final = Frame(fenetre, bg="#66CC66")
    image_choix_final = Label(frame_choix_final, image=feuille_image, bg="#66CC66")
    texte_choix_final = Label(frame_choix_final, text='vous avez choisi feuille', bg="#66CC66", font=("serif", 20))
    bouton_reset = Button(fenetre, text="recommencer", command=reset, bg="#66CC66", font=('helvetica', 30))

    bouton_reset.pack(side='bottom')
    image_choix_final.pack()
    texte_choix_final.pack()
    image_choix_final_Ad.pack()
    texte_choix_final_Ad.pack()
    texte_score.pack()

    frame_choix_final_Ad.pack(side='right')
    frame_choix_final.pack(side='left')
    frame_score.pack()
    print('feuille')


def choix_ciseaux():
    global frame_choix_final, bouton_reset, choix
    frame_choix.destroy()
    choix = ciseaux
    score()
    graph_choixAd()

    frame_choix_final = Frame(fenetre, bg="#66CC66")
    image_choix_final = Label(frame_choix_final, image=ciseaux_image, bg="#66CC66")
    texte_choix_final = Label(frame_choix_final, text='vous avez choisi ciseaux', bg="#66CC66", font=("serif", 20))
    bouton_reset = Button(fenetre, text="recommencer", command=reset, bg="#66CC66", font=('helvetica', 30))

    bouton_reset.pack(side='bottom')
    image_choix_final.pack()
    texte_choix_final.pack()
    texte_score.pack()
    image_choix_final_Ad.pack()
    texte_choix_final_Ad.pack()

    frame_choix_final_Ad.pack(side='right')
    frame_choix_final.pack(side='left')
    frame_score.pack()
    print('ciseaux')


def jeu():
    bouton_setup.destroy()
    label_setup.destroy()

    global pierre_image, feuille_image, ciseaux_image, frame_choix, choixAd

    choixAd = randint(1, 3)
    if choixAd == 1:
        print("l'adversaire a choisi pierre")
        choixAd = pierre
    elif choixAd == 2:
        print("l'advesaire a choisi feuille")
        choixAd = feuille
    else:
        print("l'adversaire a choisi ciseaux")
        choixAd = ciseaux

    pierre_image = PhotoImage(file=chemin + "\pierre.png")
    feuille_image = PhotoImage(file=chemin + "\papier.png")
    ciseaux_image = PhotoImage(file=chemin + "\ciseaux.png")

    frame_choix = Frame(fenetre)
    frame_choix.config(bg='#66CC66')
    frame_choix.pack()

    texte_choix = Label(frame_choix, bg='#66CC66', text='faites votre choix', font=('Helvetica', 20))

    bouton_choix1 = Button(frame_choix, image=pierre_image, command=choix_pierre)
    bouton_choix1.config(bg="#66CC66")

    bouton_choix2 = Button(frame_choix, image=feuille_image, command=choix_feuille)
    bouton_choix2.config(bg="#66CC66")

    bouton_choix3 = Button(frame_choix, image=ciseaux_image, command=choix_ciseaux)
    bouton_choix3.config(bg="#66CC66")

    texte_choix.grid(column=1, row=0)
    bouton_choix1.grid(column=0, row=0, padx=50, pady=10)
    bouton_choix2.grid(column=1, row=1, ipadx=10)
    bouton_choix3.grid(column=2, row=0, padx=50)


pierre = 1
feuille = 2
ciseaux = 3
scoreAd = 0
scoreJ = 0

fenetre = Tk()
fenetre.config(bg="#66CC66")
fenetre.title("chifumi")
fenetre.iconbitmap("icon.ico")

frame_pseudo = LabelFrame(fenetre, text="Quel est votre nom?", bg="#66CC66", bd=0, font=("helvetica", 30))
pseudo = Entry(frame_pseudo)
bouton_pseudo = Button(frame_pseudo, text="Cliquez ici pour continuer", command=nom)

pseudo.pack(pady=10)
bouton_pseudo.pack(pady=15)
frame_pseudo.pack(pady=200)

fenetre.geometry("1290x770")
fenetre.minsize(1290, 770)
fenetre.maxsize(1290, 770)

fenetre.mainloop()
