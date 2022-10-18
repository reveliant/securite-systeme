---
weight: 2
---
### Configuration système

- Partitionner finement
- N'installer que le **strict minimum** nécessaire

    <small>Pas d'interface graphique sur un serveur !</small>
- Durcir les options noyau (`sysctl`)
- Durcir le système (règles `sudoers` granulaires...)
- Durcir les services (empêcher les connexions `root` sur SSH...)
- Filtrer les accès (Netfilter `iptables` / `nftables`)
- Mot de passe `root` complexe et spécifique à ce système

    <small>Au coffre-fort ou dans un gestionnaire de mot de passe</small>
