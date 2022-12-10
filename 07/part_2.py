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
    all_sizes = []
    for folder in walk_folders(root):
        all_sizes.append(folder.size)

    all_sizes = sorted(all_sizes)

    total_storage_available = 70_000_000
    storage_needed = 30_000_000

    unused_space = total_storage_available - root.size

    space_to_clear = storage_needed - unused_space

    print("space_to_clear:", space_to_clear)

    # Find small directory with a size greater than or equal to space_to_clear
    for size in all_sizes:
        if size >= space_to_clear:
            print("folder to delete:", size)
            break


########################################################################
main()
