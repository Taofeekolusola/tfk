import random

def generate_acronym(words):
    # Extract the first letter from each word and capitalize it
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

def main():
    # Get input words from the user
    input_words = input("Enter words to generate an acronym (separated by spaces): ").split()

    # Check if there are at least two words
    if len(input_words) < 2:
        print("Please enter at least two words.")
        return

    # Generate and print the acronym
    acronym = generate_acronym(input_words)
    print("Generated Acronym:", acronym)

if __name__ == "__main__":
    main()
