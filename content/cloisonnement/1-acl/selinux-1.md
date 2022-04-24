---
title: SELinux
weight: 4
---
DAC souffre de nombreuses limitations :

- les utilisateurs ont un contrôle complet de leurs ressources (CRUD + nouveaux droits)
- les programmes ont les mêmes droits que leur utilisateur

<i class="fa fa-arrow-right"></i> Si un programme en `UID 0` est compromis,
le système entier est compromis

<p><br/></p>

*Security-Enhanced Linux* apporte un système de contrôle d'accès mandataire (MAC)
où le noyau applique une politique de contrôle complémentaire.

<aside class="notes">

Avec DAC, l'utilisateur fait sa vie et peut dilapider des droits sur ses ressources.
MAC permet d'ajouter un tiers de confiance, garant de l'application de la
politique de sécurité.

(Pour rappel, c'est l'UID qui compte dans le contrôle d'accès UNIX et nom le nom
de l'utilisateur, les contrôles étant désactivés au sein du noyau pour l'`UID 0`.

</aside>
