# Cci Netty App

Cci Netty App est une application Flask qui permet d'extraire des adresses e-mail à partir de fichiers CSV téléchargés. C'est l'outil idéal pour les utilisateurs de Netty souhaitant exporter leurs contacts et les importer dans leur boîte mail.

## Fonctionnalités

- **Chargement de fichiers CSV** : Téléchargez vos fichiers CSV directement via l'interface web.
- **Extraction d'e-mails** : Extrait les adresses e-mail valides à partir des fichiers CSV.
- **Interface Utilisateur Simple** : Une interface conviviale pour uploader les fichiers et afficher les e-mails extraits.

## Comment l'utiliser

1. **Installation** : Assurez-vous d'avoir Python et Flask installés sur votre machine.
2. **Configuration** : Clonez le dépôt et naviguez dans le dossier du projet.
3. **Dépendances** : Installez les dépendances nécessaires avec `pip install -r requirements.txt`.
4. **Lancement** : Exécutez l'application avec `python app.py`.
5. **Utilisation** : Ouvrez votre navigateur et allez à l'adresse `http://localhost:5000/` pour accéder à l'application.

## Exporter les contacts depuis Netty

Pour exporter vos contacts de Netty et les utiliser avec cette application, suivez ces étapes :

1. Accédez à la section contacts de Netty et ajustez l'affichage pour montrer 100 résultats.
2. Sélectionnez les contacts à exporter et téléchargez-les au format CSV.
3. Utilisez l'application pour charger le fichier CSV et extraire les adresses e-mail.

## Importer dans votre boîte mail

Après avoir extrait les adresses e-mail :

1. Copiez les adresses e-mail extraites.
2. Créez un nouveau message dans votre boîte mail et collez les adresses dans le champ "Cci".

## Développé par

Guillaume Meilgen - Version 2.0.1 - 2024
