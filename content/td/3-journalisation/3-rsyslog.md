---
weight: 3
---
### Configurer `rsyslog`

1. Vérifier que les journaux de `cryptopy` et `apipy` remontent
   dans `/var/log/messages` via `rsyslog`.

2. Configurer `rsyslog` pour :
   - enregistrer localement ([`omfile`](https://www.rsyslog.com/doc/v8-stable/configuration/modules/omfile.html#action-parameters))
     les journaux de `cryptopy` et `apipy`,
     avec `programname` puis la date (les 10 premiers caractères du format `date-rfc3339`)
     [dans le nom du fichier](https://www.rsyslog.com/doc/v8-stable/configuration/templates.html#string)
   - et les relayer en RELP ([`omrelp`](https://www.rsyslog.com/doc/v8-stable/configuration/modules/omrelp.html))
     vers un second serveur
   - relayer de même les *facilities* `auth` et `authpriv`

3. Redémarrer `rsyslog` :

   ```sh
   systemctl restart rsyslog.service
   ```
