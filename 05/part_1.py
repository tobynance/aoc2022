import collections


########################################################################
def triplets(line):
    while line:
        crate = line[:3]
        line = line[4:]
        yield crate


########################################################################
def print_stacks(stacks):
    last_stack = max(stacks.keys())
    for i in range(1, last_stack+1):
        print(f"{i}: {stacks[i]}")


########################################################################
def stack_tops(stacks):
    last_stack = max(stacks.keys())
    for i in range(1, last_stack+1):
        yield stacks[i][0]


########################################################################
def main():
    stacks = collections.defaultdict(list)
    with open("input.txt") as in_file:
        while line := in_file.readline():
            line = line.replace("\n", "")
            if line == "":
                break
            print(repr(line))
            for stack_num, crate in enumerate(triplets(line), start=1):
                if crate[0] == "[":
                    stacks[stack_num].append(crate[1])
                print("crate:", repr(crate))
        print(stacks)
        print_stacks(stacks)
        while line := in_file.readline():
            match line.strip().split():
                case ["move", num_crates, "from", from_stack, "to", to_stack]:
                    print(f"{line.strip()} - num_crates={num_crates}, from_stack={from_stack}, to_stack={to_stack}")
                    for i in range(int(num_crates)):
                        crate = stacks[int(from_stack)].pop(0)
                        stacks[int(to_stack)].insert(0, crate)
        print(stacks)
        print_stacks(stacks)
        tops = "".join(list(stack_tops(stacks)))
        print(tops)


########################################################################
main()
