---
weight: 3
---
### Configurer `journald`

1. Reconfigurer les deux services systemd avec `cryptosrv` comme
   [espace de nom de journalisation](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#LogNamespace=)

2. [Configurer](https://www.freedesktop.org/software/systemd/man/journald.conf.html)
   cet espace de nom dans le fichier adéquat:

    - fixer la [politique de rotation](https://www.freedesktop.org/software/systemd/man/journald.conf.html#MaxFileSec=)
      à 1 jour
    - fixer la [politique de rétention](https://www.freedesktop.org/software/systemd/man/journald.conf.html#MaxRetentionSec=)
      7 jours
    - activer l'export [vers syslog](https://www.freedesktop.org/software/systemd/man/journald.conf.html#ForwardToSyslog=)

3. Redémarrer les services et vérifier les journaux :

   ```sh
   systemctl daemon-reload
   systemctl start systemd-journald@cryptosrv.service
   systemctl restart cryptopy.service apipy.service
   journalctl -e --namespace=cryptosrv
   ```
