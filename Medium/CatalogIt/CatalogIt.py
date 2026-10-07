import sys
class Node:
    name: str
    parent = None
    children: list
    def __init__(self, name: str, parent, children: list):
        self.name = name
        self.parent = parent
        self.children = children
def getName(i):
    return i.name
def insert(root, i: str, b: str):
    if root.name==b:
        root.children.append(Node(i, root, []))
        root.children.sort(key=getName)
    else:
        for c in root.children:
            insert(c, i, b)
def getNames(pre, root):
    for i in root.children:
        print(pre+i.name)
        getNames(pre+"-", i)


cases = int(sys.stdin.readline().rstrip())
root = Node("None", None, [])
for caseNum in range(cases):
    term, base = sys.stdin.readline().rstrip().split(",")
    insert(root, term, base)
getNames("", root)