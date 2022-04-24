---
title: Comment centraliser ?
weight: 2
---
- Utiliser des protocoles sécurisés (confidentialité, intégrité, authentification)
  <small>natifs ou avec TLS, à défaut SSH ou IPSec</small>
- Durcir et cloisonner la plateforme de centralisation (+ MCS)
- Prévoir une partition dédiée (cf. principes généraux)
- Superviser la volumétrie <small>peut vite déborder</small>
- Préférer une base de données structurée et indexée à des fichiers à plat
  <small>
  - comme Elasticsearch + Logstash
  - à défaut, `syslog-ng` / `rsyslog`
  </small>

<aside class="notes">

</aside>
