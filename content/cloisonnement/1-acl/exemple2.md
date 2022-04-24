---
title: Exemples d'utilisation des ACL
weight: 3
---
### Répertoire de numérisation pour photocopieur

`ls -lR /srv/partage`

```console
drwxrwx---+ 7 root secretariat 4096 15 janv.  2019 Secrétariat

/srv/partage/Secrétariat
total 38
drwxrwx-w-  2 root secretariat 4096 15 janv.  2019 Numérisation
```

`getfacl /srv/partage/Secrétariat`

```console
# file: srv/partage/Secrétariat
# owner: root
# group: secretariat
user::rwx
group::rwx
other::---
user:photocopieur:--x
```

<aside class="notes">

On veut permettre le dépôt de fichiers numérisés par un photocopieur sur
le serveur de partage d'une entreprise. Les fichiers doivent être déposés
dans le repertoire du groupe fonctionnel principal des utilisateurs.

L'information restera ainsi compartimentée entre les différents groupes d'utilisateurs
(application du principe du besoin d'en connaître).

On observe ici des ACL étendues Linux (le `+` à la fin des droits).
L'utilisation d'ACL étendues est suffisement rare pour s'intérroger (`getfacl`)
sur les cas que vous rencontrerez.

</aside>
