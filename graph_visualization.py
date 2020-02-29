import numpy as np
import pandas as pd
import networkx as nx
import math
import matplotlib.pyplot as plt
'''
    This program generates 2 separate gml document for Gephi Visualization
    Handle each dataset separately
    This part is for lyft
    Further visualization would be done in Gephi
'''
dataset = pd.read_csv('cab_rides.csv', delimiter = ',')                                   #Read the dataset as Dataframe
dataset = dataset.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)     #delete invalid rows
'''
    create the node set for sources.
'''
grapher = nx.DiGraph();       
sources = dataset['source'];                                                              #Filter out nodes from source attribute
sources = sources.drop_duplicates(keep='first',inplace=False)                             #We want each node appear once
grapher.add_nodes_from(sources.values);
nx.draw(grapher,with_labels = True) 
plt.show()

uber = dataset[dataset['cab_type']=='Uber']
lyft = dataset[dataset['cab_type']=='Lyft']


lyftgraph = nx.DiGraph();
sources = lyft['source'];
sources = sources.drop_duplicates(keep='first',inplace=False)
lyftgraph.add_nodes_from(sources.values);
print(lyftgraph)
label = 0
nx.set_node_attributes(lyftgraph,label,'meanprice');

for i in lyftgraph.nodes:
    print(i);
    a = lyft[lyft['source'] == i];
    prices = a['price'].values
    distances = a['distance'].values;
    print(prices.shape[0]);
    numitem = int(prices.shape[0])
    for j in range(1,numitem):
        prices[j] = prices[j]/distances[j];                      #We want to get the price/distance ratio
    lyftgraph.nodes[i]['meanprice'] = np.mean(prices);
    
    
sources = lyft['source'];
sources = sources.drop_duplicates(keep='first',inplace=False)
sources = sources.values
destinations = lyft['destination'];
destinations = destinations.drop_duplicates(keep='first',inplace=False)
destinations = destinations.values

for i in sources:
    for j in destinations:    
        a = lyft[(lyft['source']==i)&(lyft['destination']==j)];
        b = a['price'].values;
        lyftgraph.add_edge(i,j,weight = np.mean(b));
nx.draw(lyftgraph,with_labels = True) 
plt.show()
john2 = nx.write_gml(lyftgraph,'lyft_price_dist.gml');

'''
    Handle each dataset separately
    This part is for uber
'''
ubergraph = nx.DiGraph();
sources = uber['source'];
sources = sources.drop_duplicates(keep='first',inplace=False)
ubergraph.add_nodes_from(sources.values);
print(ubergraph)
label = 0
nx.set_node_attributes(ubergraph,label,'meanprice');

for i in ubergraph.nodes:
    print(i);
    a = uber[uber['source'] == i];
    prices = a['price'].values
    distances = a['distance'].values;
    print(prices.shape[0]);
    numitem = int(prices.shape[0])
    for j in range(1,numitem):
        prices[j] = prices[j]/distances[j];
    print(prices)
    ubergraph.nodes[i]['meanprice'] = np.mean(prices);
    print(ubergraph.nodes[i]['meanprice']);
    
    
sources = uber['source'];
sources = sources.drop_duplicates(keep='first',inplace=False)
sources = sources.values
destinations = uber['destination'];
destinations = destinations.drop_duplicates(keep='first',inplace=False)
destinations = destinations.values

for i in sources:
    for j in destinations:    
        a = uber[(uber['source']==i)&(uber['destination']==j)];
        b = a['price'].values;
        ubergraph.add_edge(i,j,weight = np.mean(b));
nx.draw(ubergraph,with_labels = True) 
plt.show()
john2 = nx.write_gml(ubergraph,'uber_price_dist.gml');