KEY_PATH = key.bin
SOCKET_PATH = crypto.sock
TEST_PIDS = crypto.pid api.pid

FINAL_KEY_PATH = /etc/cryptosrv/key.bin
FINAL_BIN_PATH = /opt/cryptosrv/

SCRIPTS = crypto.py api.py
SERVICES = cryptopy.service apipy.service
SYSTEMD_UNITS = /etc/systemd/system/

FILES_WEBROOT = https://securite-systeme.rdubois.fr/td

all: test install

# Vérifie un UID 0
check-root:
	@echo "Vérification de l'exécution en UID 0"
	test `id -u` -eq 0

# Génération d'un secret si aucun déja créé
$(KEY_PATH):
	@echo "Génération d'un secret"
	openssl rand -out $@ 16

# Télécharge les scripts, services et configurations si nécessaire
download:
	test -f crypto.py || wget $(FILES_WEBROOT)/crypto.py
	test -f api.py || wget $(FILES_WEBROOT)/api.py
	test -f cryptopy.service || wget $(FILES_WEBROOT)/cryptopy.service
	test -f apipy.service || wget $(FILES_WEBROOT)/apipy.service
	test -f nginx.conf || wget $(FILES_WEBROOT)/nginx.conf

#
# TESTS
#

# Installe les dépendances APT pour les test
test-dependancies: check-root
	echo "Installation des dépendances et utilitaires"
	apt install python3-flask httpie

# Lance les services, exécute le test et arrête les services
test: download start
	@echo "Test des services"
	http --json POST :5000/hmac data="Hello world"
	$(MAKE) stop

# Lance les services de test
start: $(TEST_PIDS)

# Service cryptographique
crypto.pid: $(KEY_PATH)
	@echo "Lancement du service cryptographique"
	test ! -f $(SOCKET_PATH) || rm $(SOCKET_PATH)
	KEY_PATH=$(KEY_PATH) SOCKET_PATH=$(SOCKET_PATH) python3 crypto.py & echo $$! > crypto.pid
	sleep 1

# Service d'API Flask
api.pid: crypto.pid
	@echo "Lancement du service Flask"
	FLASK_APP=api.py SOCKET_PATH=$(SOCKET_PATH) flask run & echo $$! > api.pid
	sleep 1

# Arrête les services de test
stop:
	@echo "Arrêt des services et nettoyage"
	kill `cat api.pid` && rm api.pid
	kill `cat crypto.pid` && rm crypto.pid
	rm $(SOCKET_PATH)

#
# INSTALLATION
#

install: download check-root install-dependancies create-users deploy-files services-start nginx services-test services-stop

uninstall: services-stop remove-users remove-files

# Installe les dépendances APT
install-dependancies:
	echo "Installation des dépendances et utilitaires"
	apt install nginx uwsgi uwsgi-plugin-python3 python3-flask httpie netcat-openbsd

# Crée le groupe et les utilisateurs
create-users:
	@echo "Création du groupe et des utilisateurs"
	groupadd --system cryptosrv
	useradd --system --home-dir /opt/cryptosrv --no-create-home --gid cryptosrv --no-user-group --shell /usr/sbin/nologin cryptopy
	useradd --system --home-dir /opt/cryptosrv --no-create-home --gid cryptosrv --no-user-group --shell /usr/sbin/nologin apipy

# Supprime les utilisateurs et le groupe
remove-users:
	@echo "Suppresion des utilisateurs et du groupe"
	userdel cryptopy
	userdel apipy
	groupdel cryptosrv

# Déploie les fichiers
deploy-files: $(FINAL_KEY_PATH) $(SCRIPTS:%=$(FINAL_BIN_PATH)%) $(SERVICES:%=$(SYSTEMD_UNITS)%)

# Supprime les fichiers
remove-files: $(SCRIPTS:%=$(FINAL_BIN_PATH)%) $(SERVICES:%=$(SYSTEMD_UNITS)%)
	rm $^

# Déplace le secret et corrige les permissions
$(FINAL_KEY_PATH): $(KEY_PATH)
	mkdir -p $(basename $(FINAL_KEY_PATH))
	mv $(KEY_PATH) $(FINAL_KEY_PATH)
	chown cryptopy $(FINAL_KEY_PATH)
	chmod u=r,g=,o= $(FINAL_KEY_PATH)

# Déploie un script Python
$(FINAL_BIN_PATH)%.py: %.py
	test -d $(FINAL_BIN_PATH) || mkdir -p $(basename $(FINAL_BIN_PATH))
	cp $< $@

# Déploie un service systemd
$(SYSTEMD_UNITS)%.service: %.service
	cp $< $@
	systemctl daemon-reload

# Lance les services
services-start: $(SERVICES:%=$(SYSTEMD_UNITS)%)
	systemctl start $(SERVICES)
	systemctl status --no-pager $(SERVICES)

# Arrête les services
services-stop: $(SERVICES:%=$(SYSTEMD_UNITS)%)
	systemctl stop $(SERVICES)

# Déploie la configuration Nginx
nginx: nginx.conf
	test ! -L /etc/nginx/sites-enabled/default || rm /etc/nginx/sites-enabled/default
	cp nginx.conf /etc/nginx/sites-available/cryptosrv
	test -L /etc/nginx/sites-enabled/cryptosrv || ln -sr /etc/nginx/sites-available/cryptosrv /etc/nginx/sites-enabled/
	systemctl restart nginx.service

# Teste les services
services-test:
	echo "Hello world" | nc -U /run/cryptosrv/crypto.sock | xxd
	http --json POST :/hmac data="Hello world"
