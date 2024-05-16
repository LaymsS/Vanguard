## Projet Vanguard
Developped by Ghourtoule

### Introduction

Bienvenue sur le projet Vanguard.
Il s'agit d'un projet développé dans le cadre de mon Master en Cybersécurité.
Cet outil est conçu pour automatiser les tests de pénétration professionnels.

Il permet de consolider les différents résultats de l'analyse dans un rapport PDF bien structuré, ce qui permet aux professionnels de la sécurité d'examiner et de corriger plus facilement les vulnérabilités.

L'application a été développée en python et fonctionne sous KaliLinux, ce qui rend facile d'accès les différents outils.

Bien que Vanguard peut etre utilisé sans connaissance en cybersécurité, l'interprétation des résultats peut être compliquée.
Toutefois, dans un soucis d'accessibilitée, le rapport préente des graphiques explicatifs permettant de résumer de manière conscise et simple les résultats de l'analyse.


## Bien Commencer

Afin de récupérer le projet sur votre machine:

```bash
git clone https://github.com/LaymsS/Vanguard.git
cd projects
```

### Setup Your Own Projects

You can set up projects for yourself by following these steps:

- Fork the repo: https://github.com/2kabhishek/projects
- Clone it locally / Open it in GitHub Codespaces
- Open up `script.js` and update the `username` variable to your GitHub username.
- Open up `index.html` and update the `title` tag to make it your own.
- You may also want to update the favicon by updating the `link` tag in `index.html`
- Commit and push your changes
- Go to repo settings on GitHub, under `Pages` enable GitHub Pages.
  - Choose 'Deploy from a branch' with the `main` branch and `/` as the root directory.
- Done!

The site should be live on `https://<your-username>.github.io/projects`

#### Number Of Repos

The number of repos shown changes with the `maxPages` variable, the GitHub API supports 100 repos per page max.
If you have less than 100 repos, set `maxPages` to 1, if you have 300 then 3.

You can also edit the fetch query to reduce the per page repo count.

> There's no pagination, all repos show up on the same page.

### Forked Repos

To show forked repos set `hideForks = false` in `script.js`

### Authenticated Requests

If you are working locally and notice the API is not sending over data, it might be because of rate limit on GitHub API requests.

You can either wait for an hour or setup a personal access token on GitHub and pass that into the fetch request in `script.js`

### Themes

Comes with a dark and light theme by default, depends upon your system and browser settings.

Edit the variables under `:root` in `styles.css` to change color scheme.

### Programming Language Icons

This project uses [Devicon](https://devicon.dev/) for adding language icons, if the language name and icon are not
displayed, for any of your repos, update `devicons` mapping in `script.js`.

## How it was built

I built `Projects` using `HTML` `CSS` `JavaScript` and Neovim

## What I learned

- Learned about some quirks of the fetch API, during implementation of `maxPages`.
- Revisited Flex, box-shadow and some other CSS tricks

## What's next

You tell me!

Hit the ⭐ button if you found this useful.

## More Info