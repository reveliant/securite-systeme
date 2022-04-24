---
weight: 1
---
La fonctionnalité Linux des *Control groups*  (`cgroups(7)`) permet de :

- organiser les processus en groupes hiérarchiques
- limiter leurs ressources
- les superviser (`systemd-cgtop`)

Ils sont présentés à l'utilisateur comme un simple système de
fichiers monté (`/sys/fs/cgroup`) : *tout est fichier*.

<p><br/></p>

systemd crée par défaut un cgroup sous `system.slice` pour chaque service
(<i class="fa fa-arrow-right"></i> `systemd-cgls`).

<aside class="notes">

</aside>
