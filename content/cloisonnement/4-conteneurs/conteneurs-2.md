---
title: Conteneurs ±
weight: 2
---
### Avantages

- isolation des composants applicatifs au sein des conteneurs
- réduction des privilèges (`user_namespaces`...)
- scalabilité horizontale facilitée par la répétabilité du déploiement

### Inconvénients

- complexité accrue de l'architecture applicative
  <small>(quel conteneur héberge quoi ?)</small>
- complexité accrue de l'administration (socle + gestionnaire)
- jonction (plus) forte entre administration système et développement (*devops*)
- est-ce adapté pour assurer une sécurité élevée ?
  <small>(confiance dans l'isolation offerte par le noyau)</small>

<aside class="notes">

</aside>
