from d7.day7_input import DATA

test_input = """$ cd /
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


class Directory:
    name = None
    parent = None
    dirs: []
    files: []

    def __init__(self, name: str, parent=None):
        self.name = name
        self.parent = parent
        self.dirs = []
        self.files = []

    def print_filesystem(self):
        print(self.name)
        print(self.files)
        print('------')
        for d in self.dirs:
            d.print_filesystem()

    def get_file_sizes(self, tmp):
        total = 0

        for f in self.files:
            size = int(f.split(' ')[0])
            total += size

        if not self.dirs:
            tmp.append(total)
            return total

        for d in self.dirs:
            size = d.get_file_sizes(tmp)
            total += size

        tmp.append(total)
        return total

    def add_file(self, file):
        self.files.append(file)

    def add_dir(self, dr):
        self.dirs.append(dr)

    def get_dir(self, name):
        for d in self.dirs:
            if d.name == name:
                return d
        return None

    def get_parent(self):
        return self.parent

    def __str__(self):
        return f"{self.name}"


def solution(data):
    fs = Directory('/')
    current_dir = fs
    for l in data.split("\n"):
        if l.startswith('$'):
            if 'cd ' in l:
                if '/' in l:
                    current_dir = fs
                elif '..' in l:
                    current_dir = current_dir.get_parent()
                else:
                    name = l.replace('cd ', '').replace('$', '').strip()
                    current_dir = current_dir.get_dir(name)

        elif l.startswith('dir'):
            name = l.replace('dir', '').strip()
            d = Directory(name, parent=current_dir)
            current_dir.add_dir(d)
        else:
            current_dir.add_file(l)

    tmp = []
    fs.get_file_sizes(tmp)
    return tmp


def first_res(data):
    all_files = solution(data)
    return sum(list(filter(lambda k: k <= 100000, all_files)))


def second_res(data):
    all_files = solution(data)
    total = max(all_files)
    unused = 70000000 - total
    required = 30000000 - unused
    return min(list(filter(lambda k: k >= required, all_files)))


assert first_res(test_input) == 95437
assert first_res(DATA) == 2104783

assert second_res(test_input) == 24933642
assert second_res(DATA) == 5883165
