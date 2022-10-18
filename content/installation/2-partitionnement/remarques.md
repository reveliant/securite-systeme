---
weight: 4
---
- `nodev` empêche de jouer avec les **fichiers spéciaux** pour accéder sans droit
    ni titre à une partition autrement protégée (avec `mknod` utilisé par exemple
    sur une clé USB) :

    ```console
    brw-rw---- 1 root disk     8,   0 18 mars  16:29 sda
    brw-rw---- 1 root disk     8,   1 18 mars  16:29 sda1
    brw-rw---- 1 root disk     8,   2 18 mars  16:29 sda2
    brw-rw---- 1 root disk     8,   3 18 mars  16:29 sda3
    ```

- `/var/log` peut vous exploser à la figurer et bloquer le
    démarrage d'applications (comme X.org)
