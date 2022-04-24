---
title: "TD : Cloisonner et isoler"
weight: 2
---
### Intégrer une application avec des composants isolés

- Nginx, uWSGI, Python et systemd
- [Service HTTP](/td/api.py) (API JSON avec Flask)
- [Service cryptographique](/td/crypto.py) (calcul d'un HMAC-SHA256)
- Communication par socket UNIX

<i class="fa fa-arrow-right"></i> Isolation des deux services Python
avec systemd
