import heapq

def dijkstra(graph, start):
    # graph = {node: [(neighbor, weight), ...], ...}
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # priority queue (distance, node)

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# Example graph
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('D', 1)],
    'C': [('A', 2), ('D', 3)],
    'D': [('B', 1), ('C', 3)]
}

print(dijkstra(graph, 'A'))
