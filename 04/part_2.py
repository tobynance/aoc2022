########################################################################
def get_range(txt) -> set:
    low, high = txt.split("-")
    return set(range(int(low), int(high)+1))


########################################################################
def main():
    overlaps = 0
    for line in open("example.txt"):
        elf_1, elf_2 = [get_range(elf) for elf in line.strip().split(",")]
        if elf_1 & elf_2:
            overlaps += 1
    print("overlaps:", overlaps)


########################################################################
main()
