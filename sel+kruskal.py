def sel():
    arr = list(map(int, input("Enter numbers (space-separated): ").split()))
    print("Original: ", arr)
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print("Sorted: ", arr)

def find(p, i):
    while p[i] != i:
        i = p[i]
    return i

def uni(p, x, y):
    p[find(p, y)] = find(p, x)

def krusk():
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))
    edges = []
    print("Enter edges in format: u v weight")
    for _ in range(e):
        u, v, wt = map(int, input().split())
        edges.append((wt, u, v))
    
    edges.sort()
    parent = [i for i in range(n)]
    mst = []
    total_cost = 0

    for wt, u, v in edges:
        if find(parent, u) != find(parent, v):
            mst.append((u, v, wt))
            total_cost += wt
            uni(parent, u, v)

    print("Minimum Spanning Tree:")
    for u, v, w in mst:
        print(f"{u} --> {v} = {w}")
    print("Total cost of MST:", total_cost)

def main():
    while True:
        print("\nMenu:\n1. Selection Sort\n2. Kruskal's Algorithm\n3. Exit")
        ch = input("Enter Your Choice: ")
        if ch == '1':
            sel()
        elif ch == '2':
            krusk()
        elif ch == '3':
            print("Exiting...")
            break
        else:
            print("Enter a valid choice (1-3).")

main()
