# Path of Exile `.dat` Data Splitter

This directory contains some source data extracted from the game's files. All data was retrieved using Alexander Drozdov's neat [poe-dat-viewer tool](https://snosme.github.io/poe-dat-viewer/).

I then take the extracted data, export it to `.json` files (in this `data` directory), and have some Python scripts that manually split these large files into their own separate domains.

For mods - the domains vary widely (we're mainly interested in the first domain, the item modifiers). For item base types, the domaims also vary widely (we're mainly interested in gear base types).
