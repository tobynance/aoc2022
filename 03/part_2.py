import string

priority = {letter: value for value, letter in enumerate(string.ascii_lowercase + string.ascii_uppercase, start=1)}


########################################################################
def main():
    total_sum = 0
    with open("input.txt") as in_file:
        while in_file:
            line1 = set(in_file.readline().strip())
            if not line1:
                break
            line2 = set(in_file.readline().strip())
            line3 = set(in_file.readline().strip())

            badge = (line1 & line2 & line3).pop()
            print("badge:", badge)
            total_sum += priority[badge]

    print("sum:", total_sum)


########################################################################
main()
