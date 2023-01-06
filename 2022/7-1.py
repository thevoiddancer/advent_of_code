# find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes
# In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584).

example = r"""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

# with open('7.txt', 'r') as file:
#     example = file.read()


class DirTree:
    def __init__(self, name, size=None, parent=None):
        self.name = name
        self.parent = parent
        self.size = size
        self.items = {}

    def add_child(self, name, size=None):
        self.items[name] = DirTree(name=name, size=size, parent=self)

    def get_level(self):
        if not self.parent:
            return 0
        return 1 + self.parent.get_level()

    def get_size(self):
        global lim_sizes
        sizes = []
        for item in self.items.values():
            if item.size:
                sizes.append(item.size)
            else:
                sizes.append(item.get_size())
        lim_sizes.append(sum(sizes))
        return sum(sizes)

    def __eq__(self, other):
        return (
            self.name == other.name and
            self.size == other.size and
            self.items == other.dir
        )

    def __str__(self):
        return '  ' * self.get_level() + self.name + '\n' + ''.join([str(child) for child in self.items.values()])


lim_sizes = []

folders = DirTree('/')
active = folders

for line in example.strip().splitlines()[1:]:
    if line.startswith('$'):
        if (loc := line.split()[-1]) == '..':
            active = active.parent
            print(line, "go back")
        elif loc != 'ls':
            active = active.items[loc]
            print(line, 'new folder')
        else:
            print(line, 'list files')
    else:
        type_size, name = line.split()
        if type_size == 'dir':
            active.add_child(name)
            print(line, 'add dir')
        else:
            active.add_child(name, int(type_size))
            print(line, 'add file')

print(folders)
folders.get_size()
print(sum(lim_sizes))
print('ok')

