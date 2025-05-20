# Reflectie Van Nick Reul

## Algemene uitleg over het project

- ### Apparaten

  - Ik dacht aan de status als een soort van toestand dat het toestel word aangepast. Dus als een lamp aan staat mag de helderheid worden aangepast.

- ### Html

  - Voor de html werk ik met een jinja template die in templates zit. De html zit in \_site. In deze folder staat css al klaar voor wanneer de html binnenkomt.

- ### Nacht en dag cyclus

  - In de dag is alles heel actief. Er word gereageert op de bewoners. Maar bepaalde apparaten zijn enkel afhankelijk van de dag of nacht cyclus.

  - In de nacht worden alle apparaten uit gezet behalve rookmelders. (die moeten nog steeds kunnen detecteren.)

- ### Loging

  - Er word bij elke verandering van een apparaat door het apparaat zelf gelogt aan de hand van de logger. Zo staan alle logging's mooi per apparaat en kan een apparaat verwijderd worden indien nodig.

- ### Brandoefening

  - 1/10 000 kans per kamer dat er brand ontstaat. Dan verlaten eerst alle bewoners het gebouw, daarna worden alle toestellen uit gezet. De applicatie word dan wel gestopt.

- ### Ai klasse
  - Het idee van deze klasse is dat hij data kan maken, verzamelen, en verwerken. Mijn idee was om de data van bewoners te verzamelen en te zien welke bewoner welke kamer het meeste bezoekt.
    In het echt zou dit aan de bewegingsensors gekoppelt worden en niet aan de bewoners zoals mijn applicatie. Maar ik heb hier geen classificatiemodel aan verbonden.

## Opstarten van het project

1. Ga naar de directory -> cd .\codebestanden\
1. Environment klaar zetten.

   - microsoft

     1. python -m venv venv
     1. .\venv\scripts\activate
     1. pip install -r .\requirements.txt

   - mac
     1. python3 -m venv venv
     1. source venv/bin/activate
     1. pip install -r requirements.txt

1. Project starten -> python app.py
1. Start tijd van het programma ( vb: 18:00 of 23:00 )
1. Snelheid kiezen van 1 stap ( in seconden )

## Problemen die ik ondervond

- ### opstart van het project

  ik vond het best moeilijk om te starten aan zoon project. Ik ben uiteindelijk begonnen aan aan als eersten alle nodige klassen te maken. van daar ben ik dan naar de smarthub en html logger + jinja gegaan om al iets op beeld te krijgen. Ben zo dan wel soepel verder gegaan en weet dat ik in het vervolg sneller een begin to endpoint moet maken en daarin uitbreiden.

- ### De structuur

  In het begin wist ik niet waar ik naar toe moest gaan in zin van klassen opbouw. Ik was wel vastberaden om het met containerklassen te doen en dat is goed gelukt.

- ### Opslagstructuur apparaten

  In het vervolg zou ik mijn klassen niet in een lijst maar dictionary opslaan zo kan ik veel sneller en handiger alle apparaten zoeken/regelen.

- ### Data ophalen (Ai klasse)

  Ik vond het best moeilijk om te begrijpen hoe ik de data die ik nu heb om te vormen naar json.

## Wat ik er van vond

Ik vond het echt een heel leuke opdracht. En dit is niet om u perse blij te maken (zou leuk zijn als dat ook is megenomen) maar had echt plezier aan dit te maken. Heb er echt men eigen projectje van kunnen maken, ik heb onderandere mijn eigen appartement nagebouwd en de bewoners zijn mijn ouders, zusje en ik.

## wat ik hier uit wil menemen

de belangrijkste dingen die ik zeker wil onthouden zijn.

1. Van het begin naar einde eerst iets klein starten en dan uitbreiden.

1. Om andere datastructuren in gedachte te houden.

1. En de ervaring van dit project, want dit was de eerste keer dat ik echt aan iets groot heb gewerkt.
