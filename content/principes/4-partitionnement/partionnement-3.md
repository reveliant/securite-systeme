---
weight: 3
---
| Point de<br/>montage | Options | Description |
| -------------------- | ------- | ----------- |
| `/opt` | `nosuid,nodev`<br/>(`ro` optionnel) | Packages additionnels.<br/>`ro` si non utilisé |
| `/srv` | `nosuid,nodev`<br/>(`noexec,ro` optionnels) | Fichiers servis par un service |

D'après les [Recommandations de sécurité relatives à un système GNU/Linux](https://www.ssi.gouv.fr/reco-securite-systeme-linux/), ANSSI

<p><br/></p>

<small>Nota : utiliser correctement le système de fichier et se référer au
[*Filesystem Hierarchy Standard*](https://refspecs.linuxfoundation.org/fhs.shtml), `hier(7)`</small>