from stats import text_string
from stats import char_count
from stats import mohammed
import sys

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        print(file_contents)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {len(text_string())} total words") 
        print("--------- Character Count -------")
        num_list = mohammed()
        for char in range(0,len(num_list)):
            for key, value in num_list[char].items():
                if f"{key}".isalpha() == False:
                    None
                else:
                    print(f"{key}: {value}")        

        print("============= END ===============")
        


if __name__ == "__main__":
    main()
