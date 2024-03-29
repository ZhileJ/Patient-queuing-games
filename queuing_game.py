import networkx as nx
import numpy as np
from collections import defaultdict
import sys

from load_graph import *
from compute_utility import *

dictionary_path = "./graphs"

def main():
    argv = sys.argv[1:]
    queues, servers, strategy = load_graph_and_strategy_from_csv("/".join([dictionary_path,argv[0]]))
    utility, solving_rate, partition = compute_utility(queues, servers, strategy)
    print("The utility of each queue are:")
    print(utility)
    print("The f of each queue are:")
    print(solving_rate)
    print("The partition of queues is:")
    for k,v in partition.items():
        print("level", k, ":", v)


if __name__ == '__main__':
    main()


