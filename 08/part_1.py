from dataclasses import dataclass


########################################################################
@dataclass
class Tree:
    height: int
    x: int
    y: int
    visible: bool = False


########################################################################
def main():
    trees = []
    for y, line in enumerate(open("input.txt")):
        line = line.strip()
        tree_row = []
        for x, char in enumerate(line):
            height = int(char)
            tree = Tree(height, x, y)
            tree_row.append(tree)
        trees.append(tree_row)
    forest_width = len(trees[0])
    forest_height = len(trees)

    ####################################################################
    def check_and_update_tree(x, y):
        tree = trees[y][x]
        if x in [0, forest_width-1] or y in [0, forest_height-1]:
            tree.visible = True
            return
        else:
            for y_gen in [range(y-1, -1, -1), range(y+1, forest_height)]:
                # check north/south
                for dy in y_gen:
                    other_tree_height = trees[dy][x].height
                    if other_tree_height >= tree.height:
                        break
                else:
                    tree.visible = True
                    return
            for x_gen in [range(x-1, -1, -1), range(x+1, forest_width)]:
                # check east/west
                for dx in x_gen:
                    other_tree_height = trees[y][dx].height
                    if other_tree_height >= tree.height:
                        break
                else:
                    tree.visible = True
                    return

    num_visible_trees = 0
    for x in range(forest_width):
        for y in range(forest_height):
            check_and_update_tree(x, y)
            if trees[y][x].visible:
                num_visible_trees += 1

    print("num_visible_trees:", num_visible_trees)


########################################################################
main()
