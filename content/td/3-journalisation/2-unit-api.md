---
weight: 2
---
### Modifier `api.py` pour journaliser

1. Configurer de même [`app.logger`](https://flask.palletsprojects.com/en/2.2.x/logging/)
   pour [écrire vers systemd](https://github.com/systemd/python-systemd#notes)
   avec le `SYSLOG_IDENTIFIER='apipy'`

2. Reconigurer le service `systemd` pour envoyer les
  [journaux de uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/Logging.html#basic-logging-to-files)
   à la poubelle

3. Journaliser la source (`request.remote_addr`) et le corps des requêtes
   ainsi que les HMAC correspondants générés

4. Recharger et redémarrer le service et vérifier la journalisation :

   ```sh
   systemctl daemon-reload
   systemctl restart apipy.service
   journalctl -eu apipy.service
   ```
