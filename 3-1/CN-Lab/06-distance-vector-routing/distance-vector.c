#include <stdio.h>

#define MAX 20
#define INF 9999

struct node {
    unsigned dist[MAX];
    unsigned from[MAX];
} rt[MAX];

int main() {
    int dmat[MAX][MAX];
    int n, i, j, k, count = 0;

    printf("===================================================\n");
    printf("        DISTANCE VECTOR ROUTING ALGORITHM          \n");
    printf("===================================================\n\n");

    printf("Enter the number of nodes/routers: ");
    scanf("%d", &n);

    printf("\nEnter the cost matrix (use 9999 for infinity / no direct edge):\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            scanf("%d", &dmat[i][j]);

            // Self distance is always 0
            if (i == j) {
                dmat[i][j] = 0;
            }

            // Initialize routing table for node i
            rt[i].dist[j] = dmat[i][j];
            rt[i].from[j] = j;
        }
    }

    // Iteratively update routing tables using Bellman-Ford equation
    do {
        count = 0;
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                for (k = 0; k < n; k++) {
                    if (rt[i].dist[j] > dmat[i][k] + rt[k].dist[j]) {
                        rt[i].dist[j] = dmat[i][k] + rt[k].dist[j];
                        rt[i].from[j] = k;
                        count++;
                    }
                }
            }
        }
    } while (count != 0);

    // Print final routing table for each router
    printf("\n===================================================\n");
    printf("                 FINAL ROUTING TABLES              \n");
    printf("===================================================\n");

    for (i = 0; i < n; i++) {
        printf("\nRouting Table for Router %d:\n", i + 1);
        printf("-----------------------------------\n");
        printf(" Destination | Next Hop | Distance \n");
        printf("-------------|----------|----------\n");

        for (j = 0; j < n; j++) {
            printf("   Node %-4d |  Node %-2d |   %-6d\n", j + 1, rt[i].from[j] + 1, rt[i].dist[j]);
        }
        printf("-----------------------------------\n");
    }

    return 0;
}
