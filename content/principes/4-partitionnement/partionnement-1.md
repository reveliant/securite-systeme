---
weight: 1
---
| Point de<br/>montage | Options | Description |
| -------------------- | ------- | ----------- |
| `/` | <sans option> | Racine, contient le reste |
| `/boot` | `nosuid,nodev,noexec`<br/>(`noauto` optionnel) | Contient le noyau et le bootloader, pas d’accès après démarrage sauf mise à jour |
| `/tmp` | `nosuid,nodev,noexec` | Fichiers temporaires, ne doit pas contenir d'exécutables.<br/> Nettoyé après redémarrage, préférer du `tmpfs` |
| `/proc` | `hidepid=2` | Informations sur les processus et le système |
