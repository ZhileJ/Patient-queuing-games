import numpy as np
from collections import defaultdict

def compute_utility(queues, servers, strategy):
    n_queues = queues.shape[0]
    n_servers = servers.shape[0]

    if strategy.shape[0] != queues.shape[0] or strategy.shape[1] != servers.shape[0]:
        raise TypeError('Not a valid stratgy matrix.')

    neg_strategy = 1 - strategy
    neg_strategy_T = neg_strategy.T
    queues_name = list(range(1, n_queues + 1))
    servers_name = list(range(1, n_servers + 1))

    awaiting_nodes = queues_name.copy()
    partition = defaultdict(list)
    solving_rate = np.zeros(n_queues, dtype=np.float64)
    utility = np.zeros(n_queues, dtype=np.float64)
    level = 0
    while len(awaiting_nodes) != 0:
        n_awaiting_nodes = len(awaiting_nodes)
        n_power_sets_queue = 1 << n_awaiting_nodes
        rate_min = len(servers)
        set_min = []
        vector_min = None
        for x in range(1, n_power_sets_queue):
            vector_subset = np.zeros(n_queues,dtype=np.int8)
            list_subset = []
            for i in range(n_awaiting_nodes):
                if min(x & (1 << i), 1) != 0:
                    vector_subset[awaiting_nodes[i]-1] = 1
                    list_subset.append(awaiting_nodes[i])
            sum_lamb = (queues * vector_subset).sum()
            wasted_prob = np.clip(neg_strategy_T + (1 - vector_subset),0,1)
            prod_neg_strategy = 1-wasted_prob.prod(axis=1)
            sum_mu = (servers * prod_neg_strategy).sum()
            rate = sum_mu/sum_lamb
            if rate < rate_min or rate == rate_min and len(list_subset)>len(set_min):
                rate_min = rate
                set_min = list_subset.copy()
                vector_min = vector_subset
        neg_prod_neg_strategy = np.clip(neg_strategy_T + (1 - vector_min),0,1).prod(axis=1)
        servers *= neg_prod_neg_strategy
        partition[level] = set_min.copy()
        for i in set_min:
            awaiting_nodes.remove(i)
            solving_rate[i-1] = rate_min
            utility[i-1] = max(1-rate_min,0)
        level += 1
    return utility, solving_rate, partition