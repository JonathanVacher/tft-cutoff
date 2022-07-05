GNU General Public License v3.0
Jonathan Vacher (BiToP), 07/2022

This app provides the distribution of points of the player right at the cutoff. The distribution is estimated by sampling.

Nbr de joueurs : number of player participating to the tournament.
Cutoff : first player qualified to the rest of the tournament.
Nbr de game : number of game before qualification.
Attrib. des points : points attribution to players in each game from last to first.

You can run this app from a terminal by typing 

	python tft-cutoff.py

You convert this app to an executable app from a terminal by typing

	pyinstaller -F  tft-cutoff.py


[FRENCH]

Cette application donne l'histogramme du nombre de point du joueur classé à la position du cutoff. L'histogramme est estimé par tirage aléatoire répété.

Nbr de joueurs : nombre de joueurs total participant au tournoi.
Cutoff : premier joueur qualifié pour la suite du tournoi.
Nbr de game : nombre de parties avant qualification.
Attrib. des points : attribution des points lors d'une partie à 8 joueurs du dernier au premier.