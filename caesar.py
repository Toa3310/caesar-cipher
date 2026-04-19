def apply_mode(mode, shift):
    return shift if mode == "1" else -shift

def char_shift(char, shift):
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        return chr((ord(char) - base + shift) % 26 + base)
    return char

def caesar_cipher(mode, text, shift):
    applied_shift = apply_mode(mode, shift)
    result = ""
    for char in text:
        result += char_shift(char, applied_shift)
    return result

if __name__ == "__main__":
    mode = input("モードを選択してください(暗号化:1, 復号:2) → ")
    if mode == "1":
        plaintext = input("平文を入力してください: ")
        shift = int(input("シフト量を入力してください（例: 3）: "))
        print("暗号文:", caesar_cipher(mode, plaintext, shift))
    elif mode == "2":
        ciphertext = input("暗号文を入力してください: ")
        shift = int(input("シフト量を入力してください (例: 3) : "))
        print("復号結果:", caesar_cipher(mode, ciphertext, shift))
    else:
        print("入力が間違っています。")