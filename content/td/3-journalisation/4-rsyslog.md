---
weight: 4
---
### Relayer `journald` avec `rsyslog`

1. Configurer `rsyslog` pour :
   - enregistrer localement ([`omfile`](https://www.rsyslog.com/doc/v8-stable/configuration/modules/omfile.html#action-parameters))
     les journaux de `cryptopy` et `apipy`,
     avec le `programname` puis la date [dans le nom du fichier](https://www.rsyslog.com/doc/v8-stable/configuration/templates.html#string)
   - et les relayer en RELP ([`omrelp`](https://www.rsyslog.com/doc/v8-stable/configuration/modules/omrelp.html))
     vers un second serveur

2. Redémarrer `rsyslog` :

   ```sh
   systemctl restart rsyslog.service
   ```
