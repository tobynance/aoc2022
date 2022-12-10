########################################################################
def get_range(txt) -> set:
    low, high = txt.split("-")
    return set(range(int(low), int(high)+1))


########################################################################
def main():
    subsets = 0
    for line in open("input.txt"):
        elf_1, elf_2 = [get_range(elf) for elf in line.strip().split(",")]
        if elf_1.issubset(elf_2) or elf_2.issubset(elf_1):
            subsets += 1
    print("subsets:", subsets)


########################################################################
main()
