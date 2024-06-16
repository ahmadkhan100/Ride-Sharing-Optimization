import heapq
import math

def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    seen = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node in seen:
            continue
        path = path + [node]
        seen.add(node)
        if node == end:
            return (cost, path)
        for (next_node, weight) in graph.get(node, []):
            heapq.heappush(queue, (cost + weight, next_node, path))
    return (float("inf"), [])

def heuristic(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def a_star(graph, start, end, locations):
    queue = [(0, start, [])]
    seen = set()
    g = {start: 0}
    f = {start: heuristic(locations[start], locations[end])}
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node in seen:
            continue
        path = path + [node]
        seen.add(node)
        if node == end:
            return (cost, path)
        for (next_node, weight) in graph.get(node, []):
            tentative_g = g[node] + weight
            if next_node not in g or tentative_g < g[next_node]:
                g[next_node] = tentative_g
                f[next_node] = tentative_g + heuristic(locations[next_node], locations[end])
                heapq.heappush(queue, (f[next_node], next_node, path))
    return (float("inf"), [])

