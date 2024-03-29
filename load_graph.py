import networkx as nx #for future visualization
import pandas as pd
import numpy as np

def load_graph_and_strategy_from_csv(path):
    df = pd.read_csv(path)
    df.rename(columns={df.columns[0]:'queues'}, inplace = True)
    queues = np.array(df["queues"], dtype = np.float64)
    if np.any(queues > 1) or np.any(queues < 0):
        raise ValueError('There exists at least one queue has incorrect generating rate.')
    servers = np.array(df.columns[1:],dtype = np.float64)
    if np.any(servers > 1) or np.any(servers < 0):
        raise ValueError('There exists at least one server has incorrect processing rate.')
    strategy = np.array(df[df.columns[1:]],dtype = np.float64)
    if np.any(strategy > 1) or np.any(strategy < 0) or np.any(np.sum(strategy, axis=1) > 1):
        raise ValueError('There exists at least one queue has incorrect strategy.')
    return queues, servers, strategy

#load_graph_and_strategy_from_csv("./graphs/test.csv"))