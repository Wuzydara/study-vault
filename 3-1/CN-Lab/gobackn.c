#include <stdio.h>

int main() {
    int window_size, total_frames;
    int i, ack;
    int current_frame = 1;

    printf("========================================\n");
    printf("   SLIDING WINDOW PROTOCOL: GO-BACK-N   \n");
    printf("========================================\n\n");

    printf("Enter window size (W): ");
    if (scanf("%d", &window_size) != 1 || window_size <= 0) {
        printf("Invalid window size.\n");
        return 1;
    }

    printf("Enter total number of frames to transmit: ");
    if (scanf("%d", &total_frames) != 1 || total_frames <= 0) {
        printf("Invalid frame count.\n");
        return 1;
    }

    while (current_frame <= total_frames) {
        int sent_in_window = 0;

        printf("\n----------------------------------------\n");
        printf("Sender: Transmitting window starting at Frame %d\n", current_frame);
        printf("Frames sent: ");

        // Send up to W frames
        for (i = current_frame; i < current_frame + window_size && i <= total_frames; i++) {
            printf("[%d] ", i);
            sent_in_window++;
        }
        printf("\n----------------------------------------\n");

        // Simulate ACK or Frame Loss
        printf("Enter last successfully acknowledged frame number (0 if Frame %d failed): ", current_frame);
        scanf("%d", &ack);

        if (ack >= current_frame && ack < current_frame + sent_in_window) {
            printf(">>> ACK %d received. Sliding window forward to Frame %d.\n", ack, ack + 1);
            current_frame = ack + 1;
        } 
        else if (ack >= current_frame + sent_in_window) {
            // All frames in current window acknowledged
            printf(">>> ACK %d received. All frames in this window acknowledged!\n", ack);
            current_frame = ack + 1;
        } 
        else {
            // Frame loss occurred
            printf(">>> ERROR/TIMEOUT at Frame %d! Receiver discarded subsequent frames.\n", current_frame);
            printf(">>> Go-Back-N Triggered: Retransmitting from Frame %d...\n", current_frame);
            // current_frame remains unchanged, so loop retransmits the window
        }
    }

    printf("\n========================================\n");
    printf(" SUCCESS: All %d frames sent and acknowledged!\n", total_frames);
    printf("========================================\n");

    return 0;
}
