# InvasivePlantsSraper

## Biodiversitat arbustiva i arbòria nativa i invasora a Espanya
## Descripció
El conjunt de dades inclou les espècies de arbustos i arbres a les diferents regions d’Espanya recollides en l’Inventari forestal definint si són o no invasores, és a dir, incloses al catàleg d’espècies exòtiques invasores del Ministeri.

## Context
Les espècies invasores constitueixen una de les principals causes de la biodiversitat a nivell mundial. Malgrat la seva definició a nivell legal a través del catàleg espanyol d’espècies exòtiques invasores, no existeixen mapes actuals i actualitzables de la presència d’aquestes espècies en el territori. El dataset creat permet relacionar el llistat d’espècies exòtiques invasores amb els inventaris forestals de les diferents regions d’Espanya, permetent així el càlcul de biodiversitat nativa i invasora per regions, i per tant la delimitació de punts d’atenció especial pel que fa a la gestió d’aquestes espècies. 

L'Inventari forestal nacional (IFN) és el projecte que proporciona informació a nivell nacional de l'estat dels boscos. La seva metodologia es basa en la presa de dades en parcel·les resultants d'un mostreix estratificat realitzat en la superfície forestal arbrada. Aquestos inventaris es solen renovar-se amb certa periodicitat (cada 10 anys), actualment les dades mes recents publicades són les de l'IFN3 i s'està realitzant l'IFN4.
Les dades obtingudes en els inventaris de camp estan, en part, informatitzades en bases de dades, a nivell de provincia, descarregables des de la web institucional.

## Contingut 
Estadillo: Tipus Enter. Identificador de la parcel·la.
Cla: tipus String. Codi que determina si la parcel·la ja estava a l’IFN2, o si s’inventaria per primera vegada.
Subclasse: Tipus String. Codi que determina el tipus de parcel·la
nArbol: Tipus enter. Número de l’arbre dins de la parcel·la
OrdenIf3: Tipus enter. Número d’ordre de l’arbre en l’IFN3.
OrdenIf2: Tipus enter. Número d’ordre de l’arbre en l’IFN2.
Rumbo: Tipus enter. Angle que formen la direcció nord i la linea que uneix arbre i centre de la parcel·la. En sentit de les agulles del rellotge.
Distanci: Tipus numèric. Distància en metres al centre de la parcel·la.
Dn1: Diàmetre normal del arbre apuntant al centre de la parcel·la, en milímetres.
Dn2: Diàmetre normal del arbre en direcció perpendicular a l’anterior, en milímetres.
Hf: Tipus numèric, alçada total de l’arbre en metres.
Calidad: Tipus enter. Codifica la qualitat de l’arbre. Pot ser:
  1: Arbre sa, vigorós òptimament conformat ambg excelents perspectives de futur, capaç de proporcionar productes valuosos.
  2: Arbre sa, vigorós, no dominat amb algun defecte de conformació, capaç de proporcionar productes valuosos.
  3: Arbre no ttotalment sa i vigoros, vell o dominat pero capaç de proporcionar productes valuosos
  4: Arbre malalt i dèbil o vell, amb molts defectes de conformació, capaç de proporcionar productes de valor secundari
  5: Arbre molt malat, dèbil o vell, amb pèssima conformació y aprofitaments d’escas valor.
  6: Arbre mort pero sense podrir.
Forma: Tipus enter. Codificac la forma de l’arbre.
  1: Arbres fusiformes en quasi la totalitat del troncm troncs fustaners de més de 6mm i diàmetre normal major de 20 cm.
  2: Arbres fusiformes, amb troncs fustaners de 4 metres o més, que no petanyen a la forma 1
  3: Arbres fusiformes petits, en els que el diàmetre de 75mm queda per sota els 4 metres d’alçada.
  4: Arbres amb el tronc ramificat abans dels 4 metres d’alçada.
  5: Arbres amb el tronc principal tortuos, sanyat o amb moltes rames.
  6: Arbres escapçats.
ParEsp: Tipu ester. Parametres especials. Codifica la qualitat de suros o resines.
Agente: Tipus enter. Codifica l’agent causant del dany. Pot ser:
  100: Sense danys
  200: Cause desconegudes
  310: Fongs
  311: Insectes
  312: Vesc
  313: Plantes epífites
  314: Fauna silvestre
  315: Bestiar
  320: Maquinària
  321: Treta de fusta
  322: Home en general
  410: Neu
  411: Vent
  412: Sequera
  413: LLamp
  414: Gelades
  415: Calamarsa
  421: Foc
  422: Despreniments
  423: Erosió
Import: Tipus enter. Codifica la importància del dany. Pot ser:
  1: Petita
  2: Mitjana
  3: Gran
Elemento: Tipus Enter. Codi referent a l’element danyat. Pot ser:
  1: Escorça
  2: Fulles
  3: Rames
  4: Tronc
  5: Fruits
  6: Flors
  7: Guía terminal
  8: Copa
  9: Arbre sencer
Provincia: Tipus Enter. Codi de la provincia de la parcel·la d'inventari
Is_invasives: Tipus Text. Pren "Yes" o "No" segons si la espècie es invasora 

## Enllaços:
https://zenodo.org/record/5616003#.YXvboJuxVl8 :Versió reduïda del dataset obtingut

Inventari forestal: https://www.miteco.gob.es/es/biodiversidad/servicios/banco-datos-naturaleza/informacion-disponible/ifn3_bbdd_descargas.htm.aspx
Llistat plantes invasores: https://www.miteco.gob.es/es/biodiversidad/temas/conservacion-de-especies/especies-exoticas-invasoras/ce_eei_flora.aspx

## Membres de l'equip
Erola Fenollosa i Xavier Pascuet

## Fitxers
- ifn3_invasives.py: Conté el codi per a fer web scraping a l'Inventari Forestal i el llistat de flora invasora.
- codi_espècies.csv: Relació dels codis utilitzats en l'Inventari forestal Nacional i el nom científic de les espècies
