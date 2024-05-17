# Projet Vanguard
Developped by Ghourtoule

## Introduction

Bienvenue sur le projet Vanguard.
Il s'agit d'un projet développé dans le cadre de mon Master en Cybersécurité.
Cet outil est conçu pour automatiser les tests de pénétration de manière professionnels.

Il permet de consolider les différents résultats de l'analyse dans un rapport PDF bien structuré, ce qui permet aux professionnels de la sécurité d'examiner et de corriger plus facilement les vulnérabilités.

L'application a été développée en python et fonctionne sous KaliLinux, ce qui rend facile d'accès les différents outils.

Bien que Vanguard peut etre utilisé sans connaissance en cybersécurité, l'interprétation des résultats peut être compliquée.
Toutefois, dans un soucis d'accessibilitée, le rapport préente des graphiques explicatifs permettant de résumer de manière conscise et simple les résultats de l'analyse.


## Bien Commencer

### Prérequis


1. **Récupérer le projet sur votre machine**:
      ```python
      git clone https://github.com/LaymsS/Vanguard.git
      cd Vanguard/
      ```

2. **Installer les packages requis**:
      ```python
      pip install -r requirements.txt
      ```
---

## Usage

1. **Lancer l'application**: Pour lancer l'application, exécuter le  `main.py` script. 
   ```python
   python main.py

2. **Naviguer dans les différents menu**: Lors du premier lancement, Vanguard vous demanderas de créer une session. Il vous suffira de rentrer un nom afin d'accéder au menu principal.

3.  **Menu principal** : Le menu princial est composé de différentes options :
      - **Start**: L'option "Start" vous permettra de choisir entre deux mode d'éxecution de la toolbox
        - **SimpleMode**: est uun mode vous laissant le choix sur l'écution de vos actions. Toutefois, celle-ci ne sont pas automatisés. Vous n'avez pas le choix sur l'éxecution de plusieurs actions de manière automatisé. Elles sont réalisées au cas par cas. Ceux mode à été configuré dans le cas ou vous ne souhaitiez pas réalisé un scan complet mais plutot réaliser une recherche spécifique.
              - **AdvanceMode** : est un mode plus avancé. Il à été réalisé dans une optique de simplicité de séléction des différents choix de configuration. Ce mode permet l'éxecution d'une analyse complete celon votre configuration.
    3.2 **Documents**: Cette option vous permettra d'afficher une liste des différents rapports que vous avez réalisé dans la session, qu'il s'agisse de ceux du mode simple ou bien du mode Advance. Vous pourrez aussi les ouvrir directement depuis l'application.
    3.3 **Profil**: EN COURS DE DEVELOPPEMENT
    3.4 **Settings**: Cette option vous permet de personnaliser l'application afin qu'elle vous soit la plus accessible possible celon vos besoins ou vos préférences. Pour le moment vous pouvez personnaliser le thème de la toolbox. A therme cette option vous permettra de choisir entre différentes langues ce qui sera un très gros plus quan a la l'accessibilité de l'application et de son efficacité à générer des rapports.
    3.5 **New Session** : Vous permettra de fermer la session actuel et dans créer une nouvelle. Cela permet de mieux ségmenter vos analyse ou meme vos mission dans la meme application. 

