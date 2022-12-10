import string

priority = {letter: value for value, letter in enumerate(string.ascii_lowercase + string.ascii_uppercase, start=1)}


########################################################################
def main():
    total_sum = 0
    for line in open("input.txt"):
        items = line.strip()
        midpoint = len(items) // 2
        first_compartment = set(items[:midpoint])
        second_compartment = set(items[midpoint:])
        print("first_compartment:", first_compartment)
        print("second_compartment:", second_compartment)
        overlap = first_compartment & second_compartment
        assert len(overlap) == 1
        overlap = overlap.pop()
        print("overlap:", overlap, priority[overlap])
        total_sum += priority[overlap]
        print("\n")
    print("sum:", total_sum)


########################################################################
main()
