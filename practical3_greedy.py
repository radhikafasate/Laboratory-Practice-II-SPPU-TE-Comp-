import heapq

# -----------------------------------
# I. Selection Sort
# -----------------------------------
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    print("Sorted Array:", arr)


# -----------------------------------
# II & V. Prim's MST
# -----------------------------------
def prim_mst(graph, start):
    visited = set()
    pq = [(0, start)]
    total_cost = 0

    while pq:
        cost, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        total_cost += cost
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (weight, neighbor))

    print("Prim's MST Cost:", total_cost)


# -----------------------------------
# III & VII. Dijkstra (Shortest Path)
# -----------------------------------
def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        current_dist, node = heapq.heappop(pq)

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    print("Shortest distances:")
    for node in dist:
        print(start, "->", node, "=", dist[node])


# -----------------------------------
# IV. Job Scheduling
# -----------------------------------
def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    slots = [False] * max_deadline
    result = []

    for job in jobs:
        for j in range(job[1]-1, -1, -1):
            if not slots[j]:
                slots[j] = True
                result.append(job[0])
                break

    print("Scheduled Jobs:", result)


# -----------------------------------
# VI. Kruskal MST
# -----------------------------------
def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]


def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1


def kruskal(vertices, edges):
    edges.sort(key=lambda x: x[2])

    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    mst = []

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            mst.append((u, v, w))
            union(parent, rank, u, v)

    print("Kruskal MST:", mst)


# -----------------------------------
# Sample Graph/Data
# -----------------------------------
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 5)],
    'D': [('B', 4), ('C', 5)]
}

jobs = [
    ('J1', 2, 100),
    ('J2', 1, 19),
    ('J3', 2, 27),
    ('J4', 1, 25),
    ('J5', 3, 15)
]

vertices = ['A', 'B', 'C', 'D']
edges = [
    ('A', 'B', 1),
    ('B', 'C', 2),
    ('A', 'C', 3),
    ('C', 'D', 4)
]


# -----------------------------------
# Menu
# -----------------------------------
while True:
    print("\n--- GREEDY ALGORITHMS MENU ---")
    print("1. Selection Sort")
    print("2. Minimum Spanning Tree (Prim)")
    print("3. Single Source Shortest Path (Dijkstra)")
    print("4. Job Scheduling")
    print("5. Prim's MST")
    print("6. Kruskal's MST")
    print("7. Dijkstra Algorithm")
    print("0. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        arr = [64, 25, 12, 22, 11]
        selection_sort(arr)

    elif choice == 2:
        prim_mst(graph, 'A')

    elif choice == 3:
        dijkstra(graph, 'A')

    elif choice == 4:
        job_scheduling(jobs)

    elif choice == 5:
        prim_mst(graph, 'A')

    elif choice == 6:
        kruskal(vertices, edges)

    elif choice == 7:
        dijkstra(graph, 'A')

    elif choice == 0:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")