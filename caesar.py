def apply_mode(mode, shift):
    return shift if mode == "1" else -shift

def input_shift():
    count = 0
    while count < 5:
        try:
            shift =  int(input("シフト量を入力してください（例: 3）: "))
            return shift
        except ValueError:
            print("整数以外が入力されました。もう一度入力してください")
            count += 1
    print("5回連続で入力ミスがありました。")
    return None

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
        text = input("平文を入力してください: ")
    elif mode == "2":
        text = input("暗号文を入力してください: ")
    else:
        print("モード選択では1か2を入力してください。")
        exit()

    shift = input_shift()
    if shift is None:
        print("処理を終了します。")
        exit()

    result = caesar_cipher(mode, text, shift)
    if mode == "1":
        print("暗号文:", result)
    else:
        print("復号結果:", result)