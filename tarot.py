import sys, os, json

NOM_MAX_TAILLE = 11
ERREUR = -1
TROP_LONG = -2
PAS_D_ERREUR = 0

NOUVEAU_FICHIER = 0
REMPLACER_FICHIER = 1

ENJEU = 25
PETITE = 1
GARDE = 2
GARDE_SANS = 4
GARDE_CONTRE = 6

CONTRATS = []
CONTRATS.append("Petite")
CONTRATS.append("Garde")
CONTRATS.append("Garde sans")
CONTRATS.append("Garde contre")

POIGNEES = []
POIGNEES.append("Pas de Poignee")
POIGNEES.append("Simple")
POIGNEES.append("Double")
POIGNEES.append("Triple")

PETIT_AU_BOUT = []
PETIT_AU_BOUT.append("Pas de petit au bout")
PETIT_AU_BOUT.append("Attaque")
PETIT_AU_BOUT.append("Defense")

FACTEUR_MULTIPLICATEUR = []
FACTEUR_MULTIPLICATEUR.append(1)
FACTEUR_MULTIPLICATEUR.append(2)
FACTEUR_MULTIPLICATEUR.append(4)
FACTEUR_MULTIPLICATEUR.append(6)

BILANS = []
BILANS.append("Reussie")
BILANS.append("Chutee")

V=sys.version_info[0]

def DemanderPhrase(phrase) :
    if V==2:
        return raw_input(phrase)
    else:
        return input(phrase)

# Demander chiffer
def DemanderChiffre(phrase) :
    try :
        if V==2:
            return int(raw_input(phrase))
        else:
            return int(input(phrase))
    except :
        return -1

# affiche sans retour ligne
def AfficherSRL(liste_de_phrases):
    for i in range(0, len(liste_de_phrases)):
        sys.stdout.write(str(liste_de_phrases[i]))

# affiche avec retour ligne
def AfficherARL(liste_de_phrases):
    for i in range(0, len(liste_de_phrases)):
        sys.stdout.write(str(liste_de_phrases[i]))
    print('')

# extraire des les donnees du fichier
def ExtraireDonneesDuFichier(NomFichier) :
    try :
        Fichier = open(NomFichier + '.json', 'r')
    except :
        # Si pas de fichier existant a ce nom, retourner un dictionnaire vide
        return {}
    Donnees = json.load(Fichier)
    Fichier.close
    return Donnees

# Mettre a jour le fichier
def MettreFichierAJour(NomFichier, Donnees, Action):
    if Action == REMPLACER_FICHIER :
        os.remove(NomFichier + '.json')
    Fichier = open(NomFichier + '.json', 'w')
    json.dump(Donnees, Fichier, indent=4)
    Fichier.close

# demander a l utilisteur de choisir une option parmi celles proposees
def DemanderChoixParmiSelection(Intitule, Liste):
    while 1:
        AfficherARL((Intitule))
        for i in range(0, len(Liste)) :
            AfficherSRL(("    ",i,":", Liste[i]))
        try :
            c = int(DemanderPhrase("    --> "))
        except :
            c = -1
        if c>=0 and c<len(Liste) :
            return c

# Afficher une ligne de separation. c est pour faire en sorte que l affichage des scores d une partie soit plus lisible
def AfficherLigneDeSeparation(NbJoueurs) :
    if NbJoueurs == 5:
        for i in range(0,97+14*5+2):
            AfficherSRL(('-'))
    else:
        for i in range(0,83+14*NbJoueurs+2):
            AfficherSRL(('-'))
    AfficherARL((""))

