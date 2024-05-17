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

      - **START**: L'option "Start" vous permettra de choisir entre deux mode d'éxecution de la toolbox
        
        - **SIMPLE**: est uu mode vous laissant le choix sur l'écution de vos actions. Toutefois, celle-ci ne sont pas automatisés. Vous n'avez pas le choix sur l'éxecution de plusieurs actions de manière automatisé. Elles sont réalisées au cas par cas. Ceux mode à été configuré dans le cas ou vous ne souhaitiez pas réalisé un scan complet mais plutot réaliser une recherche spécifique.
          
        - **ADVANCE** : est un mode plus avancé. Il à été réalisé dans une optique de simplicité de séléction des différents choix de configuration. Ce mode permet l'éxecution d'une analyse complete celon votre configuration.
          
      - **DOCUMENTS**: Cette option vous permettra d'afficher une liste des différents rapports que vous avez réalisé dans la session, qu'il s'agisse de ceux du mode simple ou bien du mode Advance. Vous pourrez aussi les ouvrir directement depuis l'application.
        
      - **PROFIL**: EN COURS DE DEVELOPPEMENT
        
      - **SETTINGS**: Cette option vous permet de personnaliser l'application afin qu'elle vous soit la plus accessible possible celon vos besoins ou vos préférences. Pour le moment vous pouvez personnaliser le thème de la toolbox. A therme cette option vous permettra de choisir entre différentes langues ce qui sera un très gros plus quan a la l'accessibilité de l'application et de son efficacité à générer des rapports.
        
      - **NEW SESSION** : Vous permettra de fermer la session actuel et dans créer une nouvelle. Cela permet de mieux ségmenter vos analyse ou meme vos mission dans la meme application. 


1. **SIMPLE MODE**
   IMAGE WINDOWS SIMPLE MODE

   DESCRIPTION DE SIMPLE MODE

2. **ADVANCE MODE**
   IMAGE WINDOWS ADVANCE MODE

   DESCRIPTION DE ADVANCE MODE

## Features

### 1. Nmap Scan
La toolbox Vanguard est utilisé avec Nmap afin de réaliser un scan du réseau / d'une IP ou d'un domaine et de récupérer des informations à propos des différents ports sur la/les cibles, ainsi que les différents services et leur version.
Le scan Nmap est associé à des scripts 'Vulners' afin de récupérer les différentes CVEs (Common Vulnerabilities and Exposures) trouvées parmis les ports et services.

### 2. Nikot Scan
Le scan 'Nikot' est utilisé afin de scanner le web-server de(s) cibles qui ont étés configurées ou trouvées.
En effet, Nikto est un outil open-source permettant de réaliser des tests sur les serveurs webs et de trouver de multiple éléments tels que les versions dépassées, des problèmes spécifiques à une version, des fichiers ou dossiers accessibles contenant des données potentiellement dangereuse...

### 3. Password Analyser / Leak Analyser
Vanguard permet de vérifier la robustesse d'un mot de passe que vous lui communiqueré, d'une liste présnete dans un fichier CSV ou meme qu'il aurait trouvé lors d'un scan automatique.
La toolbox permettra églement de vérifier si ce mot de passe est présent dans des leaks de bases de données
