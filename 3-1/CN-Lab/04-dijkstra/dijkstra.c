#include <stdio.h>

#define INFINITY 9999
#define MAX 10

void dijkstra(int G[MAX][MAX], int n, int startnode);

int main() {
    int G[MAX][MAX], i, j, n, u;

    printf("===============================================\n");
    printf("       DIJKSTRA'S SHORTEST PATH ROUTING       \n");
    printf("===============================================\n\n");

    printf("Enter number of vertices/routers: ");
    scanf("%d", &n);

    printf("\nEnter the Adjacency Matrix (use 0 for self-loops or no direct edge):\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            scanf("%d", &G[i][j]);
        }
    }

    printf("\nEnter the starting (source) node (0 to %d): ", n - 1);
    scanf("%d", &u);

    dijkstra(G, n, u);

    return 0;
}

void dijkstra(int G[MAX][MAX], int n, int startnode) {
    int cost[MAX][MAX], distance[MAX], pred[MAX];
    int visited[MAX], count, mindistance, nextnode, i, j;

    // Step 1: Create the cost matrix
    // Replace 0s with INFINITY for non-self-loop nodes without direct edges
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if (G[i][j] == 0 && i != j)
                cost[i][j] = INFINITY;
            else
                cost[i][j] = G[i][j];
        }
    }

    // Step 2: Initialize arrays
    for (i = 0; i < n; i++) {
        distance[i] = cost[startnode][i];
        pred[i] = startnode;
        visited[i] = 0;
    }

    distance[startnode] = 0;
    visited[startnode] = 1;
    count = 1;

    // Step 3: Main loop to find shortest paths
    while (count < n - 1) {
        mindistance = INFINITY;

        // Find the unvisited node with the smallest distance
        for (i = 0; i < n; i++) {
            if (distance[i] < mindistance && !visited[i]) {
                mindistance = distance[i];
                nextnode = i;
            }
        }

        visited[nextnode] = 1;

        // Relax neighbors of nextnode
        for (i = 0; i < n; i++) {
            if (!visited[i]) {
                if (mindistance + cost[nextnode][i] < distance[i]) {
                    distance[i] = mindistance + cost[nextnode][i];
                    pred[i] = nextnode;
                }
            }
        }
        count++;
    }

    // Step 4: Display shortest paths and distances
    printf("\n-----------------------------------------------\n");
    printf(" SHORTEST PATHS FROM SOURCE NODE %d\n", startnode
