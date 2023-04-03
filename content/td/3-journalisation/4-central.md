---
weight: 4
---
### Configurer le serveur de centralisation

Sur le second serveur :

1. Configurer `rsyslog` pour :
   - écouter en RELP
     ([`imrelp`](https://www.rsyslog.com/doc/v8-stable/configuration/modules/imrelp.html))
   - enregistrer les journaux dans un fichier
     ([`omfile`](https://www.rsyslog.com/doc/v8-stable/configuration/modules/omfile.html#action-parameters))
     avec le nom du serveur source et la date [dans le nom du fichier](https://www.rsyslog.com/doc/v8-stable/configuration/templates.html#string)

2. Redémarrer `rsyslog` :

   ```sh
   systemctl restart rsyslog.service
   ```

3. Générer des journaux et vérifier leur centralisation

<aside class="notes">

Pour assurer le nettoyage :

1. Créer un service `systemd` pour effacer les vieux journaux
   et un *timer* `systemd` pour l'activer quotidiennement :

   ```bash
   /usr/bin/find /var/log/<xyz>/ -mtime +30 -name "*.log" -print -delete
   ```

2. Recharger, activer et démarrer le *timer* :

   ```sh
   systemctl daemon-reload
   systemctl enable <xyz>.timer
   systemctl start <xyz>.timer
   ```

</aside>
