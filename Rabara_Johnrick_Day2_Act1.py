import re

# Sample stanza from a song or poem (for demonstration purposes, here is a stanza from "Twinkle, Twinkle, Little Star")
original_lyrics = "Twinkle, twinkle, little star, How I wonder what you are. Up above the world so high, Like a diamond in the sky."

def replace_words(lyrics, noun1, noun2, adj1, adj2):
    # Replace placeholders in the lyrics with user inputs
    words = lyrics.split()
    replacements = [noun1.upper(), noun2.upper(), adj1.upper(), adj2.upper()]
    pattern = r'\b\w+\b'  # Pattern to match each word
    
    # Replace words based on a simple rule: nouns and adjectives alternate replacements.
    modified_lyrics = []
    replacement_index = 0
    for word in words:
        if re.match(pattern, word) and replacement_index < len(replacements):
            modified_lyrics.append(replacements[replacement_index])
            replacement_index += 1
        else:
            modified_lyrics.append(word)
    
    return " ".join(modified_lyrics)

def main():
    # Step 2: Get user input for nouns and adjectives
    noun1 = input("Enter the first noun: ")
    noun2 = input("Enter the second noun: ")
    adj1 = input("Enter the first adjective: ")
    adj2 = input("Enter the second adjective: ")

    # Display the original lyrics
    print("\nOriginal Lyrics:\n")
    print(original_lyrics)

    # Perform replacements in the original lyrics
    modified_lyrics = replace_words(original_lyrics, noun1, noun2, adj1, adj2)

    # Display the modified lyrics
    print("\nModified Lyrics:\n")
    print(modified_lyrics)

# Create the file and run the main function
if __name__ == "__main__":
    main()
