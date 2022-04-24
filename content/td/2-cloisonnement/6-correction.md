---
weight: 6
---
### Correction

Si vous avez obtenu une application opérationnelle, **félicitations** !

Sinon, pas de panique, voici des fichiers fonctionnels :

- [`cryptopy.service`](/td/cryptopy.service)
- [`apipy.service`](/td/apipy.service)
- [`nginx.conf`](/td/nginx.conf)

En complément, un [`Makefile`](/td/Makefile) avec les cibles suivantes :
<small>(nécessite évidemment `make`)</small>

- `test-dependancies` : <small>installe `python3-flask` et `httpie`</small>
- `test` : <small>teste l'application (ne nécessite pas les droits `root`)</small>
- `install-dependancies` : <small>installe `nginx uwsgi uwsgi-plugin-python3`
   `python3-flask httpie` et `netcat-openbsd`</small>
- `install` : <small>déploie, configure et teste l'application</small>
