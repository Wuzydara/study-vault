#include <stdio.h>
#include <string.h>

int main() {
    char frame[100][50];  // Array to hold stuffed frame elements
    char str[50][50];    // Array to hold user input tokens
    char flag[] = "flag";
    char esc[] = "esc";
    int i, n, k = 0;

    printf("========================================\n");
    printf("   DATA LINK LAYER: BYTE STUFFING LAB   \n");
    printf("========================================\n");

    printf("Enter number of data tokens/words: ");
    if (scanf("%d", &n) != 1) {
        printf("Invalid input.\n");
        return 1;
    }

    printf("Enter %d data string(s):\n", n);
    for (i = 0; i < n; i++) {
        scanf("%s", str[i]);
    }

    // 1. Add starting FLAG to the frame
    strcpy(frame[k++], flag);

    // 2. Perform Byte Stuffing on data
    for (i = 0; i < n; i++) {
        // If current string is 'flag' or 'esc', insert 'esc' first
        if (strcmp(str[i], flag) == 0 || strcmp(str[i], esc) == 0) {
            strcpy(frame[k++], esc);
        }
        // Copy the actual data string
        strcpy(frame[k++], str[i]);
    }

    // 3. Add ending FLAG to the frame
    strcpy(frame[k++], flag);

    // Display Output
    printf("\n----------------------------------------\n");
    printf("Frame after Byte Stuffing (Sender Side):\n");
    printf("----------------------------------------\n");
    for (i = 0; i < k; i++) {
        printf("%s\t", frame[i]);
    }
    printf("\n========================================\n");

    return 0;
}
