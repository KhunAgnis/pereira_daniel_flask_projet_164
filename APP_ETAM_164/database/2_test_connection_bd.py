"""Démonstration d'envoi d'une requête SQL à la BD
Fichier : 2_test_connection_bd.py
Auteur : OM 2023.03.21
"""

from APP_ETAM_164.database.database_tools import DBconnection

try:
    """
        Une seule requête pour montrer la récupération des données de la BD en MySql.
    """
    strsql_produits_afficher = """SELECT * FROM t_produit ORDER BY id_Produit ASC"""

    with DBconnection() as db:
        db.execute(strsql_produits_afficher)
        result = db.fetchall()
        print("data_produits ", result, " Type : ", type(result))


except Exception as erreur:
    # print(f"2547821146 Connection à la BD Impossible ! {type(erreur)} args {erreur.args}")
    print(f"2547821146 Test connection BD !"
          f"{__name__,erreur} , "
          f"{repr(erreur)}, "
          f"{type(erreur)}")
