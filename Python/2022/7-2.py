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

# - / (dir)
#   - a (dir)
#     - e (dir)
#       - i (file, size=584)
#     - f (file, size=29116)
#     - g (file, size=2557)
#     - h.lst (file, size=62596)
#   - b.txt (file, size=14848514)
#   - c.dat (file, size=8504156)
#   - d (dir)
#     - j (file, size=4060174)
#     - d.log (file, size=8033020)
#     - d.ext (file, size=5626152)
#     - k (file, size=7214296)

# find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes
# In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584).

# from lark import Lark

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

total = 70000000
required = 30000000


with open('7.txt', 'r') as file:
    example = file.read()


class DirTree:
    def __init__(self, name, size=None, parent=None):
        self.name = name
        self.parent = parent
        self.size = size
        self.dir = {}
        self.is_dir = False if size else True
        self.path = (self.parent.path + '/' + name) if self.parent else '~'

    def add_child(self, name, size=None):
        self.dir[name] = DirTree(name=name, size=size, parent=self)

    def get_level(self):
        if not self.parent:
            return 0
        return 1 + self.parent.get_level()

    def __eq__(self, other):
        return (
                self.name == other.name and
                self.size == other.size and
                self.dir == other.dir
        )

    def __str__(self):
        if self.size:
            out = "  "
        else:
            out = "**"
        out *= self.get_level()
        out += self.name
        out += '\t\t' + str(self.size)
        # out += '\t\t' + (str(self.size) if self.size else str(self.get_size()))
        out += '\n'
        out += ''.join([str(child) for child in self.dir.values() if child.is_dir])
        return out

    def __repr__(self):
        return self.path

    def get_dir_sizes(self):
        global dir_sizes
        child_sizes = []
        for child in self.dir.values():
            if child.size:
                child_sizes.append(child.size)
            else:
                child_sizes.append(child.get_dir_sizes())
        self.size = sum(child_sizes)
        dir_sizes[self.path] = self.size
        return self.size


dir_sizes = {}
folders = DirTree('/')
active = folders

for line in example.strip().splitlines()[1:]:
    if line.startswith('$'):
        if (loc := line.split()[-1]) == '..':
            active = active.parent
        elif loc != 'ls':
            active = active.dir[loc]
    else:
        type_size, name = line.split()
        if type_size == 'dir':
            active.add_child(name)
        else:
            active.add_child(name, int(type_size))

# print(folders)
folders.get_dir_sizes()
# print(folders)

to_delete = required - (total - folders.size)
print(min(size for size in dir_sizes.values() if size > to_delete))

# # print(sum(lim_sizes))
# free = total - max(lim_sizes.values())
# to_delete = required - free
# gained = [x for x in lim_sizes.values() if x > to_delete]
# # print(gained[-1])
# # print(sorted(list(lim_sizes.values())))
# # print('ok')
#
