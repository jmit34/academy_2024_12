import pandas as pd
import re, os, sys

def helpme(): 
    print("**********************************************************************************")
    print("* makelist.py : fait une liste d'emails depuis un fichier excel                  *")
    print("*  paramètres  :                                                                 *")
    print("   - le nom du fichier                                                           *")
    print("*  - le numéro de feuille (sheet), 0 pour la première                            *") 
    print("*  - le numéro de la colonne contenant les emails (0 pour la première)           *") 
    print("*    attention : cette colonne doit être au moins aussi longue que ses voisines  *") 
    print("*  - un pattern à selectionner après le @ de l'adresse mail                      *") 
    print("**********************************************************************************")
    print("***  il faut être dans un environnement python qui connait pandas              ***")
    print("**********************************************************************************")
    print("*-version-************************************************************************")
    print("* 20231110 v0.1 jmt ajout des infos de versioning et de la fonction helpme()     *")
    print("* 20231215 v0.2 jmt vérifie si le fichier existe avant de tenter de le lire      *")
    print("* 20240221 v0.3 jmt sélection du domaine des mail (que ibm, laposte, Sanofi ...) *")
    print("* 20240430 v0.4 jmt produit un fichier 'liste.txt'                               *")
    print("**********************************************************************************")

def verif_fic(fname):

    if os.path.exists(fname):
        print(" ---- le fichier existe")
        return True
    else:
        print(" ---- le fichier n'existe pas.")
        return False

def valid_email(email,domain):
    #print("**>", email, domain)  
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):  
        if domain == "" :
            return True
        else : 
            if domain in email.split('@')[1]: 
                return True
    return False

def make_dist_list(fname,sheet=0,col=0,domain=""): 
    try:
        df = pd.read_excel(fname,sheet_name=sheet)
    except Exception as e:
        print(f"Une exception de type {type(e).__name__} a été levée : {e}")
    #TODO : tester d'abord si le fichier existe, puis la sheet, puis la colonne

    df2 = df.iloc[:,[col]]
    l2 = df2.values.tolist()
    mail_list = ""
    count = 0
    #print(count)
    fiout =  open('liste.txt','w')
    #print('domaine=', domain, len(domain))
    for e in l2:
        #print(e[0])
        if valid_email(e[0], domain):
            count +=1 
            mail_list = mail_list + e[0] + ";"
            fiout.write(e[0] + ";")
    print("="*20)
    print(f"in file : {fname}")
    print(f"sheet   : {sheet}")
    print(f"col     : {col}") 
    print(f"I found : {count} valid emails:  ")
    print("="*20)
    print(mail_list)
    print("="*20)

#print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))
if len(sys.argv) < 4: 
    helpme()
    print(' ')
    print(" Erreur : le nombre d'argument passés est incorrect")
    print(' ')
    exit()



fname,sheet,col, domain = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]),sys.argv[4]
if domain in ('None','none','all','a','All'): 
    domain = ""

if verif_fic(fname) == False: 
    print("on ne trouve pas le fichier")
    exit(1)

make_dist_list(fname,sheet,col,domain)