# Calculaer et Afficher tous les points d'une partie
def AfficherBilanPartie(Donnees) :

    AfficherARL((""))

    # ligne de separation
    NbJoueurs =  len(Donnees["Joueurs"])
    AfficherLigneDeSeparation(NbJoueurs)

    # ligne d'en tete
    AfficherSRL(('|%4s' %(' ')))
    AfficherSRL((' |%13s' %('Contrat')))
    AfficherSRL((' |%8s' %('Bilan')))
    AfficherSRL((' |%11s' %('De combien')))
    AfficherSRL((' |%12s' %('Preneur')))
    if NbJoueurs == 5 :
        AfficherSRL((' |%12s' %('Partenaire')))
    AfficherSRL((' |%8s' %('Poignee')))
    AfficherSRL((' |%14s' %('Petit au bout')))
    for i in range (0, NbJoueurs) :
        NomDuJoueur = Donnees["Joueurs"][i]
        AfficherSRL((' |%12s' %(NomDuJoueur)))
    AfficherARL((" |"))

    # ligne de separation
    AfficherLigneDeSeparation(NbJoueurs)

    # donnees
    NbTours = len(Donnees["Tours"])

    if NbTours > 0 :
        ScoreDeLaPartie = {}
        for i in range (0, NbJoueurs) :
            NomDuJoueur = Donnees["Joueurs"][i]
            ScoreDeLaPartie[NomDuJoueur] = 0

        for i in range (0, NbTours) :
            Tour = Donnees["Tours"][i]
            AfficherSRL(('|%4d' %(i+1)))
            AfficherSRL((' |%13s' %(Tour["Contrat"])))
            AfficherSRL((' |%8s' %(Tour["Bilan"])))
            AfficherSRL((' |%11s' %(Tour["DeCombien"])))
            AfficherSRL((' |%12s' %(Tour["Preneur"])))
            if NbJoueurs == 5 :
                AfficherSRL((' |%12s' %(Tour["Partenaire"])))
            if Tour["Poignee"] != ""  :
                AfficherSRL((' |%8s' %(Tour["Poignee"])))
            else:
                AfficherSRL((' |%8s' %('')))
            if Tour["PetitAuBout"] != "" :
                AfficherSRL((' |%14s' %(Tour["PetitAuBout"])))
            else :
                AfficherSRL((' |%14s' %('')))

            # comptons les points de la partie
            for j in range(0,len(CONTRATS)) :
                if Tour["Contrat"] == CONTRATS[j] :
                    FacteurMultiplicateur = FACTEUR_MULTIPLICATEUR[j]

            # Points de reference
            PointsDeReference = (ENJEU + int(Tour["DeCombien"])) * FacteurMultiplicateur
            if Tour["Bilan"] == "Chutee" :
                PointsDeReference = - PointsDeReference

            # Petit Au bout
            BonusPetitAuBout = 0
            if Tour["PetitAuBout"] != "":
                if Tour["PetitAuBout"] == "Attaque" :
                    BonusPetitAuBout = 10
                else :
                    BonusPetitAuBout = -10
                # mise a jour points de reference petit au bout
                PointsDeReference += BonusPetitAuBout * FacteurMultiplicateur

            # ScoreDuTour est un dictionnaire local
            ScoreDuTour = {}
            for j in range (0, NbJoueurs) :
                NomDuJoueur = Donnees["Joueurs"][j]
                ScoreDuTour[NomDuJoueur] = 0

            # Poignee n est pas multipliee
            BonusPoignee = 0
            if Tour["Poignee"] != "" :
                # simple double ou triple ?
                if Tour["Poignee"] == "Simple" :
                    BonusPoignee = 20
                elif Tour["Poignee"] == "Double" :
                    BonusPoignee = 30
                elif Tour["Poignee"] == "Triple" :
                    BonusPoignee = 40
                else :
                    AfficherARL(('Erreur d implementation 1. ca ne doit jamais de produire !'))

                if Tour["Bilan"] == "Chutee" :
                    BonusPoignee = -BonusPoignee

            # Points des preneur et partenaire
            if NbJoueurs == 5 :
                if Tour["Partenaire"] == "ToutSeul" :
                    ScoreDuTour[Tour["Preneur"]] = 4*(PointsDeReference + BonusPoignee)
                else :
                    ScoreDuTour[Tour["Preneur"]] = 2*(PointsDeReference + BonusPoignee)
                    ScoreDuTour[Tour["Partenaire"]] = PointsDeReference + BonusPoignee
            elif NbJoueurs == 3 :
                ScoreDuTour[Tour["Preneur"]] = 2*(PointsDeReference + BonusPoignee)
            else :
                ScoreDuTour[Tour["Preneur"]] = 3*(PointsDeReference + BonusPoignee)

            # Points des autres joueurs
            for j in range (0, NbJoueurs) :
                NomDuJoueur = Donnees["Joueurs"][j]
                if ScoreDuTour[NomDuJoueur] == 0 :
                    ScoreDuTour[NomDuJoueur] = -(PointsDeReference + BonusPoignee)
                ScoreDeLaPartie[NomDuJoueur] += ScoreDuTour[NomDuJoueur]

            for j in range (0,NbJoueurs) :
                AfficherSRL((' |%12d' %(ScoreDuTour[Donnees["Joueurs"][j]])))
            AfficherARL((" |"))

        AfficherLigneDeSeparation(NbJoueurs)

        if NbJoueurs == 5 :
            AfficherSRL(('%97s' %('          TOTAL')))
        else:
            AfficherSRL(('%83s' %('          TOTAL')))
        for j in range (0,NbJoueurs) :
            AfficherSRL((' |%12d' %(ScoreDeLaPartie[Donnees["Joueurs"][j]])))
        AfficherARL((" |"))

    # derniere ligne
    AfficherLigneDeSeparation(NbJoueurs)
    AfficherARL((""))

def VerifierNom(Donnees, Nom):
    if len(Nom) >= NOM_MAX_TAILLE :
        return TROP_LONG
    for n in Donnees["Joueurs"] :
        if n == Nom:
            return ERREUR
    return PAS_D_ERREUR

