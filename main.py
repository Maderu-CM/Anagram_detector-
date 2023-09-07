
from lib.anagram import Anagram

def main():
    # Create an Anagram object
    listen = Anagram("listen")

    # Find matches in a list of possible anagrams
    matches = listen.match(['enlists', 'google', 'inlets', 'banana'])

    # Print the matches
    print("Anagrams of 'listen':", matches)

if __name__ == "__main__":
    main()
