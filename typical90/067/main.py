n, k = map(int, input().split())

def oct_to_base9(oct_str):
    # 10進数に変換
    dec = int(oct_str, 8)
    # 9進数に変換
    digits = []
    if dec == 0:
        return "0"
    while dec > 0:
        digits.append(str(dec % 9))
        dec //= 9
    return "".join(reversed(digits))

now = str(n)
for _ in range(k):
    nine_str = oct_to_base9(now)
    now = nine_str.replace('8', '5')

print(now)
