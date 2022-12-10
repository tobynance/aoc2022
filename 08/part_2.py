import math
from dataclasses import dataclass


########################################################################
@dataclass
class Tree:
    height: int
    x: int
    y: int
    visibility_score: int = 0


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
            tree.visibility_score = 0
            return
        else:
            directions = []
            for y_gen in [range(y-1, -1, -1), range(y+1, forest_height)]:
                visibility_score_in_direction = 0
                # check north/south
                for dy in y_gen:
                    visibility_score_in_direction += 1
                    other_tree_height = trees[dy][x].height
                    if other_tree_height >= tree.height:
                        break
                directions.append(visibility_score_in_direction)
            for x_gen in [range(x-1, -1, -1), range(x+1, forest_width)]:
                visibility_score_in_direction = 0
                # check east/west
                for dx in x_gen:
                    visibility_score_in_direction += 1
                    other_tree_height = trees[y][dx].height
                    if other_tree_height >= tree.height:
                        break
                directions.append(visibility_score_in_direction)
            print(f"{x} {y}: {directions}")
            tree.visibility_score = math.prod(directions)

    highest_visibility_score = 0
    for x in range(forest_width):
        for y in range(forest_height):
            check_and_update_tree(x, y)
            if trees[y][x].visibility_score > highest_visibility_score:
                highest_visibility_score = trees[y][x].visibility_score

    print("highest_visibility_score:", highest_visibility_score)


########################################################################
main()
