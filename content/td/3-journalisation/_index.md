---
title: "TD : Journaliser et centraliser"
weight: 3
---
### Ajouter des fonctionnalités de journalisation centralisée

- [Journaliser](https://docs.python.org/3/library/logging.html)
  les requêtes et les opérations cryptographiques
- Conserver localement sur 7 jours
  <small>(`systemd` + `logrotate`)</small>
- Centraliser sur un serveur voisin <small>(`rsyslog`)</small> et conserver 1 mois

<small>
Pour aller plus loin :

- Identifier les ressources sensibles et les surveiller avec `auditd`
- Mettre en place une pile Elasticsearch pour indexer et faciliter la rechercher
  dans les journaux

</small>

<i class="fa fa-arrow-right"></i> Recommandations de l'ANSSI :

- [Journalisation](https://www.ssi.gouv.fr/journalisation/)
- [Journalisation Windows](https://www.ssi.gouv.fr/journalisation-windows/)
