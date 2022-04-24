---
title: SELinux
weight: 4
---
SELinux utilise des contextes de sécurité composés :

- d'une identité (`_u`, propriétaire du contexte)
- d'un rôle (`_r`)
- d'un domaine pour les sujet (utilisateurs ou processus)
ou d'un type pour les objets (ressources passives) (`_t`).

Le contexte d'un objet peut être vu avec `ls -Z` :

```console
drwxr-xr-x root root system_u:object_r:etc_t  /etc
```

<p><br/></p>

Écrire une politique de sécurité est **difficile**.
Certaines distributions appliquent par défaut une politique SELinux,
comme RHEL qui se base sur le FHS.

<aside class="notes">

Une politique de sécurité doit, pour pouvoir être fine, être établie lors du
développement de l'application, où l'on connait (ou pourrait connaitre, avec les
langages de haut niveau) les appels systèmes nécessaires.

Les contextes de sécurité sont des labels sur les objets qui indiquent les
conditions pour y accéder. Se rappeler que SELinux a été conçu par la NSA
comme système de sécurité multi-niveaux, lié en particulier au classifié de défense.

Un cours plus détaillé sur SELinux est prévu par le second intervenant du module.

</aside>
