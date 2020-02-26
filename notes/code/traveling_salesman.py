# THIS TURNED INTO A JUNK DRAWER
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random

class Node:
  def __init__(self, value):
    self.value = value
    self.edges = {} # maps target to distance from self
  def edge(self, target, distance):
    self.edges[target] = distance


def make_graph():
    names = ['SF', 'OAK', 'SJO', 'PA', 'MTN']

    nodes = {}
    for name in names:
        nodes[name] = Node(name)

    nodes['SF'].edge('OAK', distance=10)
    nodes['SF'].edge('PA', distance=30)
    nodes['OAK'].edge('SJO', distance=50)
    nodes['OAK'].edge('PA', distance=20)
    nodes['PA'].edge('SJO', distance=15)
    nodes['PA'].edge('MTN', distance=5)
    nodes['MTN'].edge('SJO', distance=11)
    return nodes


def shortest_path(nodes,start):
    n = len(nodes)
    all_nodes = set(nodes.keys())
    visited = {start}
    distance = {}
    distance[start] = 0
    while len(visited) < n:
        # find p not in visited with an edge from node in visited to p
        unvisited = all_nodes.difference(visited)
        for q in unvisited:
            if q
            print(q)
        return
        # for p in visited:
        #     if p in nodes[p]
        # # find smallest distance from
        # pass

nodes = make_graph()

shortest_path(nodes,'SF')


