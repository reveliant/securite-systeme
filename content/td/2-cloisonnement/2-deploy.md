---
weight: 2
---
### Préparer le déploiement

1. Déployer les scripts dans un répertoire conforme au FHS (par exemple `/opt/cryptosrv`)
2. Créer un groupe système (`groupadd(8)`)
3. Créer un compte de service (système, `useradd(8)`) pour chacun des deux scripts,
   en prenant garde à bien paramétrer les comptes (répertoire des scripts comme *home*
   et `nologin(8)` comme *shell*)
4. Positionner le secret `key.bin` (paramétrage / configuration)
   dans un répertoire conforme au FHS et vérifier les permissions
