---
weight: 2
---
### Modifier `api.py` pour journaliser

1. Configurer de même [`app.logger`](https://flask.palletsprojects.com/en/2.2.x/logging/)
   pour [écrire vers systemd](https://github.com/systemd/python-systemd#notes)
   avec le `SYSLOG_IDENTIFIER='apipy'`

2. Journaliser la source <small>(`request.remote_addr`)</small>
   et le corps des requêtes ainsi que les HMAC correspondants générés

3. Redémarrer le service et vérifier la journalisation :

   ```sh
   systemctl restart apipy.service
   journalctl -eu apipy.service
   ```
