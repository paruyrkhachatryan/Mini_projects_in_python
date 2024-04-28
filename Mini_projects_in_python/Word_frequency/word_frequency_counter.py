def get_content(filename):
    with open(filename) as f:
        return f.read()


stop_words = {"a", "of", "on", "i", "for", "with", "the", "at",
              "from", "in", "to", "is", "and", "was", "as", "were"}


def count_words(content):
    words = content.lower().split()
    return {word: words.count(word) for word in set(words) if word.isalpha() and word not in stop_words}


def check_top_num(words):
    while True:
        tops = input("Enter the number of top words to show: ")
        if tops.isdigit() and int(tops) <= len(words):
            return int(tops)
        else:
            print("Invalid input. Please enter a number within the range.")


def get_tops(tops, words):
    return sorted(words.items(), key=lambda x: x[1], reverse=True)[:tops]


def main():
    content = get_content("text.txt")
    counted_words = count_words(content)
    top_num = check_top_num(counted_words)
    top_words = get_tops(top_num, counted_words)
    print("Top {} words and their frequencies:".format(top_num))
    for word, count in top_words:
        print(word, ":", count)


if __name__ == "__main__":
    main()
