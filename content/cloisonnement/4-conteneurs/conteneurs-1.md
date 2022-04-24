---
title: Conteneurs
weight: 1
---
Avec les fonctionnalités précédentes, il est possible sur un même système hôte
(noyau) :

- de mettre en place des conteneurs Linux (sans noyau)
- d'isoler les processus et les ressources associées

Ces conteneurs peuvent être gérés :

- bas niveau avec les commandes [LXC](https://linuxcontainers.org/lxc/introduction/)
  (`lxc-*`)
- avec `systemd-nspawn` / `systemd-machined` (`machinectl`)
- plus haut niveau avec Docker ou [containerd](https://containerd.io/)
  pour faciliter la diffusion et le déploiement

<p><br/></p>

Voir aussi les [Recommandations pour la mise en place de cloisonnement
système](https://www.ssi.gouv.fr/guide-cloisonnement-systeme/), ANSSI

<aside class="notes">

</aside>
