import itertools
import networkx as nx
import pandas as pd

# Friendship network
G = nx.Graph()

players = [1,2,3,4,5,0]
G.add_nodes_from(players)

edges = [
    
]
G.add_edges_from(edges)

strategies = ['G','N']
profiles = list(itertools.product(strategies, repeat=6))


# Payoff function
def compute_payoffs(profile):

    strategy_dict = {player: profile[i] for i, player in enumerate(players)}
    payoffs = {}

    for player in players:

        if strategy_dict[player] == 'N':
            payoffs[player] = 0

        else:
            payoff = 0
            for friend in G.neighbors(player):

                if strategy_dict[friend] == 'G':
                    payoff += 1
                else:
                    payoff -= 1

            payoffs[player] = payoff

    return payoffs


# Find Nash equilibria
nash_equilibria = []

for profile in profiles:

    payoffs = compute_payoffs(profile)
    is_nash = True

    for i, player in enumerate(players):

        current_strategy = profile[i]
        alternate_strategy = 'N' if current_strategy == 'G' else 'G'

        new_profile = list(profile)
        new_profile[i] = alternate_strategy
        new_profile = tuple(new_profile)

        new_payoffs = compute_payoffs(new_profile)

        if new_payoffs[player] > payoffs[player]:
            is_nash = False
            break

    if is_nash:
        nash_equilibria.append({
            "P1": profile[0],
            "P2": profile[1],
            "P3": profile[2],
            "P4": profile[3],
            "P5": profile[4],
            "P6": profile[5],
            "Payoff_P1": payoffs[0],
            "Payoff_P2": payoffs[1],
            "Payoff_P3": payoffs[2],
            "Payoff_P4": payoffs[3],
            "Payoff_P5": payoffs[4],
            "Payoff_P6": payoffs[5]
        })


# Convert to dataframe
ne_df = pd.DataFrame(nash_equilibria)

# Export to Excel
ne_df.to_excel()

print("Number of Nash equilibria:", len(ne_df))
print(ne_df)