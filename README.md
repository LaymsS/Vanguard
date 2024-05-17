# Projet M1 SupDeVinci Vanguard
Developped by Ghourtoule

<p align="center">
  <img src="vanguard_git.png" alt="Vanguard"/>
</p>

## Table of Contents
- [Introduction](#Introduction)
- [Bien Commencer](#Bien-commencer)
- [Usage](#Usage)
- [Features](#Features)
- [Remarques et amélioration](#Remarques-et-Améliorations)
- [Difficultées rencontrées](#Difficultées-rencontrées)
- [Licences et dépendances](#Licences-et-dépendances)

## Introduction

Bienvenue sur le projet Vanguard.
Il s'agit d'un projet développé dans le cadre de mon Master en Cybersécurité.
Cet outil est conçu pour automatiser les tests de pénétration de manière professionnelles.

Il permet de consolider les différents résultats de l'analyse dans un rapport PDF bien structuré, ce qui permet aux professionnels de la sécurité d'examiner et de corriger plus facilement les vulnérabilités.

L'application a été développée en python et fonctionne sous Kali Linux, ce qui rend faciles d'accès les différents outils.

Bien que Vanguard pût être utilisé sans connaissance en cybersécurité, l'interprétation des résultats peut être compliquée.
Toutefois, dans un souci d'accessibilités et de compréhension, le rapport présente des graphiques explicatifs permettant de résumer de manière concise et simple les résultats de l'analyse.


## Bien Commencer

### Prérequis

Assurez-vous de posséder les applications suivantes sur votre système Linux :

> python 3.11

> Hydra (pas de version spécifique)

> Nikto (pas de version spécifique)

### Installation

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
        
        - **SIMPLE**: est uu mode vous laissant le choix sur l'éxécution de vos actions. Toutefois, celles-ci ne sont pas automatisés. Vous n'avez pas le choix sur l'éxecution de plusieurs actions de manière automatisé. Elles sont réalisées au cas par cas. Ceux mode a été configuré dans le cas ou vous ne souhaitiez pas réaliser un scan complet mais plutot réaliser une recherche spécifique.
          
        - **ADVANCE** : est un mode plus avancé. Il a été réalisé dans une optique de simplicité de sélection des différents choix de configuration. Ce mode permet l'exécution d'une analyse complète selon votre configuration.
          
      - **DOCUMENTS**: Cette option vous permettra d'afficher une liste des différents rapports que vous avez réalisée dans la session, qu'il s'agisse de ceux du mode simple ou bien du mode Advance. Vous pourrez aussi les ouvrir directement depuis l'application.
        
      - **PROFIL**: EN COURS DE DEVELOPPEMENT
        
      - **SETTINGS**: Cette option vous permet de personnaliser l'application afin qu'elle vous soit la plus accessible possible celon vos besoins ou vos préférences. Pour le moment vous pouvez personnaliser le thème de la toolbox. A therme cette option vous permettra de choisir entre différentes langues ce qui sera un très gros plus quant à l'accessibilité de l'application et de son efficacité à générer des rapports.
        
      - **NEW SESSION** : Vous permettra de fermer la session actuelle et d'en créer une nouvelle. Cela permet de mieux segmenter vos analyses ou meme vos missions dans la meme application. 


1. **SIMPLE MODE**
   IMAGE WINDOWS SIMPLE MODE

   DESCRIPTION DE SIMPLE MODE

2. **ADVANCE MODE**
   IMAGE WINDOWS ADVANCE MODE

   DESCRIPTION DE ADVANCE MODE

---

## Features

  ### 1. Nmap Scan
  - La toolbox Vanguard est utilisée avec Nmap afin de réaliser un scan du réseau / d'une IP ou d'un domaine et de récupérer des informations à propos des différents ports sur la/les cibles, ainsi que les différents services et leur version.
  - Le scan Nmap est associé à des scripts `Vulners` afin de récupérer les différentes CVEs (Common Vulnerabilities and Exposures) trouvées parmi les ports et services.
  
  ### 2. Nikto Scan
  - Le scan `Nikto` est utilisé afin de scanner le web-serveur de(s) cibles qui ont été configurées ou trouvées.
  - En effet, Nikto est un outil open source permettant de réaliser des tests sur les serveurs web et de trouver de multiples éléments tels que les versions dépassées, des problèmes spécifiques à une version, des fichiers ou dossiers accessibles contenant des données potentiellement dangereuse...
  
  ### 3. Password Analyser / Leak Analyser
  - Vanguard permet de vérifier la robustesse d'un mot de passe que vous lui communiquerait, d'une liste présente dans un fichier CSV ou meme qu'il aurait trouvé lors d'un scan automatique.
  - La toolbox permettra également de vérifier si ce mot de passe est présent dans des leaks de bases de données
  
  ### 4. Email Scrapper / Email Analyser
  - La toolbox possède une fonction complémentaire souvent associée à la `3. (Password / Leak)`, celle de pouvoir vérifier si un email est présent dans des bases de données qui auraient leak.
  - Lors d'éxécutions d'une analyse Advance, Vanguard vérifira sur les différentes pages du / des serveurs web, si des emails sont présents et vérifira si ceux-ci sont compromis.
  
  ### 5. Subdomain Enumeration
  - Vous avez la possibilité de récupérer des informations concernant le domaine principal ainsi qu'énumérer tous les sous-domaines associés au domaine principal.
  - Il s'agit d'une fonctionnalitée présente dans le mode Simple.
  
  ### 6. Exploit SSH
  - Lors d'une analyse automatisée, si le port 22 est présent ou bien qu'un service utilise SSH, alors la toolbox tentera une analyse par BruteForce sur la machine cible à l'aide de l'outil Hydra.
  ! ATTENTION ! Cette fonctionnalité peut affecter les performances de votre système car demande certaines ressources. Le temps d'exécution de l'analyse peut s'en retrouver grandement impacté.
  - Si le test de pénétration est fonctionnel, les identifiants seront récupérés et analysés afin d'établir si ceux-ci sont compromis, tant par la robustesse que par leur présence dans certaines bases de données.
  - En plus de permettre un accès vers la machine cible, cela permettra à Vanguard de proposer pour un futur développement de la toolbox une fonctionnalitée `RESPONSE` afin de proposer des correctifs.
  
  ### 7. Exploit target
  - Suite à une connexion distante réussite avec la machine, la toolbox sera en mesure de récupérer automatiquement différents éléments sur la machine.
  - On pourra retrouver dans le rapport, le nombre et les noms des utilisateurs présent sur machine, le nombre et le détail des fichiers de clés, de backup ou de mot de passe chiffré (shadow.txt).
  - Vous retrouverez aussi les différentes règles existant sur le firewall (si elles existent) ainsi que les différentes applications installées (nom, version, emplacement) sur la machine.

  ### 8. Analyse MITRE ATT&CK
  - Vanguard filtres les différentes CVEs trouvées sur la / les cibles et les classifies celon les tactiques `MITRE ATT&CK`.
  - Bien qu'il s'agisse d'un classement non précis car le script à été réalisé à la main sans dépendances, cela permet de générer un graphique mettant en lumière les principales failles et techniques qui pourraient etre utilisé par un attaquant sur le SI cible.
  
  
  #### 9. Rapport Generation
  - Suite à l'éxecution d'une analyse sur une cible, la toolbox générera un rapport PDF détaillé et accessible.
  - Le rapport sera découpé en deux parties.
        - La première plus générique propose des graphiques et tableaux d'analyse recapitulatifs des différentes actions qui ont étés prises lors de l'éxécution du scan ainsi que les différentes informations trouvées
        - La deuxième plus détaillé porpose quant à elle un détails des informations trouvés (liste des CVEs, listes des ports, services, usernames...etc)

## Remarques et Améliorations

### Remarques

  - Certaines parties de l'application non pas pu etre développé comme voulu. Principalement la partie sur l'exploitation.
    - Il était voulu de développer l'exploitation à l'aide de requete API afin de récupérer des informations sur les CVEs trouvées et permettre à la toolbox de créer un `Payload` à utiliser sur la cible. Malheureusement par manque de temps et de connaissance en dévellopement cela n'a pas pu etre réalisé
  - Certains bouts de code ne sont pas fonctionnelles dans le cas ou aucune donnée n'est récupéré par le scan, entrainant le crash de l'application ainsi que la non génération du rapport.
  - La gestion des erreurs n'est pas fini d'etre correctement implémenté dans le code
  - Implémentation de l'outil SQLMap non fonctionnel du à des problèmes techniques 

### Améliorations

  - Ajout de paramètres pour la personnalisation de l'application
    - Ajouter le choix de la langue pour l'application
  - Implémentation de la logique d'exploitation initialement voulue.
  - Apporter les correctifs nécessaires pour un fonctionnement complet sans erreurs lorsque la toolbox ne récupère pas les informations voulues. 

## Difficultées Rencontrées

Parmi les différentes difficultées rencontrées lors du développement de la toolbox ont principalement été des difficultées sur l'apprentissage de la récupération et l'ajout de données dans des fichiers `JSON` et leurs utilisations.

## Licences et Dépendances

  - `Hydra = Licence : GNU Affero General Public License (AGPL) v3`
  - `Paramiko = Licence : GNU Lesser General Public License (LGPL)`
  - `Pillow = Licence : Historical Permission Notice and Disclaimer (HPND)`
  - `Nmap = Licence : GNU General Public License (GPL) v2`
  - `Weasyprint = Licence : BSD License`
  - `Password_strength = Licence : MIT License`
  - `Enzoic = Licence : MIT License`
  - `PIL = Licence : Historical Permission Notice and Disclaimer (HPND)`

