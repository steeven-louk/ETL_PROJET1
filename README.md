# ETL Project

Ce projet est un exemple d'ETL (Extraction, Transformation et Chargement) réalisé en utilisant Python. L'objectif principal de ce projet est de démontrer comment extraire des données
à partir de différentes sources, les transformer selon les besoins spécifiques et les charger dans différentes destinations.

## Structure du Projet

Le projet est structuré de la manière suivante :

- `extraction/`: Ce répertoire contient les scripts pour extraire les données à partir de différentes sources telles que des fichiers CSV, JSON, XML, des bases de données, etc.


- `transformation/`: Ce répertoire contient les scripts pour transformer les données extraites selon les besoins spécifiques du projet. Cela peut inclure le nettoyage des données, la normalisation, l'agrégation, etc.


- `loading/`: Ce répertoire contient les scripts pour charger les données transformées dans différentes destinations telles que des fichiers CSV, JSON, XML, des bases de données, etc.


- `pipeline.py`: Ce fichier définit le pipeline ETL qui spécifie l'ordre dans lequel les opérations d'extraction, de transformation et de chargement doivent être effectuées.


- `config.pipeplane_config`: Ce fichier contient la configuration du pipeline ETL, y compris les sources de données, les transformations à appliquer et les destinations de chargement.


- `main.py`: Ce fichier est responsable de l'exécution automatique du pipeline ETL en lisant la configuration à partir de `config.pipeplane_config` et en appelant les fonctions appropriées pour exécuter chaque étape du pipeline.


- `destination`: Ce dossier contient les fichiers transformer et modifier


- `data`: Ce dossier contient tout les fichiers de test


- `README.md`: Le README, fournit des informations sur le projet, son objectif, sa structure et des instructions sur la façon de l'exécuter.

## Comment Exécuter le Projet

1. Assurez-vous que Python est installé sur votre système.

2. Cloner ce dépôt dans votre environnement local :
   ```bash
   git clone https://github.com/steeven-louk/ETL_PROJET1.git

3. Accéder au répertoire du projet :
    ```bash
    cd ETL_PROJET1
   
4. Assurez-vous que les fichiers de données nécessaires sont présents dans les répertoires spécifiés dans 
    ```bash
    config.pipeplane_config.yaml
5. Importer la base de donnée `dm22` dans votre `phpmyadmin`
   
6. Exécutez le fichier `main.py` en utilisant la commande `python main.py` pour lancer le pipeline ETL.

7. NB: Le Projet a été fait sur `Pycharm`