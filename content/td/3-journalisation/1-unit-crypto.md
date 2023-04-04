---
weight: 1
---
### Modifier `crypto.py` pour journaliser

1. Installer `python3-systemd`

2. Importer les modules Python nécessaires :

   ```python
   import logging
   from systemd import journal
   ```

3. [Configurer](https://github.com/systemd/python-systemd#notes)
   le *logger* racine (`logging.getLogger()`) pour le `SYSLOG_IDENTIFIER='cryptopy'`
   à partir du niveau `logging.INFO`

4. Utiliser `logging.info()` pour journaliser proprement les messages à la place
   des `print()`

5. Redémarrer le service et vérifier la journalisation :

   ```sh
   systemctl restart cryptopy.service
   journalctl -eu cryptopy.service
   ```
