import argparse
import string


def decode(password, to_decode, pointer=0):
    if pointer >= len(to_decode):
        return ""

    letters = string.ascii_lowercase

    key = {}

    print(f"cipher len: {len(to_decode)}")

    current_id = 1
    for letter in letters:
        for i in range(len(password)):
            if password[i] == letter:
                key[i] = (password[i], current_id)
                current_id += 1

    sorted_key = []
    for i in range(len(key)):
        sorted_key.append(key[i])

    total_key_value = 0
    for sk in sorted_key:
        total_key_value += sk[1]

    print(f"total key value: {total_key_value}")
    print(f"fraction check: {len(to_decode) / total_key_value}")
    print(sorted_key)

    varchar_l = []
    for s_key in sorted_key:
        length = s_key[1]
        varchar = ""
        for i in range(length):
            varchar += to_decode[i + pointer]
        pointer += length
        varchar_l.append(varchar)
        print(f"{varchar}")

    de_cipher = ""
    for i in range(current_id):
        for vl in varchar_l:
            try:
                de_cipher += vl[i]
            except IndexError:
                pass

    return de_cipher + decode(password, to_decode, pointer)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("passkey")
    parser.add_argument("cipher")
    args = parser.parse_args()

    passkey = args.passkey
    cipher = args.cipher

    result = decode(passkey, cipher)

    if len(result) == len(cipher):
        print("Input is equally long as the output")

    print(result)
