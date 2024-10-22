import gol_network
import networkx as nx
import random
import csv
import os
import simple_colors


def stepsb4_sizzleout(G,dead_list_steps):
    for dead_list in enumerate(dead_list_steps):
        if (len(dead_list[1])==len(G.nodes)):
            return dead_list[0]
    return -1

file_name = "./data1.csv"
file = open(file_name,'w+',newline='')
writer = csv.writer(file)
writer.writerow(["trial","edos_renyi p","poss of initial dead","steps till all dead","clustering","assortativity coefficent"])
for trial in range(100000):
        n = 50
        p,pb = random.uniform(0.1,0.9),random.uniform(0.1,0.9)
        print(simple_colors.blue("p="+str(p)+",pb="+str(pb)+"::"),end="")
        G = nx.erdos_renyi_graph(n,p)
        initial = gol_network.random_initial_dead(n,pb)
        num = stepsb4_sizzleout(G,gol_network.main(G,initial,show_plot_flag=False,evolution_steps=50))
        writer.writerow([trial,p,pb,num,sum(nx.clustering(G))/len(G.nodes),nx.degree_assortativity_coefficient(G)])
        del n,p,pb
        print(simple_colors.green("COMPUTED TRIAL:"+str(trial)))



