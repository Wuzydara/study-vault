#include <stdio.h>
#include <stdlib.h>

#define MAX 50
#define INF 99

int n;
int edge[MAX][MAX];
int parent[MAX];
int t[MAX][2];

// Find operation with Path Compression / Parent Check
int find(int i) {
    while (parent[i] >= 0) {
        i = parent[i];
    }
    return i;
}

// Union operation for disjoint sets
void sunion(int i, int j) {
    parent[i] = j;
}

int main() {
    int i, j, u = -1, v = -1, p, q;
    int min = INF, mincost = 0;
    int edge_count = 0;

    printf("===================================================\n");
    printf("     SUBNET BROADCAST TREE (SPANNING TREE)         \n");
    printf("===================================================\n\n");

    printf("Enter the number of hosts/routers in the subnet: ");
    scanf("%d", &n);

    // Initialize parent array for disjoint sets (-1 indicates root)
    for (i = 0; i < n; i++) {
        parent[i] = -1;
    }

    printf("\nEnter the cost matrix (use 99 for infinity / no direct edge):\n");
    printf("   ");
    for (i = 0; i < n; i++) {
        printf("  %c", 65 + i); // Labels A, B, C, ...
    }
    printf("\n");

    for (i = 0; i < n; i++) {
        printf("%c  ", 65 + i);
        for (j = 0; j < n; j++) {
            scanf("%d", &edge[i][j]);
        }
    }

    // Kruskal's Algorithm loop
    for (int k = 0; k < n * n; k++) {
        min = INF;

        // Find the edge with minimum cost
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                if (edge[i][j] < min) {
                    min = edge[i][j];
                    u = i;
                    v = j;
                }
            }
        }

        // Check if adding this edge forms a cycle
        p = find(u);
        q = find(v);

        if (p != q) {
            t[edge_count][0] = u;
            t[edge_count][1] = v;
            mincost += min;
            sunion(p, q);
            edge_count++;
        }

        // Mark edge as visited so it isn't picked again
        edge[u][v] = INF;
        edge[v][u] = INF;

        if (edge_count == n - 1)
            break; // Spanning tree completed
    }

    printf("\n---------------------------------------------------\n");
    printf(" Total Minimum Cost of Broadcast Tree = %d\n", mincost);
    printf("---------------------------------------------------\n");
    printf(" Broadcast Tree Edges (Subnet Links):\n");
    printf(" Edge\tCost\n");
    printf(" ----\t----\n");

    for (i = 0; i < edge_count; i++) {
        printf(" %c - %c\t  %d\n", 65 + t[i][0], 65 + t[i][1],
               edge[t[i][0]][t[i][1]]);
    }
    printf("===================================================\n");

    return 0;
}
