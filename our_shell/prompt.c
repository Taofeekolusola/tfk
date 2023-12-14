#include "shell.h"
ssize_t promptprint(const char* prompt) {
    return write(STDOUT_FILENO, prompt, strlen(prompt));
}
