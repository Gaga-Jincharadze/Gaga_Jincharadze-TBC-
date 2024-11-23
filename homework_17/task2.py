graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}
def is_path_exists(graph, start, end):

    if start == end:
        return True
    for neighbor in graph.get(start, []):
        if is_path_exists(graph, neighbor, end):
            return True
    return False

print(is_path_exists(graph, 'A', 'E'))
print(is_path_exists(graph, 'B', 'A'))
print(is_path_exists(graph, 'A', 'D'))
print(is_path_exists(graph, 'D', 'E'))