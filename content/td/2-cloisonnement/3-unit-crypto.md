---
weight: 3
---
### Écrire le service systemd pour `crypto.py`

1. Créer un service systemd pour lancer `crypto.py`
   <small>(voir [`systemd.service(5)`](https://www.freedesktop.org/software/systemd/man/systemd.service.html)
   et [`systemd.exec(5)`](https://www.freedesktop.org/software/systemd/man/systemd.exec.html))</small>

   - le service doit utiliser son compte de service et son groupe
   - `SOCKET_PATH` et `KEY_PATH` doivent être paramétrées dans l'environnement
   - la socket devra être créée avec les bonnes permissions (*umask*)
     dans un répertoire géré par le service systemd sous `/run`

2. Charger et lancer le service :

   ```sh
   systemctl daemon-reload
   systemctl start <xyz>.service
   ```

3. Vérifier les permissions sur le répertoire sous `/run` et la socket
4. Tester le service :

   ```sh
   echo "Hello world" | nc -U /run/.../xyz.sock | xxd
   ```
