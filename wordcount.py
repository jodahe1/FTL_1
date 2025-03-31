# Q.4

def read_text_from_file(file_path):
    """Reads text from a file and returns it as a string."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def count_words(text):
    """Counts word occurrences, excluding stop words, and returns a dictionary."""
    stop_words = {
        'a', 'an', 'the', 'and', 'or', 'but', 'is', 'are', 'was', 'were',
        'in', 'on', 'at', 'to', 'of', 'for', 'with', 'by', 'as', 'it',
        'this', 'that', 'these', 'those', 'be', 'been', 'have', 'has', 'had',
        'i', 'you', 'he', 'she', 'we', 'they', 'me', 'him', 'her', 'us', 'them'
    }

    words = text.lower().split()

    filtered_words = []
    for word in words:
        cleaned_word = ''.join(
            char for char in word if char.isalpha() or char == "'")
        if cleaned_word and cleaned_word not in stop_words:
            filtered_words.append(cleaned_word)

    word_count = {}
    for word in filtered_words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


def print_word_count(word_count):
    """Prints word counts sorted by frequency (highest first)."""
    sorted_words = sorted(word_count.items(),
                          key=lambda item: item[1], reverse=True)
    for word, count in sorted_words:
        print(f"{word}: {count}")


def main(file_path):
    """Orchestrates reading, counting, and printing word counts."""
    try:
        text = read_text_from_file(file_path)
        word_count = count_words(text)
        print_word_count(word_count)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Usage: python word_count.py <file_path>")

# Run on bash python wordcount.py sample.txt