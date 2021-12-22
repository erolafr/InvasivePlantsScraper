PRA2
================
Erola Fenollosa i Xavier Pasquet
22 desembre de 2021

# MEMÒRIA PRA2

### 0. Introducció

Aquest arxiu conté els apartats de la memòria de la **PRA2** juntament amb el codi per a respondre a les preguntes. Per tant el punt 7 de la memòria queda integrat en aquest mateix arxiu.

### 1. Descripció del dataset. Perquè és important i quina pregunta/problema pretén respondre?

descripció dataset perquè és important

Tal i com presentavem en la PRA1 (<https://github.com/erolafr/InvasivePlantsScraper/blob/main/Mem%C3%B2riaPRA1.pdf>), el dataset “Biodiversitat arbustiva i arbòria nativa i invasora a Espanya”.

Preguntes: Biodiversitat i riquesa nativa i invasora en les diferents regions. Rànquing de províncies amb més diversitats i riquesa. Correlació entre biodiversitat i riquesa nativa i invasora. Qualitat de l’arbrat i la seva relació amb la biodiversitat,i riquesa tant nativa com invasora.

Explicar hipotesis i conceptes: indexs, què signifiquen les variables…

### 2. Integració i selecció de les dades d’interès a analitzar.

Importem el csv:

``` r
ifn3 <- read.csv("ifn3.csv")
```

Revisió de quines variables hi ha i fer subset d’algunes

``` r
#Revisem l'estructura global del dataset importat
str(ifn3)
```

    ## 'data.frame':    1264270 obs. of  20 variables:
    ##  $ Estadillo  : int  1 1 1 1 1 1 5 5 5 5 ...
    ##  $ Cla        : chr  "A" "A" "A" "A" ...
    ##  $ Subclase   : chr  "1" "1" "1" "1" ...
    ##  $ nArbol     : int  1 2 3 4 5 6 1 2 3 4 ...
    ##  $ OrdenIf3   : int  1 2 3 4 5 6 1 2 3 4 ...
    ##  $ OrdenIf2   : int  0 0 0 0 0 0 0 0 0 0 ...
    ##  $ Rumbo      : int  4 20 44 149 170 25 1 8 31 37 ...
    ##  $ Distanci   : num  2 15.4 8 7.5 8.8 ...
    ##  $ Especie    : chr  "Eucalyptus globulus" "Eucalyptus globulus" "Eucalyptus globulus" "Eucalyptus globulus" ...
    ##  $ Dn1        : int  136 314 151 154 155 141 209 240 260 244 ...
    ##  $ Dn2        : int  145 352 153 148 167 147 201 238 222 205 ...
    ##  $ Ht         : num  10 18 11.5 11.5 14 12.5 22.5 22.5 25 23 ...
    ##  $ Calidad    : int  2 2 2 2 2 2 2 2 2 2 ...
    ##  $ Forma      : int  2 2 2 2 2 2 2 2 2 2 ...
    ##  $ ParEsp     : int  NA NA NA NA NA NA NA NA NA NA ...
    ##  $ Agente     : int  100 100 100 100 100 100 100 100 100 100 ...
    ##  $ Import     : int  NA NA NA NA NA NA NA NA NA NA ...
    ##  $ Elemento   : int  NA NA NA NA NA NA NA NA NA NA ...
    ##  $ Provincia  : int  48 48 48 48 48 48 48 48 48 48 ...
    ##  $ Is_invasive: chr  "No" "No" "No" "No" ...

``` r
library(dplyr)
```

    ## Warning: package 'dplyr' was built under R version 4.0.4

    ## 
    ## Attaching package: 'dplyr'

    ## The following objects are masked from 'package:stats':
    ## 
    ##     filter, lag

    ## The following objects are masked from 'package:base':
    ## 
    ##     intersect, setdiff, setequal, union

``` r
# Seleccionem les variables d'interès
ifn3_subset <- select(ifn3, c(Estadillo, Especie, Calidad, Provincia, Is_invasive))

# Visualitzem el dataset filtrat:
head(ifn3_subset)
```

    ##   Estadillo             Especie Calidad Provincia Is_invasive
    ## 1         1 Eucalyptus globulus       2        48          No
    ## 2         1 Eucalyptus globulus       2        48          No
    ## 3         1 Eucalyptus globulus       2        48          No
    ## 4         1 Eucalyptus globulus       2        48          No
    ## 5         1 Eucalyptus globulus       2        48          No
    ## 6         1 Eucalyptus globulus       2        48          No

### 3. Neteja de les dades.

#### 3.1. Les dades contenen zeros o elements buits? Com gestionaries aquests casos?

Comptabilitzar casos amb zeros o elements buits en valor absolut i en percentatge per cada variable

``` r
colSums(is.na(ifn3_subset))
```

    ##   Estadillo     Especie     Calidad   Provincia Is_invasive 
    ##           0           0        2525           0           0

Discutir què fer i eliminar en funció de la variable

#### 3.2. Identificació i tractament de valors extrems.

generar histogrames per a atributs numerics i frequencia de casos en categorics.

Discutir què fer amb valors extrems

### 4. Anàlisi de les dades.

#### 4.1. Selecció dels grups de dades que es volen analitzar/comparar (planificació dels anàlisis a aplicar).

En primer lloc, creació de noves variables per provincia (nou dataset per provincia)

``` r
#riquesa per provincia
#indexs de biodiversitat per provincia
```

Indexs: Simpson, Shannon, Margalef.

per la variable de qualitat farem la mitjana de la província i també error estàndard.

Creació de grups depen de si tenen invasores o no, en cada parcela mirar si té alguna invasora o cap i agrupar en una variable. Variable que sigui “conté invasora”.

#### 4.2. Comprovació de la normalitat i homogeneïtat de la variància.

comprovem normalitat:

comprovem homogeneitat de variancies:

comentem resultats.

#### 4.3. Aplicació de proves estadístiques per comparar els grups de dades. En funció de les dades i de l’objectiu de l’estudi, aplicar proves de contrast d’hipòtesis, correlacions, regressions, etc. Aplicar almenys tres mètodes d’anàlisi diferents.

Contrast d’hipotesis de si les parceles amb alguna invasora tenen millor qualitat o menys biodiversitat que les que no.

Correlació entre biodiversitat nativa de la provincia i la biodiversitat invasora de la provincia

Correlació entre biodiversitat invasora i qualitat de l’arbrat

### 5. Representació dels resultats a partir de taules i gràfiques.

resultats de riquesa i biodiversitat per provincia

ranquing per provincia

taula anova, p-valors del contrast d’hipotesi

grafics de correlacions

### 6. Resolució del problema. A partir dels resultats obtinguts, quines són les conclusions? Els resultats permeten respondre al problema?

Conclusions. Redactar.

### 7. Codi: Cal adjuntar el codi, preferiblement en R, amb el que s’ha realitzat la neteja, anàlisi i representació de les dades. Si ho preferiu, també podeu treballar en Python

Explicar que el codi està aquí

### Taula de contribucions:

Contribucions Firma Investigació prèvia

Redacció de les respostes

Desenvolupament del codi
