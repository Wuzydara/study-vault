#include <stdio.h>
#include <string.h>

char data[100], padded_data[100], cs[50], gen[50];
int data_len, gen_len, c, e;

// XOR operation between current check sequence and generator polynomial
void xor_function() {
    for (c = 1; c < gen_len; c++) {
        cs[c] = (cs[c] == gen[c]) ? '0' : '1';
    }
}

// CRC computation using Modulo-2 Division
void compute_crc() {
    // Copy first gen_len bits of padded data into check sequence buffer
    for (e = 0; e < gen_len; e++) {
        cs[e] = padded_data[e];
    }

    do {
        // If MSB is '1', perform XOR with generator polynomial
        if (cs[0] == '1') {
            xor_function();
        }
        // Shift left by 1 bit and bring down next bit from padded_data
        for (c = 0; c < gen_len - 1; c++) {
            cs[c] = cs[c + 1];
        }
        cs[c] = padded_data[e++];
    } while (e <= data_len + gen_len - 1);
}

int main() {
    int choice;

    printf("=============================================\n");
    printf("     CYCLIC REDUNDANCY CHECK (CRC) DEMO      \n");
    printf("=============================================\n\n");

    printf("Select Generator Polynomial:\n");
    printf("1. Basic / Lab Default (1011)\n");
    printf("2. CRC-12    (1100000001111)\n");
    printf("3. CRC-16    (11000000000000101)\n");
    printf("4. CRC-CCITT (10001000000100001)\n");
    printf("Enter choice (1-4): ");
    scanf("%d", &choice);

    switch (choice) {
        case 1: strcpy(gen, "1011"); break;
        case 2: strcpy(gen, "1100000001111"); break;
        case 3: strcpy(gen, "11000000000000101"); break;
        case 4: strcpy(gen, "10001000000100001"); break;
        default:
            printf("Invalid choice! Defaulting to 1011.\n");
            strcpy(gen, "1011");
    }

    gen_len = strlen(gen);

    printf("\nEnter binary data to transmit (e.g., 10100001): ");
    scanf("%s", data);

    data_len = strlen(data);
    strcpy(padded_data, data);

    // Step 1: Pad data with (gen_len - 1) zeros
    for (e = data_len; e < data_len + gen_len - 1; e++) {
        padded_data[e] = '0';
    }
    padded_data[e] = '\0';

    printf("\n---------------------------------------------");
    printf("\nGenerator Polynomial : %s", gen);
    printf("\nPadded Data          : %s", padded_data);
    printf("\n---------------------------------------------");

    // Step 2: Compute CRC remainder
    compute_crc();
    printf("\nGenerated CRC Checksum: %s", cs);

    // Step 3: Replace padded zeros with actual CRC bits
    for (e = data_len; e < data_len + gen_len - 1; e++) {
        padded_data[e] = cs[e - data_len];
    }
    printf("\nFinal Transmitted Frame: %s", padded_data);
    printf("\n---------------------------------------------");

    // Step 4: Error Detection Test
    printf("\nTest Error Detection? (0 = Yes, 1 = No): ");
    scanf("%d", &e);

    if (e == 0) {
        int pos;
        do {
            printf("Enter bit position to flip (1 to %d): ", data_len + gen_len - 1);
            scanf("%d", &pos);
        } while (pos < 1 || pos > data_len + gen_len - 1);

        // Flip bit at position (1-indexed)
        padded_data[pos - 1] = (padded_data[pos - 1] == '0') ? '1' : '0';

        printf("---------------------------------------------");
        printf("\nCorrupted Data Frame : %s\n", padded_data);
    }

    // Step 5: Receiver verification
    compute_crc();

    // Check if remainder contains any '1's
    int error_flag = 0;
    for (e = 0; e < gen_len - 1; e++) {
        if (cs[e] == '1') {
            error_flag = 1;
            break;
        }
    }

    printf("---------------------------------------------");
    if (error_flag) {
        printf("\nRESULT: ERROR DETECTED in received frame!\n");
    } else {
        printf("\nRESULT: NO ERROR DETECTED (Frame is valid).\n");
    }
    printf("=============================================\n");

    return 0;
}