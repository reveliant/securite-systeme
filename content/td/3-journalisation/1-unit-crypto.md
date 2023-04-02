---
weight: 1
---
### Modifier `crypto.py` pour journaliser

1. Installer `python3-systemd`

2. Importer `logging`, et `journal` depuis le module `systemd`

3. [Configurer](https://github.com/systemd/python-systemd#notes)
   le *logger* racine (`logging.getLogger()`) pour le `SYSLOG_IDENTIFIER='cryptopy'`

4. Utiliser `logging.info()` pour journaliser proprement les messages à la place
   des `print()`

5. Redémarrer le service et vérifier la journalisation :

   ```sh
   systemctl restart cryptopy.service
   journalctl -eu cryptopy.service
   ```
