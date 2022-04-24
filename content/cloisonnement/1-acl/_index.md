---
title: Contrôle d'accès UNIX (ACL)
bg-image: lock.jpg
bg-credits: https://unsplash.com/photos/ybtUqjybcjE
bg-authornick: "@calina"
bg-author: Georg Bommeli
weight: 2
---
### Rappels

Système de contrôle d'accès discrétionnaire (DAC) où tout est fichier :

<div class="columns">

- Utilisateur propriétaire (`u`)
- Groupe propriétaire (`g`)
- Autres utilisateurs (`o`)
{.column}

- Lecture (`r`)
- Ecriture (`w`)
- Exécution / traversée (`x`)
{.column}

</div>

#### Ne pas oublier sur Linux

- ACL étendues (`getfacl` / `setfacl`)
- On peut ainsi (un peu) s'orienter vers du contrôle d'accès par rôles (RBAC)

<aside class="notes">

Les ACL UNIX en elles-mêmes sont assez pauvres et ne peuvent donc couvrir tous
les besoins de sécurité ; en particulier, l'utilisation d'un seul groupe ne
permet pas une approche RBAC.

Rappel DAC vs RBAC :

- avec DAC, on *vous* confère personnelement des droits, qui doivent être
  explicitement révoqués lorsque vous perdez le besoin d'en connaître
- avec RBAC, on confère les droits à un rôle que l'on vous assigne, et les droits
  sont révoqués en même temps que la perte du rôle (par exemple un badge d'accès
  vous est conféré en tant qu'élève ou apprenti, et sera révoqué à la fin de votre
  formation ou vous perdrez ce rôle d'élève ou d'apprenti).

</aside>
