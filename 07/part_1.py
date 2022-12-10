from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional


########################################################################
@dataclass
class Folder:
    name: str
    parent: Optional[Folder]
    children: dict = field(default_factory=dict)

    ####################################################################
    @property
    def size(self):
        return sum([child.size for child in self.children.values()])


########################################################################
@dataclass
class File:
    name: str
    size: int


########################################################################
def walk_folders(folder):
    yield folder
    for child in folder.children.values():
        if isinstance(child, Folder):
            for entry in walk_folders(child):
                yield entry


########################################################################
def main():
    root = Folder("/", None)
    current = None
    for line in open("input.txt"):
        line = line.strip()
        print(repr(line))
        match line.split():
            case ["$", "cd", "/"]:
                current = root
            case ["$", "cd", ".."]:
                current = current.parent
            case ["$", "cd", folder_name]:
                if folder_name not in current.children:
                    current.children[folder_name] = Folder(folder_name, current)
                current = current.children[folder_name]
            case [file_size, file_name] if file_size.isdigit():
                current.children[file_name] = File(file_name, int(file_size))

    # Now check all file sizes
    print(root)
    sum_of_sizes = 0
    for folder in walk_folders(root):
        if folder.size <= 100_000:
            sum_of_sizes += folder.size
        print("folder:", folder.name)
    print("sum_of_sizes:", sum_of_sizes)


########################################################################
main()
