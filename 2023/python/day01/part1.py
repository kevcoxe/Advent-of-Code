from data import INPUT_DATA


words = [word for word in INPUT_DATA.split() if word]

code = 0
found_numbers = []

for word in words:

    ai = 0
    bi = len(word) - 1

    a = word[ai]
    b = word[bi]

    afound = None
    bfound = None

    print(f"\nFinding numbers in word ({ word })...")

    while(ai <= bi and (afound is None or bfound is None)):
        try:
            if afound is None:
                # check for string digit
                afound = int(a)
                print(f"..found A ({afound})...")
        except Exception as e:
            ai = ai + 1
            a = word[ai]

        try:
            if bfound is None:
                # check for string digit
                bfound = int(b)
                print(f"..found B ({bfound})...")
        except Exception as e:
            bi = bi - 1
            b = word[bi]

    found_numbers.append(int(f"{afound}{bfound}"))

code = sum(found_numbers)
print(f"\nWe have found the code, it is: { code }")



