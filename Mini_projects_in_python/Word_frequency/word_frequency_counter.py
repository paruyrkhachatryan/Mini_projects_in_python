def get_content(filename):
    """
    Read content from a file and return it.
    """
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return ""


stop_words = {"a", "of", "on", "i", "for", "with", "the", "at",
              "from", "in", "to", "is", "and", "was", "as", "were"}


def count_words(content):
    """
    Count words in the content and return a dictionary of word counts.
    """
    words = content.lower().split()
    return {word: words.count(word) for word in set(words) if word.isalpha() and word not in stop_words}


def check_top_num():
    """
    Prompt the user to enter the number of top words and return it.
    """
    while True:
        top_num = input("Enter the number of top words to show: ")
        try:
            top_num = int(top_num)
            if top_num > 0:
                return top_num
            else:
                print("Invalid input. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_tops(tops, words):
    """
    Get the top 'tops' words from the given dictionary of words and their counts.
    """
    return sorted(words.items(), key=lambda x: x[1], reverse=True)[:tops]


def main():
    """
    Main function to process the text file, count words, and display top words.
    """
    content = get_content("text.txt")
    counted_words = count_words(content)
    top_num = check_top_num()
    top_words = get_tops(top_num, counted_words)
    print("Top {} words and their frequencies:".format(top_num))
    for word, count in top_words:
        print(word, ":", count)


if __name__ == "__main__":
    main()

