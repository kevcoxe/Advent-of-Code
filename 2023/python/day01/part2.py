from data import INPUT_DATA, NUMBERS

def indices(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)

word_with_numbers_list = {}
def getNumbersFromWord(word):
    word_with_numbers_list[word] = []

    l = [(dex, NUMBERS[n], n) for i,n in enumerate(NUMBERS) if n in word for dex in indices(word, n)]

    l.sort(key=lambda a: a[0])
    word_with_numbers_list[word] = l

    firstWordIndex = len(word)
    lastWordIndex = -1
    if len(l) > 0:
        firstWordIndex = l[0][0]
        lastWordIndex = l[-1][0] + len(l[-1][2]) - 1

    ai = 0
    bi = len(word) - 1

    a = word[ai]
    b = word[bi]

    aFound = False
    bFound = False

    aNum = 0
    bNum = 0

    print(f"\nFinding numbers in word ({ word })...")
    print(firstWordIndex, lastWordIndex, l)

    while(ai <= bi and (not aFound or not bFound)):
        try:
            if not aFound and ai >= firstWordIndex:
                aNum = l[0][1]
                aFound = True
                print(f"..found A ({ aNum }) {ai} {l[0][2]}...")

            if not aFound:
                # check for string digit
                aNum = int(a)
                aFound = True
                print(f"..found A ({ aNum }) {ai}...")
        except Exception as e:
            ai = ai + 1
            a = word[ai]

        try:
            print(f"bFound: {bFound}, bi: {bi}, lastWordIndex: {lastWordIndex}")
            if not bFound and bi < lastWordIndex:
                bNum = l[-1][1]
                bFound = True
                print(f"..found B ({ bNum }) {bi} {l[-1][2]}...")

            if not bFound:
                # check for string digit
                bNum = int(b)
                bFound = True
                print(f"..found B ({ bNum }) {bi}...")
        except Exception as e:
            bi = bi - 1
            b = word[bi]

    return(int(f"{ aNum }{ bNum }"))

def runPart2():
    words = [word for word in INPUT_DATA.split() if word]

    code = 0
    found_numbers = []


    for word in words:
        found_numbers.append(getNumbersFromWord(word))

    code = sum(found_numbers)
    print(f"\nWe have found the code, it is: { code }")


if __name__ == '__main__':
    runPart2()
