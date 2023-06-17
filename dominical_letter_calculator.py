def est_bissextile(annee):
    """
    Vérifie si une année est bissextile selon le calendrier grégorien.
    Une année est bissextile si elle est divisible par 4 mais pas par 100,
    sauf si elle est également divisible par 400.
    """
    # Si l'année n'est pas divisible par 4, elle n'est pas bissextile.
    if annee % 4 != 0:
        return False
    # Si l'année est divisible par 4 mais pas par 100, elle est bissextile.
    elif annee % 100 != 0:
        return True
    # Si l'année est divisible par 100 mais pas par 400, elle n'est pas bissextile.
    elif annee % 400 != 0:
        return False
    # Si l'année est divisible par 400, elle est bissextile.
    else:
        return True

def calculer_lettre_dominicale(annee):
    """
    Calcule la lettre dominicale de l'année donnée.
    La lettre dominicale est une méthode utilisée pour déterminer le jour de la semaine 
    de toute date dans une année.
    """
    # Calcul des valeurs intermédiaires pour le calcul de la lettre dominicale.
    siecle = annee // 100
    siecle_div_4 = siecle // 4
    annee_sans_siecle = annee % 100
    annee_sans_siecle_div_4 = annee_sans_siecle // 4
    
    # Calcul de la somme des valeurs intermédiaires.
    somme_intermediaire = 2 * siecle - siecle_div_4 - annee_sans_siecle - annee_sans_siecle_div_4
    
    # Calcul du reste de la division de la somme par 7.
    reste_division = somme_intermediaire % 7
    
    # Si le reste est négatif, prendre son complément à 7.
    if reste_division < 0:
        reste_division += 7
    
    # Ajouter 1 au reste pour obtenir la valeur finale.
    reste_final = reste_division + 1
    
    # Convertir la valeur finale en lettre majuscule.
    lettre_dominicale_commune = chr(64 + reste_final)
    
    # Si l'année est bissextile, calculer une deuxième lettre pour les dix derniers mois.
    if est_bissextile(annee):
        valeur_bissextile = ((reste_final + 7) % 7) + 1
        lettre_dominicale_bissextile = chr(64 + valeur_bissextile)
        # Retourner les lettres dans l'ordre inverse.
        return lettre_dominicale_bissextile + lettre_dominicale_commune
    else:
        return lettre_dominicale_commune
    
# Exemple d'utilisation
for annee in range(2030, 2040):
    print(f"Lettre dominicale de l'année {annee}: {calculer_lettre_dominicale(annee)}")
