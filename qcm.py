def poser_question(question, r1, r2, r3, r4, choix_bonne_reponse):
    global score
    print("QUESTION :")
    print(" ",question)
    print(" (a)",r1)
    print(" (b)",r2)
    print(" (c)",r3)
    print(" (d)",r4)
    print()
    reponse = input("votre réponse est: ")

    reponse_correcte = False
    if reponse == choix_bonne_reponse:
        print("bonne reponse")
        score += 1
    else:
        print("mauvaise reponse")

    print()
    
score = 0
poser_question("Quelle est la capitale de la France?","Marseille","Nice", "Paris ","Nantes","c")
poser_question("Quelle est la capitale de l'Italie ?","Rome","Venise", "Pise","Florence","a")
poser_question("Quelle est la capitale de Madagascar?","Antsirabe","Toliara", "Toamasina","Antananarivo","d")

print("Score final :",score)