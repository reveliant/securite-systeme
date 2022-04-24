---
weight: 3
---
### `setuid` et `setgid`

Ces deux appels systèmes changent l'utilisateur et le groupe principal du
processus :

- fait par la plupart des services *sérieux* lancés en `root`
- sinon, écrire un service systemd adapté (`systemd.exec(5)`)
- y dédier un compte de service spécifique
- y dédier un groupe spécifique à un ensemble de services

    <small>(cf. exemple ACL)</small>

Pour limiter les privilèges requis sur certaines actions sensibles,
Linux propose les `capabilities(7)`

<aside class="notes">

</aside>
