# A text simplifier

def uprosc_zdanie(tekst, dl_slowa, liczba_slow):
    """
    Simplify a sentence by cutting too long words
    and limit the total number of words.

    :param tekst: the text
    :param dl_slowa: the maximum length of a word
    :param liczba_slow: the maximum number of words
    :return: the simplified text
    """
    # Split the text by the space delimiter.
    words = tekst.split()
    # Remove the words longer than the parameter's value.
    words = [word for word in words if len(word) <= dl_slowa]
    # Return only the first words.
    words = words[:liczba_slow]
    return ' '.join(words) + '.'

example = ("Podział peryklinalny inicjałów wrzecionowatych kambium charakteryzuje sie "
         "sciana podziałowa inicjowana w płaszczyznie maksymalnej.")
print(uprosc_zdanie(example, 10, 5))
