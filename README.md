# tarot-francais-compteur-de-points

Une simple application en python pour vous aider a compter les points de vos parties de tarot
Le chelem n'est pas encore pris en compte par l'application pour le moment.

L'application est supportee par python2 et python3.

A chaque creation d'une nouvelle partie, un fichier json est cree et peut etre reutilise ulterieurement
Dans le cas d'une continuation d'une partie deja commencee, il suffit de rentrer le nom du fichier, sans l'extension .json 

Cette application utilise des concepts elementaires de python.
N'hesitez pas a me contacter en cas de question a propos de son implementation !

Ci dessous deux exemples de rendu de l'application.

Exemple d'une partie a 4 joueurs :

```
---------------------------------------------------------------------------------------------------------------------------------------------
|     |      Contrat |   Bilan | De combien |     Preneur | Poignee | Petit au bout |    Philippe |     Valerie |        Mael |       Fanny |
---------------------------------------------------------------------------------------------------------------------------------------------
|   1 |        Garde | Reussie |         13 |    Philippe |  Simple |               |         288 |         -96 |         -96 |         -96 |
|   2 |       Petite |  Chutee |          5 |     Valerie |         |               |          30 |         -90 |          30 |          30 |
|   3 |   Garde sans |  Chutee |         10 |       Fanny |         |               |         140 |         140 |         140 |        -420 |
|   4 |   Garde sans | Reussie |         15 |        Mael |         |       Defense |        -120 |        -120 |         360 |        -120 |
|   5 |       Petite | Reussie |          4 |     Valerie |         |       Defense |         -19 |          57 |         -19 |         -19 |
---------------------------------------------------------------------------------------------------------------------------------------------
                                                                              TOTAL |         319 |        -109 |         415 |        -625 |
---------------------------------------------------------------------------------------------------------------------------------------------
```

Exemple d'une partie a 5 joueurs :

```
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|     |      Contrat |   Bilan | De combien |     Preneur |  Partenaire | Poignee | Petit au bout |    Philippe |     Valerie |        Mael |       Fanny | Jean-Pierre |
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|   1 |       Petite | Reussie |         10 |        Mael |       Fanny |         |               |         -35 |         -35 |          70 |          35 |         -35 |
|   2 |        Garde | Reussie |         10 |        Mael |       Fanny |         |               |         -70 |         -70 |         140 |          70 |         -70 |
|   3 |        Garde | Reussie |         10 |        Mael |       Fanny |         |       Attaque |         -90 |         -90 |         180 |          90 |         -90 |
|   4 |        Garde | Reussie |         10 |        Mael |       Fanny |         |       Defense |         -50 |         -50 |         100 |          50 |         -50 |
|   5 |        Garde | Reussie |         10 |        Mael |       Fanny |         |               |         -70 |         -70 |         140 |          70 |         -70 |
|   6 |        Garde | Reussie |         10 |        Mael |       Fanny |  Simple |               |         -90 |         -90 |         180 |          90 |         -90 |
|   7 |        Garde |  Chutee |         10 |        Mael |       Fanny |  Simple |               |          90 |          90 |        -180 |         -90 |          90 |
|   8 |       Petite | Reussie |         10 |        Mael |    ToutSeul |         |               |         -35 |         -35 |         140 |         -35 |         -35 |
|   9 |        Garde | Reussie |         10 |        Mael |    ToutSeul |         |               |         -70 |         -70 |         280 |         -70 |         -70 |
|  10 |        Garde | Reussie |         10 |        Mael |    ToutSeul |         |       Attaque |         -90 |         -90 |         360 |         -90 |         -90 |
|  11 |        Garde | Reussie |         10 |        Mael |    ToutSeul |         |       Defense |         -50 |         -50 |         200 |         -50 |         -50 |
|  12 |        Garde | Reussie |         10 |        Mael |    ToutSeul |         |               |         -70 |         -70 |         280 |         -70 |         -70 |
|  13 |        Garde | Reussie |         10 |        Mael |    ToutSeul |  Simple |               |         -90 |         -90 |         360 |         -90 |         -90 |
|  14 |        Garde |  Chutee |         10 |        Mael |    ToutSeul |  Simple |               |          90 |          90 |        -360 |          90 |          90 |
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                            TOTAL |        -630 |        -630 |        1890 |           0 |        -630 |
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

