
def main():
    print("Choose a Mad Lib:\n\n")
    print("1: Star Wars")
    print("2: pizza")
    print("3: summer vacaton")
    choice = input("\n\nEnter Your Choice: ")

    if choice == "1":
        do_star_wars_madlib()
    elif choice == "2":
        do_pizza_madlib()
    elif choice == "3":
        do_summer_vacaton_madlib()

def do_pizza_madlib():
    words_array = []

    pizza_madlib_description_words = ["ajective",
                      "nationality",
                      "person",
                      "noun",
                      "ajective",
                      "noun",
                      "ajective",
                      "ajective",
                      "plural noun",
                      "noun",
                      "number",
                      "shapes",
                      "food",
                      "food",
                      "number",]

    for type_of_word in pizza_madlib_description_words:
        word_from_user = make_a_anything(type_of_word)
        words_array.append(word_from_user)

    print(f"""
        Pizza was invented by a {words_array.pop(0)} {words_array.pop(0)} chef named {words_array.pop(0)}.
        To make pizza, you need to take a lump of {words_array.pop(0)}, and make a thin, round {words_array.pop(0)} {words_array.pop(0)}.
        Then you cover it with {words_array.pop(0)} sauce, {words_array.pop(0)} cheese, and fresh chopped {words_array.pop(0)}.
        Next you have to bake it in a very hot {words_array.pop(0)}.  When it is done, cut it into {words_array.pop(0)} {words_array.pop(0)}.
        Some kids like {words_array.pop(0)} pizza the best, but my favorite is the {words_array.pop(0)} pizza. If I could,
        I would eat pizza {words_array.pop(0)} times a day!
    """)


def do_summer_vacaton_madlib():
    words_array = []

    summer_vacaton_description_words = ["person",
                                        "place",
                                        "ajective",
                                        "same place",
                                        "plural noun",
                                        "ajective",
                                        "plural noun",
                                        "place",
                                        "verb",
                                        "plural noun",
                                        "plural noun",
                                        "noun",
                                        "verb",
                                        "verb",
                                        "ajective",]


    for type_of_word in summer_vacaton_description_words:
        word_from_user = make_a_anything(type_of_word)
        words_array.append(word_from_user)




    print(f"""
        Last summer, my mom and dad took me and {words_array.pop(0)} on a trip to {words_array.pop(0)}.
        The weather there is very {words_array.pop(0)}! Nothern {words_array.pop(0)} has many {words_array.pop(0)},
    and they make {words_array.pop(0)} {words_array.pop(0)} there. Many people also go to {words_array.pop(0)} to
        {words_array.pop(0)} or see the {words_array.pop(0)}. The people that live there love to eat {words_array.pop(0)}
        and are very proud of their big {words_array.pop(0)}. They also like to {words_array.pop(0)} in the sun and swim
        in the {words_array.pop(0)}! It was a really {words_array.pop(0)} trip!
    """)
def do_star_wars_madlib():
    types_of_words_we_need = ["adjective",
                              "noun",
                              "adjective",
                              "place",
                              "ajdective",
                              "adjective",
                              "vehicle",
                              "adjective",
                              "adjective",
                              "plural_noun",
                              "ajective",
                              "plural noun",
                              "plural noun",
                              "ajectdesxfcrive",
                              "noun",
                              "verb",
                              "adjective",
                              "verb",
                              "plural noun",
                              "type of job",
                              "ajective",
                              "verb",
                              "ajective",]

    words_array = []

    for type_of_word in types_of_words_we_need:
        word_from_user = make_a_anything(type_of_word)
        words_array.append(word_from_user)

    print(f"Star Wars is a {words_array.pop(0)} {words_array.pop(0)} of {words_array.pop(0)} versus evil in a {words_array.pop(0)} far far away.")
    print(f"There are {words_array.pop(0)} battles between {words_array.pop(0)} {words_array.pop(0)} in {words_array.pop(0)} space and {words_array.pop(0)} "
          f"duels with {words_array.pop(0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 )} called {words_array.pop(0)} sabers. {words_array.pop(0)} ")
    print(f"called \"droids\" are helpers and {words_array.pop(0)} to the heroes. A {words_array.pop(0)} power called the {words_array.pop(0)} {words_array.pop(0)}s people to do")
    print(f"{words_array.pop(0)} things, like {words_array.pop(0)} {words_array.pop(0)}. The Jedi {words_array.pop(0)} use The Force for the")
    print(f"{words_array.pop(0)} side and the Sith {words_array.pop(0)} it for the {words_array.pop(0)} side.")

def make_a_anything(type_of_word):
    word = input(f"Enter a {type_of_word}: ")
    return word

if __name__ == '__main__':
    main()
