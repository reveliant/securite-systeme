---
weight: 2
---
| Point de<br/>montage | Options | Description |
| -------------------- | ------- | ----------- |
| `/home` | `nosuid,nodev,noexec`<br/>(`ro` optionnel) | Répertoires utilisateurs.<br/>`ro` si non utilisé.<br/>`noexec` à discuter sur station de travail |
| `/usr` | `nodev` | Majorité des utilitaires (exécutables et bibliothèques) |
| `/var` | `nosuid,nodev,noexec` | Fichiers variables pendant la vie du système (mails, BDD...) |
| `/var/log` | `nosuid,nodev,noexec` | Journaux du système |
| `/var/tmp` | `nosuid,nodev,noexec` | Fichiers temporaires conservés après extinction |