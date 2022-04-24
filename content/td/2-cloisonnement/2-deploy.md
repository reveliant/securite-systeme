---
weight: 2
---
### Préparer le déploiement

1. Créer un groupe système (`groupadd(8)`)
2. Créer un compte de service (système, `useradd(8)`) pour chacun des deux scripts,
   en prenant garde à bien paramétrer les comptes (*home* et *shell*)
3. Déployer les scripts dans un répertoire conforme au FHS
4. Positionner le secret `key.bin` (paramétrage)
   dans un répertoire conforme au FHS et vérifier les permissions
