import strategie
class tournoi:
    def __init__(self) -> None:
        """
        Constructeur
        """
    def duel(self,strat1: strategie, strat2: strategie, nb_tour: int) -> None:
        """
        Fais s'affronter deux strategie nb_tour fois
        """
        for i in range(nb_tour-1):
            strat1_a_cooperer = strat1.coopére_tu()
            strat2_a_cooperer = strat2.coopére_tu()
            if strat2_a_cooperer :
                strat1.tu_as_reçu_une_coopereration()
            else :
                strat1.tu_as_été_trahi()
            if strat1_a_cooperer :
                strat2.tu_as_reçu_une_coopereration()
            else :
                strat2.tu_as_été_trahi()