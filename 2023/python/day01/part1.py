from data import INPUT_DATA


words = [word for word in INPUT_DATA.split() if word]

code = 0
found_numbers = []

for word in words:
    ai = 0
    bi = len(word) - 1

    a = word[ai]
    b = word[bi]

    aFound = False
    bFound = False

    aNum = 0
    bNum = 0

    print(f"\nFinding numbers in word ({ word })...")

    while(ai <= bi and (not aFound or not bFound)):
        try:
            if not aFound:
                # check for string digit
                aNum = int(a)
                aFound = True
                print(f"..found A ({ aNum })...")
        except Exception as e:
            ai = ai + 1
            a = word[ai]

        try:
            if not bFound:
                # check for string digit
                bNum = int(b)
                bFound = True
                print(f"..found B ({ bNum })...")
        except Exception as e:
            bi = bi - 1
            b = word[bi]

    found_numbers.append(int(f"{ aNum }{ bNum }"))

code = sum(found_numbers)
print(f"\nWe have found the code, it is: { code }")



