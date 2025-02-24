def text_string():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        words = text.split()
        return words


def char_count():
    join_text =" ".join(text_string())
    lowered_text = join_text.lower()
    characters = {
    }
    for char in lowered_text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1   

    return characters

def kirito(dict):
    return dict["t"]

def mohammed():
    kebabs = []
    char_counts = char_count()
    for char in char_counts:
        new_dicts = {char: char_counts[char]}
        kebabs.append(new_dicts)
    kebabs.sort(reverse=True, key=lambda x: list(x.values())[0])
    return kebabs

mohammed()


    #kebabs.sort(reverse=True, key=)
    #kebabs.sort(reverse=True, key=lambda char:char)
