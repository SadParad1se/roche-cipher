import argparse
import string
from typing import List, Tuple


def create_key_table(key: str) -> List[Tuple[str, int]]:
    """
    Create an ordered key table.
    :param key: A word used for decoding
    :return: Key table
    """
    ordered_key = {}
    order = 1
    for letter in string.ascii_lowercase:
        for i in range(len(key)):
            if key[i] == letter:
                ordered_key[i] = (key[i], order)
                order += 1

    return [ordered_key[i] for i in range(len(ordered_key))]


def decode_cipher(key_table: List[Tuple[str, int]], cipher: str, pointer: int) -> str:
    """
    Decode the cipher using the key table.
    :param key_table: Table with the key used for decoding
    :param cipher: Encoded text
    :param pointer: How much of the text have we translated
    :return: Decoded text
    """
    # First, create a table according to the key table
    characters_table = []
    for key in key_table:
        length = key[1]
        characters = ""
        for i in range(length):
            characters += cipher[i + pointer]

        characters_table.append(characters)
        pointer += length

    # Load the characters in the correct order
    decoded_cipher = ""
    for i in range(key_table[-1][1]):
        for characters in characters_table:
            if i < len(characters):
                decoded_cipher += characters[i]

    # If we still haven't decoded the cipher, continue
    return decoded_cipher + (decode_cipher(key_table, cipher, pointer) if pointer < len(cipher) else "")


def main(key: str, cipher: str):
    """
    Generate key table and decode the cipher with it.
    :param key: Key to decode the text
    :param cipher: Encoded text
    :return: None
    """
    key_table = create_key_table(key.lower())
    result = decode_cipher(key_table, cipher, 0)

    if len(result) != len(cipher):
        raise AssertionError("Input and output length is not equal! Please, submit a report.")

    print(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        "Roche cipher decoder",
        description="Insert the key and the encoded text you want to decode."
    )
    parser.add_argument("key")
    parser.add_argument("text")
    args = parser.parse_args()

    main(args.key, args.text)
