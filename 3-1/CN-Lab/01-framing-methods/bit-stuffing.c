#include <stdio.h>
#include <string.h>

/**
 * Function to perform bit stuffing on a binary string.
 * Inserts a '0' after five consecutive '1's in the data stream.
 */
void bitStuffing(const char source[], char stuffed[]) {
    int srcIndex = 0;
    int destIndex = 0;
    int count = 0;

    while (source[srcIndex] != '\0') {
        if (source[srcIndex] == '1') {
            count++;
        } else {
            count = 0; // Reset count on encountering '0'
        }

        // Copy current bit to destination
        stuffed[destIndex++] = source[srcIndex++];

        // If five consecutive '1's are found, insert a '0'
        if (count == 5) {
            stuffed[destIndex++] = '0';
            count = 0; // Reset counter after stuffing
        }
    }
    stuffed[destIndex] = '\0'; // Null-terminate destination string
}

int main() {
    char sourceData[100];
    char stuffedData[200];

    printf("========================================\n");
    printf("   DATA LINK LAYER: BIT STUFFING LAB    \n");
    printf("========================================\n");
    
    printf("Enter binary data (e.g., 11111111): ");
    if (scanf("%99s", sourceData) != 1) {
        printf("Error reading input.\n");
        return 1;
    }

    bitStuffing(sourceData, stuffedData);

    printf("\n--- RESULTS ---\n");
    printf("Original Data : %s\n", sourceData);
    printf("Stuffed Frame : %s\n", stuffedData);
    printf("========================================\n");

    return 0;
}
