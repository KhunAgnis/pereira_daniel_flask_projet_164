"""Gestion des formulaires avec WTF pour les films
Fichier : gestion_films_wtf_forms.py
Auteur : OM 2022.04.11

"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import Length
from wtforms.validators import Regexp



class FormWTFAjouterStock(FlaskForm):
    """
        Dans le formulaire "produits_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_couleur_regexp = ""
    nom_couleur_add_wtf = StringField("Nom de la couleur ", validators=[Length(min=2, max=2000, message="min 2 max 20"),
                                                               Regexp(nom_couleur_regexp,
                                                                      message="Pas de chiffres, de caractères "
                                                                              "spéciaux, "
                                                                              "d'espace à double, de double "
                                                                              "apostrophe, de double trait union")
                                                               ])

    submit = SubmitField("Enregistrer la couleur")


class FormWTFUpdateCouleur(FlaskForm):
    """
        Dans le formulaire "film_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    nom_couleur_regexp = ""
    nom_couleur_add_wtf = StringField("Nom de la couleur ", validators=[Length(min=2, max=2000, message="min 2 max 20"),
                                                                        Regexp(nom_couleur_regexp,
                                                                               message="Pas de chiffres, de caractères "
                                                                                       "spéciaux, "
                                                                                       "d'espace à double, de double "
                                                                                       "apostrophe, de double trait union")
                                                                        ])

    submit = SubmitField("Mettre à jour la couleur")


class FormWTFDeleteCouleur(FlaskForm):
    """
        Dans le formulaire "film_delete_wtf.html"

        nom_film_delete_wtf : Champ qui reçoit la valeur du film, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "film".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_film".
    """
    nom_couleur_delete_wtf = StringField("Effacer cette couleur")
    submit_btn_del_couleur = SubmitField("Effacer la couleur")
    submit_btn_conf_del_couleur = SubmitField("Etes-vous sur de vouloir effacer ?")
    submit_btn_annuler = SubmitField("Annuler la suppression")
