---
title: Exemples d'utilisation des ACL
weight: 2
---
### Serveur web (`httpd:http`) et PHP FPM (`php:http`)

```console
srw-rw---- 1 httpd http    0  5 mars  16:21 /run/php-fpm.sock
-r-------- 1 php   http 3272 13 févr.  2021 /etc/myapp/privkey.pem
```

<aside class="notes">

On veut ici séparer le fonctionnement du serveur web de son service applicatif
PHP FPM, tout deux membres du groupe `http` et peuvent donc échanger *via* `php-fpm.sock`,
mais disposent de comptes de service dédiés pour leurs fonctionnalités respectives.

La clé privée n'est ainsi accessible, en lecture uniquement, qu'à l'application.

Les applications web ont d'ailleurs trop souvent le droit d'écriture sur leur code
qui pourrait conduire à une exécution de code arbitraire à distance (*RCE*).
Le seul espace éventuellement légitime en écriture serait un répertoire de
téléversement (*upload*).

</aside>
