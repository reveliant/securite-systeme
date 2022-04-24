---
weight: 1
---
### Tester l'application

1. Télécharger (`wget`...) les scripts [`api.py`](/td/api.py) et [`crypto.py`](/td/crypto.py)
2. Générer un secret et paramétrer les composants :

   ```sh
   openssl rand -out key.bin 16
   export KEY_PATH=key.bin
   export SOCKET_PATH=crypto.sock
   export FLASK_APP=api.py
   ```

3. Lancer les services :

   ```sh
   python3 crypto.py & echo $! > crypto.pid
   flask run & echo $! > api.pid
   ```

4. Tester les services :

   ```sh
   http --json POST :5000/hmac data="Hello World"
   ```
