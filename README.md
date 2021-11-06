# InvasivePlantsSraper

## Biodiversitat arbustiva i arbòria nativa i invasora a Espanya
## Descripció
El conjunt de dades inclou les espècies de arbustos i arbres a les diferents regions d’Espanya recollides en l’Inventari forestal definint si són o no invasores, és a dir, incloses al catàleg d’espècies exòtiques invasores del Ministeri.

## Context
Les espècies invasores constitueixen una de les principals causes de la biodiversitat a nivell mundial. Malgrat la seva definició a nivell legal a través del catàleg espanyol d’espècies exòtiques invasores, no existeixen mapes actuals i actualitzables de la presència d’aquestes espècies en el territori. No obstant, l'Inventari forestal nacional (IFN) és el projecte que proporciona informació a nivell nacional de l'estat dels boscos. La seva metodologia es basa en la presa de dades en parcel·les resultants d'un mostreig estratificat realitzat en la superfície forestal arbrada. Aquests inventaris es solen renovar amb certa periodicitat (cada 10 anys), actualment les dades més recents publicades són les de l'IFN3 i s'està realitzant l'IFN4. Les dades obtingudes en els inventaris de camp estan, en part, informatitzades en bases de dades, a nivell de provincia, descarregables desde la web institucional. Així doncs, relacionant les dades de l’IFN3 i el llistat d’espècies invasores, el dataset creat permet relacionar el llistat d’espècies exòtiques invasores amb els inventaris forestals de les diferents regions d’Espanya, permetent així el càlcul de biodiversitat nativa i invasora per regions, i per tant la delimitació de punts d’atenció especial pel que fa a la gestió d’aquestes espècies.

## Enllaços:
El dataset reduit es troba penjat a Zenodo (https://zenodo.org/record/5616003#.YXvboJuxVl8) amb el DOI:  10.5281/zenodo.5616003.

El dataset complet es troba a: https://drive.google.com/file/d/1rPzM_QDatn4CJlSQ8YUtH8UVGsesFTsN/view?usp=sharing 

Inventari forestal: https://www.miteco.gob.es/es/biodiversidad/servicios/banco-datos-naturaleza/informacion-disponible/ifn3_bbdd_descargas.htm.aspx

Llistat plantes invasores: https://www.miteco.gob.es/es/biodiversidad/temas/conservacion-de-especies/especies-exoticas-invasoras/ce_eei_flora.aspx

## Membres de l'equip
Erola Fenollosa i Xavier Pascuet

## Fitxers
- MemòriaPRA1.pdf: Conté les respostes als apartats demanats a la PRA1 amb descripció i context del dataset així com descripció del contingut, inspiració, agraïments i llicència.
- ifn3_invasives.py: Conté el codi per a fer web scraping a l'Inventari Forestal i el llistat de flora invasora.
- codi_espècies.csv: Relació dels codis utilitzats en l'Inventari forestal Nacional i el nom científic de les espècies.
