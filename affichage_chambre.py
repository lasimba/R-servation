offre_standard_ch_i = ['2 personnes', 'TV', 'Lit double 140 * 120','Petit frigo', 'Machine à café', 'Set de thé','Set de bain','3 serviettes de douches']
offre_standard_ch_d = ['3 personnes', 'TV', 'Lit double 80 * 80','Petit frigo', 'Machine à café', 'Set de thé','Set de bain','3 serviettes de douches']
offre_suite_royale = ['2 personnes', 'TV', 'Lit double 200 * 200','Petit frigo', 'Machine à café', 'Set de thé','Set de bain','3 serviettes de douches', 'Corbeille de fruits','Serveur dédié à la chambre', 'Pack de bienvenue'] #a faire le dernier
offre_studio = ['3 personnes', 'TV', 'Lit double 140 * 120','Petit frigo', 'Machine à café', 'Set de thé','Set de bain','3 serviettes de douches','Canapé','Kitchenette']
import os 
# def main() : 
    

def main_menu ():
    print("--------------------------------------------------")
    print("     BIENVENUE DANS NOTRE APP DE RESERVATION      ")
    print("--------------------------------------------------")
    print("     1.VOIR NOS TOUTES LES OFFRES")
    print("     2.QUITTER")
    print("--------------------------------------------------")
    choix = int(input("Veuillez choisir une option : "))
    print("--------------------------------------------------")
    while (choix < 1 or choix > 2) :
        print("L'option", choix," ne figure pas parmi les options")
        choix = int(input("Veuillez choisir une option : "))
        print("--------------------------------------------------")
    return choix 
def menu_offres(choix) : 
    if choix == 1 :
        os.system('cls')
        print("--------------------------------------------------")
        print("VOICI LES OFFRES DISPONIBLES DANS NOTRE HOTEL")
        print("--------------------------------------------------")
        print("1.OFFRE STANDARD (CHAMBRE INDIVIDUELLE)")
        print("2.OFFRE STANDARD+ (CHAMBRE DOUBLE)")
        print("3.OFFRE SUITE ROYALE ")
        print("4.OFFRE STUDIO")
        print("5.RETOUR")
        print("--------------------------------------------------")
        choix_offre = int(input("Veuillez choisir une offre : "))
        print("--------------------------------------------------")
        while choix_offre < 1 or choix_offre > 5 :
            print("L'option", choix_offre," ne figure pas parmi les offres")
            choix_offre = int(input("Veuillez choisir une offre : "))
            print("--------------------------------------------------")
        return choix_offre
def affichage_offre(choix_offre) : 
    retour = 0
    if choix_offre == 1 :
        while retour != 1 : 
            affichage_titre("STANDARD")
            affichage(offre_standard_ch_i)
            retour = int(input("1.Retour")) 
        if retour == 1 :
            menu_offres(1)
    elif choix_offre == 2 : 
        while retour != 1 : 
            affichage_titre("CHAMBRE DOUBLE")
            affichage(offre_standard_ch_i)
            retour = int(input("1.Retour")) 
        if retour == 1 :
            menu_offres(1)
    elif choix_offre == 3 :
        while retour != 1 : 
            affichage_titre("SUITE ROYALE")
            affichage(offre_suite_royale)
            retour = int(input("1.Retour"))
        if retour == 1 :
            menu_offres(1)
    elif choix_offre == 4 : 
        while retour != 1 :
            affichage_titre("STUDIO")
            affichage(offre_studio)
            retour = int(input("1.Retour"))
        if retour == 1 :
            menu_offres(1)
    else : 
        os.system('cls')
        main_menu()
def affichage_titre(titre):
    os.system('cls')
    print("--------------------------------------------------")
    print("INFOS SUR L'OFFRE ",titre)
    print("--------------------------------------------------")
def affichage (offre) :
    for i in offre: 
        print(i)
    print("--------------------------------------------------") 

