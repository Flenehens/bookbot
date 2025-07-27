
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def count_words(text):
    word_count = text.split()
    return len(word_count)

def character_count(text):
    char_count = {}
    lowerCase = text.lower()
    for i in lowerCase:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count


def sort_on(items):
    return items["num"]


    
def sorted_count(char_count):
    sorted_count_list = []
    for key,value in char_count.items():
        sorted_count_list.append({"char":key, "num":value})
    sorted_count_list.sort(reverse=True, key=sort_on)
    return sorted_count_list