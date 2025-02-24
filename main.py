from stats import text_string
from stats import char_count
from stats import mohammed

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {len(text_string())} total words") 
        print("--------- Character Count -------")
        num_list = mohammed()
        counter = -1
        for char in mohammed():
            counter += 1
            if f"{num_list[counter]}".isalpha() == False:
                None
            else:
                print(num_list[char])
        print("============= END ===============")
        


if __name__ == "__main__":
    main()
