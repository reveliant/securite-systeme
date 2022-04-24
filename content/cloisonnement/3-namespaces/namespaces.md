---
weight: 2
---
Les `(*_)namespaces(7)` permettent de cloisonner les applications sur plusieurs types de ressources :

| Type | Fonctionnalité |
| ---- | -------------- |
| *Mount* | Isolation des points de montage<br/><small>`chroot` en *beaucoup* mieux</small> |
| *UTS* | Isolation du nom d'hôte et de domaine |
| *IPC* | Isolation des communications interprocessus<br/><small>(IPC System V, files de messages POSIX)</small> |
| *User* | Isolation des identifiants utilisateurs et des groupes<br/><small>Permet d'avoir un `UID 0` sans être vraiment privilégié</small> |
| *PID* | Isolation des identifiants des processus |
| *Network* | Isolation des ressources réseau (interfaces, ports...) |
| *Cgroup* | Isolation des Cgroups |
| *Time* | Isolation des horloges système |

<aside class="notes">

</aside>
