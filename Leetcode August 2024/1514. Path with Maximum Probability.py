'''
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

 
'''
#Solution
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        weights=list(map(lambda x:-math.log2(x),succProb))
        graph=defaultdict(list)
        for (u,v),w in zip(edges,weights):
            graph[u].append([v,w])
            graph[v].append([u,w])

        dist={}
        q=[(0,start)]
        while q:
            w,u=heapq.heappop(q)
            if u in dist:
                continue

            dist[u]=w
            if u==end:
                break

            for v,w in graph[u]:
                if v not in dist or dist[v]>dist[u]+w:
                    heapq.heappush(q,(dist[u]+w,v))

        return 2**(-dist[end]) if end in dist else 0.0                    
