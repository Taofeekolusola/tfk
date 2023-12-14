#include "shell.h"
ssize_t our_print(const char* message) {
    size_t message_length = strlen(message);
    char newline_message[message_length + 2]; // Allocate space for message + '\n' + '\0'
    // Copy the original message to the new buffer
    strcpy(newline_message, message);
    // Add a newline character at the end of the message
    newline_message[message_length] = '\n';
    newline_message[message_length + 1] = '\0'; // Null-terminate the string
    ssize_t bytes_written = write(STDOUT_FILENO, newline_message, message_length + 1);
if (bytes_written == -1) {
    perror("Error writing to STDOUT");
    // Handle the error or exit the program
}
    // Write the modified message to the standard output
    //return write(STDOUT_FILENO, newline_message, message_length + 1); // Include the newline character
}
