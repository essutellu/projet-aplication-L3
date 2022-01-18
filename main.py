import strategie
import tournoi

#chaque stratégie est le joueur 1
#ici il est le t dans tc
cc = 3
tc = 5
ct = 0
tt = 1
strat1 = strategie.gentille(cc, tc, ct, tt)
strat2 = strategie.mechante(cc, tc, ct, tt)

print(strat1.coopére_tu())
print(strat2.coopére_tu())
strat1.tu_as_été_trahi()
strat2.tu_as_reçu_une_coopereration()
print(strat1.getter_score())
print(strat2.getter_score())

to = tournoi.tournoi()
to.duel(strat1, strat2, 100)
print(strat1.getter_score())
print(strat2.getter_score())