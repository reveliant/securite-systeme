---
weight: 4
---
### `seccomp`(`-bpf`)

À l'origine, `seccomp(2)` est un appel système pour jeter ses droits et se
restreindre à la manipulation de fichiers déjà ouverts (`SECCOMP_SET_MODE_STRICT`).

Effectuer un appel système autre que `exit`, `sigreturn`, `read` ou `write`
conduit à se faire tuer par le noyau.

<p><br/></p>

Le mode filtre *Berkley Packet Filter* (`SECCOMP_SET_MODE_FILTER`) permet de préciser
la liste des appels systèmes autorisés.

`seccomp-bpf` a ainsi été particulièrement utilisé par Chromium OS dont le code source
peut servir de référence d'implémentation.

<aside class="notes">

</aside>
