from typing import List
def can_construct(target_word: str, word_bank: List[str])-> bool:
    """_Find out whether a target word can be constructed by concatenating str in a given list _

    Args:
        target_word (str): _Word to construct_
        word_bank (List[str]): _A list of str_

    Returns:
        bool: _True if word can be constructed from the given str else False_
    """
    if target_word  == "":
        return True
    for word in word_bank:
            if target_word.startswith(word):
                new_target_word = target_word.removeprefix(word)
                if can_construct(target_word=new_target_word, word_bank=word_bank):
                    return True
    return False

def main()-> None:
    target_word: str = 'abcdef'
    word_bank: List[str] = ['ab', 'abc', 'cd', 'def', 'abcd']

    is_word_possible: bool = can_construct(target_word=target_word, word_bank=word_bank)

    print(f"Is it possible to construct {target_word} by concatenating str(s) in {word_bank}? {is_word_possible}")
    target_word: str = 'skateboard'
    word_bank: List[str] = ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']

    is_word_possible: bool = can_construct(target_word=target_word, word_bank=word_bank)
    print(f"Is it possible to construct {target_word} by concatenating str(s) in {word_bank}? {is_word_possible}")

if __name__ == "__main__":
    main()