
def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    xroot, yroot = find(parent, x), find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


V, E = map(int, input("Enter number of vertices and edges: ").split())
edges = []
vertices = set()

print("Enter edges (source destination weight):")
for _ in range(E):
    u, v, w = input().split()
    w = int(w)
    vertices.add(u)
    vertices.add(v)
    edges.append((w, u, v))


vertex_list = list(vertices)
vertex_index = {vertex_list[i]: i for i in range(len(vertex_list))}


edges.sort()
parent = [i for i in range(len(vertex_list))]
rank = [0] * len(vertex_list)
mst = []
total_cost = 0

for w, u, v in edges:
    u_idx, v_idx = vertex_index[u], vertex_index[v]
    if find(parent, u_idx) != find(parent, v_idx):
        union(parent, rank, u_idx, v_idx)
        mst.append((u, v, w))
        total_cost += w


print("\nEdges in Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"{u} -- {v} == {w}")
print("Total cost of MST =", total_cost)
