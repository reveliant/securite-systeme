---
title: Configuration noyau (`sysctl`)
bg-image: volcano.jpg
bg-credits: https://unsplash.com/photos/Nqdx6-LW4VE
bg-authornick: "@tobyelliott"
bg-author: Toby Elliott
weight: 5
---
Se référer aux [Recommandations de sécurité relatives à un système GNU/Linux](https://www.ssi.gouv.fr/reco-securite-systeme-linux/)
de l'ANSSI :

- pour la pile réseau, durcir les configuration IPv4 et IPv6 face à des paquets
    peu commun ou non standards

    ANSSI : serveur sans routage et avec adresse IPv6 statique

    Pas d'IPv6 : `net.ipv6.conf.all.disable_ipv6 = 1`
- pour le reste du systèmes, paramétrages de la mémoire, des processus,
    du système de fichiers...
