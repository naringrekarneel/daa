V = int(input("Enter number of vertices: "))
vertices = input(f"Enter {V} vertex names (space separated): ").split()

INF = float('inf')
dist = [[INF]*V for _ in range(V)]

print("Enter adjacency matrix (use 0 if no edge):")
for i in range(V):
    row = input().split()
    for j in range(V):
        w = int(row[j])
        dist[i][j] = w if w != 0 or i == j else INF


for k in range(V):
    for i in range(V):
        for j in range(V):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]


print("\nShortest distances between every pair of vertices:")
for i in range(V):
    for j in range(V):
        print(f"{vertices[i]}->{vertices[j]}:", "INF" if dist[i][j]==INF else dist[i][j], end="  ")
    print()