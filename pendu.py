import os

COMMAND = "cls"

class Pendu:
    def __init__(self):
        self.word = ""
        self.number_draw = 0
        self.mot = []
        self.lettre = []
        self.affichage = []

    def afficher_mot(self):
        for i in range(len(self.word)):
            self.affichage.append("_")

    def get_index_word(self,letter):
        if self.word.count(letter) == 1:
            index_letter = self.word.index(letter)
            self.replace_underscore(index_letter,letter)
        else:
            plusieur_lettre = self.get_index_words(letter)
            print()
            print(plusieur_lettre)
            print()
            self.replace_plusieur_underscore(plusieur_lettre,letter)

    def get_index_words(self,letter):
        plusieur_lettres = []
        for i in range(len(self.word)):
            if self.word[i] == letter:
                plusieur_lettres.append(i)
        return plusieur_lettres

    def get_affichage(self):
        return " ".join(self.affichage)

    def get_lettres(self):
        return " ".join(self.lettre)

    def get_mots(self):
        return " ".join(self.mot)

    def replace_underscore(self,index_letter,letter):
        self.affichage.pop(index_letter)
        self.affichage.insert(index_letter,letter)

    def replace_plusieur_underscore(self,index_letters,letter):
        for i in index_letters:
            self.affichage.pop(i)
            self.affichage.insert(i,letter)

    def test_lettre(self):
        lettre_entre = input("Entrez votre lettre ")
        if not lettre_entre in self.lettre:
            if lettre_entre in self.word:
                print("Vous avez trouver la lettre :",lettre_entre)
                self.get_index_word(lettre_entre)
            else:
                print(lettre_entre,"n'est pas dans le mot")
                self.draw()
            self.lettre_dite(lettre_entre)
        else:
            print("La lettre :",lettre_entre,"a déja été dite !")
            self.test_lettre()

    def test_mot(self):
        mot_entre = input("Entrer le mot que vous souhaiter ")
        if not mot_entre in self.mot:
            if mot_entre == self.word:
                print("Vous avez trouver le bon mot :",self.word)
                exit()
            else:
                print(mot_entre,"n'est pas le bon mot !")
                self.draw()
            self.mot_dit(mot_entre)
        else:
            print("Le mot :",mot_entre,"a déja été dit !")
            self.test_mot()

    def mot_dit(self,mot_entre):
        self.mot.append(mot_entre)

    def lettre_dite(self,lettre_entre):
        self.lettre.append(lettre_entre)

    def draw(self):
        self.number_draw += 1
        if self.number_draw == 1:
            print("_|_")
        elif self.number_draw == 2:
            print(" |")
            print(" |")
            print("_|_")
        elif self.number_draw == 3:
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("_|_")
        elif self.number_draw == 4:
            print(" __")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("_|_")
        elif self.number_draw == 5:
            print(" ______")
            print(" |   |")
            print(" |")
            print(" |")
            print(" |")
            print("_|_")
        elif self.number_draw == 6:
            print(" ______")
            print(" |   |")
            print(" |   ()")
            print(" |")
            print(" |")
            print("_|_")
        elif self.number_draw == 7:
            print(" ______")
            print(" |   |")
            print(" |   O")
            print(" |   |")
            print(" |")
            print("_|_")
        elif self.number_draw == 8:
            print(" ______")
            print(" |   |")
            print(" |   O")
            print(" |  /|")
            print(" |")
            print("_|_")
        elif self.number_draw == 9:
            print(" ______")
            print(" |   |")
            print(" |   O")
            print(" |  /|\ ")
            print(" |")
            print("_|_")
        elif self.number_draw == 10:
            print(" ______")
            print(" |   |")
            print(" |   O")
            print(" |  /|\ ")
            print(" |  /")
            print("_|_")
        elif self.number_draw == 11:
            print(" ______")
            print(" |   |")
            print(" |   O")
            print(" |  /|\ ")
            print(" |  / \ ")
            print("_|_")
            print("Vous etes pendu !")
            print("Vous avez perdu !")
            exit()

        else:
            print(ValueError)

pendu = Pendu()
print("Bonjour, bienvenue dans le pendu")
reponse_mot = input("Veuillez entrer le mot ")
pendu.word = reponse_mot
pendu.afficher_mot()
os.system(COMMAND)
while True:
    print("1) Dire une lettre")
    print("2) Dire un mot")
    reponse_utilisateur = int(input("Que voulez vous faire ? "))
    print()
    if reponse_utilisateur == 1:
        pendu.test_lettre()
    elif reponse_utilisateur == 2:
        pendu.test_mot()
    else:
        print(ValueError)

    os.system(COMMAND)
    print()
    print("Les lettres deja dites sont :",pendu.get_lettres())
    print("Les mots deja dit sont :",pendu.get_mots())
    print()
    print(pendu.get_affichage())