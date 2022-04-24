---
weight: 2
---
### `chroot` / `jail`

`jail` est une alternative plus robuste sous FreeBSD avec :

- un appel système
- un jeu de commandes (`jail`, `jls` et `jexec`)

Un `jail` a aussi son propre environnement réseau (nom d'hôte et adresse IP.)

<p><br/></p>

Faute de mieux, on a le programme `firejail` sous Linux, utilisant les
*namespaces* et *seccomp-bpf*

<aside class="notes">

Pour faire simple, `jail` = `chroot` en moins pire. Le mieux est quand même
d'utiliser des mécanismes modernes comme les *namespaces* qui ont été conçus
à cet effet et sont bien plus robustes

`firejail` permet historiquement d'isoler le navigateur web, qui dispose notamment
d'accès au système de fichiers, pour ainsi éviter (par exemple) l'aspiration de fichiers
personnels depuis un site web indélicat.

</aside>
