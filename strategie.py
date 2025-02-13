from abc import ABC, abstractmethod
#classe abstract
class strategie(ABC):
    #__init__ c'est le constructeur
    #__nomdevariable__ est appelle une dundermethod
    def __init__(self, cc: int, ct: int, tc: int, tt: int) -> None:
        super().__init__()
        #constante pour savoir combien on gagne selon nos choix
        self._CC = cc
        self._CT = ct
        self._TC = tc
        self._TT = tt
        #list contenant les coups jouer par l'adversaire
        self._memoire = []
        #score obtenu au file du tournoi
        self._score = 0
        self._a_tu_coop_au_dernier_coup = None
    def getter_score(self) -> int:
        return self._score
    #->bool est juste la pour le programmeur, sert a savoir ce que renvoie la methode
    def coopére_tu(self) -> bool:
        return self._je_joue()
    # _ devant le nom d'une fontion pour dire qu'elle est interne
    @abstractmethod
    def _je_joue(self) -> bool:
        """
        méthode qui va dire ce que l'on joue suivant la stratégie implementé
        """
    def tu_as_reçu_une_coopereration(self) -> None:
        """résultat de recevoir de la coopération par rapport a votre dernier comportement"""
        self._score += self._CC if self.a_tu_coop_au_dernier_coup else self._CT

    def tu_as_été_trahi(self) -> None:
        """résultat de se faire trahir par rapport a votre dernier comportement"""
        self._score += self._TC if self.a_tu_coop_au_dernier_coup else self._TT

class gentille(strategie):
    def __init__(self, cc: int, ct: int, tc: int, tt: int) -> None:
        super().__init__(cc, ct, tc, tt)
    def _je_joue(self) -> bool:
        self.a_tu_coop_au_dernier_coup = True
        return True

class mechante(strategie):
    def __init__(self, cc: int, ct: int, tc: int, tt: int) -> None:
        super().__init__(cc, ct, tc, tt)
    def _je_joue(self) -> bool:
        self.a_tu_coop_au_dernier_coup = False
        return False

