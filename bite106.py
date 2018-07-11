text = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
vowels = 'aeiou'


def strip_vowels(text=text):
    """Replace all vowels by *, return newly formed string
       and number of replacements done"""
    words = text.split()
    new_words = []
    number_replacements = 0
    for word in words:
        characters = list(word)
        new_character_list = []
        for character in characters:
            if str(character).lower() in vowels:
                character = "*"
                number_replacements += 1
            new_character_list.append(character)
        new_character_list = ''.join(new_character_list)
        new_words.append(new_character_list)
    output = " ".join(new_words)

    return output, number_replacements
