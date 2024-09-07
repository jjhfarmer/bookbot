def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wc = get_book_wc(text)
    count = get_character_count(text)
    chars_sorted_list = count_dict_to_sorted_list(count)
    
    print(f"---Begin report of {book_path} ---")
    print(f"{wc} words found in the document.")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times ")

    print("--- End report ---")

def sort_on(d):
    return d["num"]

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_wc(text):
    return len(text.split())

def get_character_count(text):
    lc_text = text.lower()
    character_count = {}
    for ch in lc_text:
        if ch in character_count:
            character_count[ch] += 1
        else:
            character_count[ch] = 1
    return character_count

def count_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()