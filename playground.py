import model_generator
import networkx as nx

'''
mess around with the constants and run
'''

# CONSTANTT


UNDERPOPULATION = 0.4 
OVERPOPULATION = 0.125
JUST_RIGHT = 0.25

EVOLUTION_STEPS = 20 # amount of steps in the play

N = 50 # NODES
P = 0.2 # Erdos-Reynyi probability(Prob any edge exists)
PB = 0.5 # 



# main-----------------------------------------------------------------------

graph = nx.erdos_renyi_graph(N,P)
initial = model_generator.random_initial_dead(N,PB)
model_generator.main(G=graph,
                    initial=initial,
                    show_plot_flag=True,
                    underpopulation=UNDERPOPULATION,
                    overpopulation=OVERPOPULATION,
                    just_right=JUST_RIGHT,
                    evolution_steps=EVOLUTION_STEPS)