#include "shell.h"
ssize_t _print(const char* message) {
    // Check if the input pointer is NULL
    if (message == NULL) {
        //fprintf(stderr, "Error: Null pointer passed to our_print function.\n");
        return -1; // Return an error code or handle the error as appropriate
    }
    // Calculate the length of the message
    size_t message_length = strlen(message);
    // Allocate memory for the modified message
    char* newline_message = malloc(message_length + 2); // Include space for '\n' and '\0'
    // Check if memory allocation is successful
    if (newline_message == NULL) {
        perror("Error allocating memory");
        return -1; // Return an error code or handle the error as appropriate
    }
    // Copy the original message to the new buffer
    strcpy(newline_message, message);
    // Add a newline character at the end of the message
    newline_message[message_length] = '\n';
    newline_message[message_length + 1] = '\0'; // Null-terminate the string
    // Write the modified message to the standard output
    ssize_t bytes_written = write(STDOUT_FILENO, newline_message, message_length + 2);
    // Check for errors during write
    if (bytes_written == -1) {
        perror("Error writing to STDOUT");
        // Handle the error or exit the program
    }
    // Free the dynamically allocated memory
    free(newline_message);
    // Return the number of bytes written
    return bytes_written;
}
