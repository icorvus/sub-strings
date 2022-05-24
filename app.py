
def sub_strings(input_string: str, word_list):
    input_string = input_string.lower()
    subs_dictionary = {}
    for word in word_list:
        count = 0
        start = 0
        while input_string.find(word, start) != -1:
            count += 1
            start = input_string.find(word, start) + 1
        if count:
            subs_dictionary[word] = count
    return subs_dictionary
            


def main():
    dictionary = ["below","down","go","going","horn","how","howdy","it","i","low","own","part","partner","sit"]
    print(sub_strings("below", dictionary))
    print(sub_strings("Howdy partner, sit down! How's it going?", dictionary))

if __name__ == "__main__":
    main()