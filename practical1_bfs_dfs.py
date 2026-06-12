from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}      
        self.vertices = set()

    def add_edge(self, u, v):
        """Add an undirected edge between u and v."""

        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

        self.vertices.add(u)
        self.vertices.add(v)

    def display(self):
        """Display adjacency list."""
        print("\nAdjacency List:")
        if not self.vertices:
            print("Graph is empty.")
            return

        for node in sorted(self.vertices):
            print(f"{node} --> {sorted(self.graph[node])}")


    def bfs(self, start):
        """Breadth First Search."""
        if start not in self.vertices:
            print("Vertex not found.")
            return

        visited = set()
        queue = deque([start])
        traversal = []

        visited.add(start)

        print(f"\nBFS starting from {start}:")

        while queue:
            node = queue.popleft()
            traversal.append(node)

            for neighbour in sorted(self.graph[node]):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        print(" -> ".join(map(str, traversal)))


    def dfs(self, start):
        """Depth First Search (recursive)."""
        if start not in self.vertices:
            print("Vertex not found.")
            return

        visited = set()
        traversal = []

        def dfs_recursive(node):
            visited.add(node)
            traversal.append(node)

            for neighbour in sorted(self.graph[node]):
                if neighbour not in visited:
                    dfs_recursive(neighbour)

        print(f"\nDFS starting from {start}:")
        dfs_recursive(start)

        print(" -> ".join(map(str, traversal)))




def build_sample_graph(g):
    edges = [(0,1), (0,2), (1,3), (1,4), (2,5), (2,6)]

    for u, v in edges:
        g.add_edge(u, v)

    print("Sample graph loaded.")


def menu():
    g = Graph()

    while True:
        print("\n" + "="*40)
        print(" GRAPH TRAVERSAL MENU ")
        print("="*40)
        print("1. Add Edge")
        print("2. Display Graph")
        print("3. BFS")
        print("4. DFS")
        print("5. Load Sample Graph")
        print("6. Clear Graph")
        print("7. Exit")

        choice = input("Enter choice: ").strip()

        if choice == '1':
            try:
                u = int(input("Enter vertex u: "))
                v = int(input("Enter vertex v: "))
                g.add_edge(u, v)
                print("Edge added.")
            except ValueError:
                print("Invalid input!")

        elif choice == '2':
            g.display()

        elif choice == '3':
            try:
                start = int(input("Enter start vertex: "))
                g.bfs(start)
            except ValueError:
                print("Invalid input!")

        elif choice == '4':
            try:
                start = int(input("Enter start vertex: "))
                g.dfs(start)
            except ValueError:
                print("Invalid input!")

        elif choice == '5':
            g = Graph()
            build_sample_graph(g)

        elif choice == '6':
            g = Graph()
            print("Graph cleared.")

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice.")



if __name__ == "__main__":
    menu()
