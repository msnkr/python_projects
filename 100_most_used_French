import random
import os

french_to_english = {
    'le': 'the',
    'de': 'of',
    'un': 'a',
    'à': 'to',
    'être': 'be',
    'et': 'and',
    'en': 'in',
    'avoir': 'have',
    'que': 'that',
    'pour': 'for',
    'dans': 'in',
    'ce': 'this',
    'il': 'he',
    'qui': 'who',
    'ne': 'not',
    'sur': 'on',
    'se': 'himself',
    'pas': 'not',
    'plus': 'more',
    'pouvoir': 'can',
    'par': 'by',
    'je': 'I',
    'avec': 'with',
    'tout': 'all',
    'faire': 'make',
    'nous': 'we',
    'son': 'his',
    'mettre': 'put',
    'autre': 'other',
    'mais': 'but',
    'on': 'one',
    'dire': 'say',
    'ou': 'where',
    'si': 'if',
    'me': 'me',
    'voir': 'see',
    'bien': 'well',
    'rien': 'nothing',
    'être': 'being',
    'leur': 'their',
    'savoir': 'know',
    'vouloir': 'want',
    'très': 'very',
    'deux': 'two',
    'ici': 'here',
    'même': 'same',
    'quand': 'when',
    'y': 'there',
    'temps': 'time',
    'aller': 'go',
    'sans': 'without',
    'ainsi': 'thus',
    'notre': 'our',
    'encore': 'still',
    'mon': 'my',
    'trouver': 'find',
    'personne': 'person',
    'jouer': 'play',
    'cette': 'this',
    'pendant': 'during',
    'mettre': 'set',
    'grand': 'big',
    'ainsi': 'thus',
    'quelque': 'some',
    'nouveau': 'new',
    'partir': 'leave',
    'prendre': 'take',
    'vivre': 'live',
    'travail': 'work',
    'venir': 'come',
    'devoir': 'must',
    'dernier': 'last',
    'voir': 'see',
    'lui': 'him',
    'autre': 'other',
    'monde': 'world',
    'homme': 'man',
    'chose': 'thing',
    'jour': 'day',
    'temps': 'time',
    'peu': 'few',
    'depuis': 'since',
    'soir': 'evening',
    'venir': 'come',
    'jour': 'day',
    'toujours': 'always',
    'enfant': 'child',
    'aller': 'go',
    'femme': 'woman',
    'père': 'father',
    'beaucoup': 'much',
    'donner': 'give',
    'avant': 'before',
    'main': 'hand',
    'rendre': 'render',
    'après': 'after',
    'autre': 'other',
    'petit': 'small',
    'très': 'very',
    'venir': 'come',
    'ouvrir': 'open',
    'là': 'there',
    'deux': 'two',
    'mourir': 'die',
    'devoir': 'owe',
    'déjà': 'already',
    'croire': 'believe',
    'rien': 'nothing',
    'entendre': 'hear',
    'devenir': 'become',
}


def quiz(new_dict):
    count = 1
    score = 0
    os.system("cls")
    another_dict = {}

    for word in new_dict:
        correct_word = input(
            f" {count}. What is the English word for {word}: ")
        if correct_word == new_dict[word]:
            print("You are correct!")
            score += 1
        else:
            print(f"The correct word is: {new_dict[word]}")
        count += 1

    print(f"Your score is: {score}")


def get_words(dictionary):
    new_dict = {}
    for _ in range(10):
        random_word = random.choice(list(french_to_english.items()))
        new_dict[random_word[0]] = random_word[1]

    count = 1
    for key in new_dict:
        print(f"{count}. French: {key}. English: {new_dict[key]}")
        space_bar = input("Press Enter to continue")
        count += 1

    quiz(new_dict)


def main():
    print("Learn the most used French words")
    print("Press enter to move to the next word")
    get_words(french_to_english)


if __name__ == "__main__":
    main()
