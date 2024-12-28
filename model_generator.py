#=====================================================================================================
#                                       IMPORTS
#======================================================================================================

import networkx as nx
import matplotlib.pyplot as plt
import random
from matplotlib.widgets import Slider

#=====================================================================================================
#                                       FUNCTIONS
#======================================================================================================

def mono_color_map(G: nx.Graph, black_nodes: list):
    monochrome_map = []
    for node in G.nodes:
        if node in black_nodes:
            monochrome_map.append("black")
        else:
            monochrome_map.append("white")
    return monochrome_map


def unique_append(lst, element):
    if element not in lst:
        lst.append(element)


# evolution
def step(G: nx.Graph, dead_nodes, overpopulation, underpopulation, just_right):
    new_dead_nodes = dead_nodes.copy()
    for node in G.nodes:

        num_adjacent_nodes = len(G.adj[node])
        num_dead_adjacent = len([n for n in G.adj[node] if n in dead_nodes])
        num_alive_adjacent = num_adjacent_nodes - num_dead_adjacent

        if (num_adjacent_nodes==0):
            continue

        adj_alive_p = num_alive_adjacent / num_adjacent_nodes

        if (adj_alive_p > overpopulation
        or adj_alive_p< underpopulation):
            unique_append(new_dead_nodes, node)
            continue

        if ((adj_alive_p > just_right) and (node in new_dead_nodes)):
            new_dead_nodes.remove(node)
            continue

    return new_dead_nodes


def get_dead_list(G, initial_dead, overpopulation, underpopulation, just_right, steps=20):
    dead_nodes = initial_dead
    dead_nodes_steps = [dead_nodes]
    for _ in range(steps):
        dead_nodes = step(G, dead_nodes, overpopulation, underpopulation, just_right)
        dead_nodes_steps.append(dead_nodes)
    return dead_nodes_steps


def random_initial_dead(n, p):
    return [node for node in range(n) if random.random() < p]


# New function to handle plotting and interaction
def show_plot(G: nx.Graph, dead_nodes_steps, initial_dead, evolution_steps,pos):
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.35)

    # Positioning the graph layout

    # Draw the initial graph
    node_colors = ['black' if i in initial_dead else 'lightblue' for i in range(G.number_of_nodes())]
    nodes = nx.draw_networkx_nodes(G, pos, node_color=node_colors, ax=ax)
    edges = nx.draw_networkx_edges(G, pos, ax=ax)
    nx.draw_networkx_labels(G, pos, ax=ax)

    # Create a slider for selecting a list of dead nodes
    ax_slider_list = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    set_slider = Slider(ax_slider_list, 'evolution', 0, evolution_steps - 1, valinit=0, valstep=1)

    # Update function for the slider
    def update(val):
        selected_list_index = int(set_slider.val)
        selected_list = dead_nodes_steps[selected_list_index]

        # Update node colors based on the selected list
        node_colors = ['black' if i in selected_list else 'lightblue' for i in range(G.number_of_nodes())]
        nodes.set_facecolor(node_colors)
        fig.canvas.draw_idle()

    # Attach the update function to the slider
    set_slider.on_changed(update)

    # Display the graph
    plt.show()

#=====================================================================================================
#                                       MAIN CALL
#======================================================================================================

def main(G=None, initial=None, show_plot_flag=False, overpopulation=0.4, underpopulation=0.125, just_right=0.25, evolution_steps=20):
    nodes = G.nodes
    pos = nx.layout.shell_layout(G)
    if G is None:
        exit("Graph is not provided")
    
    # Generate the dead node evolution list
    dead_nodes_steps = get_dead_list(G, initial, overpopulation, underpopulation, just_right, evolution_steps)

    if show_plot_flag:
        show_plot(G, dead_nodes_steps, initial, evolution_steps,pos)

    return dead_nodes_steps