def Menu() :
    Choix = 0
    NomFichier = None
    Donnees = {}

    while Choix != 9 :
        AfficherARL(("******************************************************************"))
        AfficherARL(("Menu : Entrez un numero"))
        AfficherARL(("1. Entrez le nom d'une partie existente ou d'une nouvelle partie."))
        if Donnees != {} :
            AfficherARL(("2. Afficher le resume de la partie"))
            AfficherARL(("3. Ajouter un nouveau tour a la partie en cours"))
            if len(Donnees["Tours"]) > 0 :
                AfficherARL(("4. Retirer un tour a la partie en cours"))
        AfficherARL(("9. Sortir"))
        AfficherARL(("******************************************************************"))

        Choix = int(DemanderChiffre("Votre choix ? "))
        if Donnees == {} :
            if Choix == 2 or Choix == 3 or Choix == 4 :
                # choix non possible si pas de partie en cours
                Choix = 0
        elif Choix == 4 and len(Donnees["Tours"]) == 0:
            # choix non possible si pas au moins 1 tour de fait
            Choix = 0

        if Choix == 1 :
            AfficherARL(("Nom de la partie ? "))
            NomFichier = DemanderPhrase("    --> ")
            Donnees = ExtraireDonneesDuFichier(NomFichier)

            if Donnees == {} :
                # Pas de fichier trouve : c est une nouvelle partie
                NbJoueurs = 0
                Donnees["Joueurs"] = []
                AfficherARL(("Pas de fichier trouve. Il s\'agit donc d\'une nouvelle partie"))

                while NbJoueurs < 3 or NbJoueurs > 5 :
                    AfficherARL(("Nombre de Joueurs ? "))
                    NbJoueurs = DemanderChiffre("    --> ")
                    if NbJoueurs < 3 or NbJoueurs > 5 :
                        AfficherARL(("Erreur. Il faut entrer 3,4 ou 5"))
                i = 0
                while i < NbJoueurs :
                    AfficherSRL(("Nom du joueur numero : ", i+1))
                    NomJoueur = DemanderPhrase("    --> ")
                    if VerifierNom(Donnees, NomJoueur) == ERREUR :
                        AfficherARL(("2 joueurs avec le meme nom ? T'es serieux ? "))
                    elif VerifierNom(Donnees, NomJoueur) == TROP_LONG :
                        AfficherSRL(("C'est un peu trop long comme nom. Tu seras gentil de raccourcir ce nom a ", NOM_MAX_TAILLE, " caracteres max. "))
                    else :
                        Donnees["Joueurs"].append(NomJoueur)
                        i += 1
                Donnees["Tours"] = []
                MettreFichierAJour(NomFichier, Donnees, NOUVEAU_FICHIER)
            AfficherBilanPartie(Donnees)

        elif Choix == 2 :
            AfficherBilanPartie(Donnees)

        elif Choix == 3 :
            Tour = {}
            NbJoueurs =  len(Donnees["Joueurs"])

            # Garde ou petite ou autre chose ?
            c = DemanderChoixParmiSelection("Contrat de partie", CONTRATS)
            Tour["Contrat"] = CONTRATS[c]

            # Faite ?
            c = DemanderChoixParmiSelection("Faite ou chutee ?", BILANS)
            Tour["Bilan"] = BILANS[c]

            # De combien
            AfficherARL(("De combien ? "))
            c = -1
            while c < 0 :
                c = DemanderChiffre("    --> ")
            Tour["DeCombien"] = str(c)

            # Preneur
            c = DemanderChoixParmiSelection("Qui a pris ?", Donnees["Joueurs"])
            Tour["Preneur"] = Donnees["Joueurs"][c]

            # Partenaire
            if NbJoueurs == 5:
                cp = c
                # copier la liste de joueurs dans une nouvelle liste temporaire
                ListePartenaires = Donnees["Joueurs"][:]
                ListePartenaires.append("ToutSeul")
                while cp == c:
                    cp = DemanderChoixParmiSelection("Partenaire ?", ListePartenaires)
                Tour["Partenaire"] = ListePartenaires[cp]

            # Poignee
            Tour["Poignee"] = ""
            c = DemanderChoixParmiSelection("Poignee ? ", POIGNEES)
            if c > 0:
                Tour["Poignee"] = POIGNEES[c]

            # petit au bout
            Tour["PetitAuBout"] = ""
            c = DemanderChoixParmiSelection("Petit au bout ? Attaque : Derniere levee realisee par l'attaque. Defense : Derniere levee realisee par la defense.", PETIT_AU_BOUT)
            if c > 0:
                Tour["PetitAuBout"] = PETIT_AU_BOUT[c]

            # ajouter les donnees de ce tour aux donnees de la partie
            Donnees["Tours"].append(Tour)

            # on met a jour le fichier
            MettreFichierAJour(NomFichier, Donnees, REMPLACER_FICHIER)
            AfficherBilanPartie(Donnees)

        elif Choix == 4 :
            AfficherARL(("Quel est le numero de la partie a retirer ?"))
            c = int(DemanderChiffre("    --> "))
            c -= 1
            if c>=0 and c<len(Donnees["Tours"]) :
                del (Donnees["Tours"][c])
                # on met a jour le fichier
                MettreFichierAJour(NomFichier, Donnees, REMPLACER_FICHIER)
                AfficherBilanPartie(Donnees)
            else :
                AfficherARL(("Erreur dans la saisie. Essaie encore"))

Menu()
