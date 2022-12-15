---
weight: 1
---
### `chroot` / `jail`

`chroot` (appel système et commande) simule une autre racine à l’intérieur du
système de fichiers

- seuls les fichiers sous la nouvelle racine seront visibles
- nécessite de recréer une arborescence FHS (`/`, `/dev`, `/proc`,
`/sys`...), et d'exposer les biliothèques nécessaires
- nécessite des privilèges élevés pour être utilisé (ou `CAP_SYS_CHROOT`), mais
    utiliser `root` ne respecte pas les moindre privilèges
    (<i class="fa fa-arrow-right"></i> `setuid`)
- *chroot is not and never has been a security tool* (Alan Cox)
- *This call [...] is not intended to be used for any kind of security purpose* (`chroot(2)`)

<aside class="notes">

`chroot` est typiquement utilisé par les systèmes d'installation (Debian, Arch Linux...)

Ce n'est **pas** un outil de sécurité et une évasion est possible sous certaines
conditions : le principe est documenté depuis 1999 et de nombreuses méthodes sont
disponibles sur Internet.

<aside>
