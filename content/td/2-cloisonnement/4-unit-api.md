---
weight: 4
---
### Écrire le service systemd pour `api.py`

1. Créer un service systemd pour lancer `api.py` avec uWSGI
   <small>(`uwsgi-core(1)` et [documentation Flask](https://flask.palletsprojects.com/en/2.1.x/deploying/uwsgi/#starting-your-app-with-uwsgi))</small>

   - le service doit utiliser son compte de service et les groupes nécessaires
     pour communiquer avec le service cryptographique et Nginx
   - `SOCKET_PATH` doit être paramétrée dans l'environnement
   - une socket, accessible à Nginx, doit être créée  dans un répertoire
     géré par le service systemd sous `/run`

2. Charger et lancer le service :

   ```sh
   systemctl daemon-reload
   systemctl start <xyz>.service
   ```

3. Vérifier les permissions sur le répertoire sous `/run` et la socket
