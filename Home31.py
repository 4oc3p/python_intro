import os

d = {}


def traverse_dir(dir, indent_level=0, out=0):
    for name in os.listdir(dir):
        if not name.startswith((".", ",", "_")):
            path = os.path.join(dir, name)
            prefix = indent_level * (" " * 4)
            # a = '/'.join(path.split("\\")[:-1])
            index = path[:path.rindex("\\")]
            d[index] = d.get(index, 0)
            if out == 0:
                if os.path.isfile(path):
                    d[index] += os.path.getsize(path)
                else:
                    traverse_dir(path, indent_level + 1, out=0)
                    d[index] += d[path]
            else:
                if os.path.isfile(path):
                    print("%s (%d bytes)" % (prefix + "╰─── " + name, os.path.getsize(path)))
                else:
                    print(prefix + name + ": %s" % d[index])
                    traverse_dir(path, indent_level + 1, out=1)

traverse_dir("D:\\folder", indent_level=0)

traverse_dir("D:\\folder", indent_level=0, out=1)
