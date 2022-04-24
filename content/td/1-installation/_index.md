---
title: "TD : Installer un système sécurisé"
weight: 1
---
### Installer un système sécurisé sur base Debian

- Chiffrement des disques
- Partitionnement et montage adaptés
- [Durcissement noyau](/td/sysctl.conf) (`sysctl`)
- Durcissement OpenSSH (`PermitRootLogin no` au minimum)
- Filtrage Netfilter (<i class="fa fa-down-long"></i> SSH --
  <i class="fa fa-up-long"></i> DHCP, DNS, HTTP[S])

<i class="fa fa-arrow-right"></i> Recommandations de l'ANSSI :

- [GNU/Linux](https://www.ssi.gouv.fr/reco-securite-systeme-linux/)
  <small>(<strike>`noexec`</strike> sur `/var` pour Debian)</small>
- [(Open)SSH](https://www.ssi.gouv.fr/nt-ssh/)
