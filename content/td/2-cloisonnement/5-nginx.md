---
weight: 5
---
### Configurer Nginx

1. Configurer Nginx pour communiquer avec la *socket* uWSGI
   <small>(voir [documentation Flask](https://flask.palletsprojects.com/en/2.1.x/deploying/uwsgi/#configuring-nginx))</small>

   ```nginx
   location / { try_files $uri @cryptosrv; }
   location @cryptosrv {
       include uwsgi_params;
       uwsgi_pass unix:/run/.../uwsgi.sock;
   }
   ```

2. Redémarer Nginx et tester l'application :

   ```sh
   systemctl restart nginx.service
   http --json POST :/hmac data="Hello World"
   ```
