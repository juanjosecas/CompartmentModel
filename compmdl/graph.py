import networkx as nx


def build_graph(model):
    G = nx.DiGraph()

    for c in model.compartments:
        G.add_node(c)

    for flow in model.flows:
        G.add_edge(flow.from_, flow.to, rate=flow.rate)

    return G