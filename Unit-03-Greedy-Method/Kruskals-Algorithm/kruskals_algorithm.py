"""Kruskal's minimum spanning tree algorithm."""

def kruskals(edges, vertices):
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(u, v):
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        if rank[ru] < rank[rv]:
            parent[ru] = rv
        elif rank[ru] > rank[rv]:
            parent[rv] = ru
        else:
            parent[rv] = ru
            rank[ru] += 1
        return True

    mst = []
    total_cost = 0
    for u, v, weight in sorted(edges, key=lambda e: e[2]):
        if union(u, v):
            mst.append((u, v, weight))
            total_cost += weight
    return mst, total_cost


def main():
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [
        ('A', 'B', 4), ('A', 'C', 2), ('B', 'C', 1),
        ('B', 'D', 5), ('C', 'D', 8), ('C', 'E', 10), ('D', 'E', 2),
    ]
    mst, cost = kruskals(edges, vertices)
    print("MST edges:", mst)
    print("Total cost:", cost)


if __name__ == "__main__":
    main()
