from anytree import Node, RenderTree, findall, AsciiStyle


with open('7.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        if '$ cd' in line:
            dir_name = line.split('$ cd ')[1]
            if dir_name == '..':
                current_node = current_node.parent
            elif dir_name == '/':
                root = Node(name=dir_name, type='dir', size=0)
                current_node = root
            else:
                node, = findall(
                    current_node,
                    filter_=lambda n: n.name == dir_name and n in current_node.children,
                    maxcount=1)
                current_node = node
        elif '$ ls' in line:
            continue
        else:
            data = line.split()
            if data[0] == 'dir':
                node = Node(name=data[1], parent=current_node, type=data[0], size=0)
            else:
                node = Node(name=data[1], parent=current_node, type='file', size=int(data[0]))


print(RenderTree(root, style=AsciiStyle()).by_attr())
node_sizes = {}
current_sum = 0
dirs = findall(root, filter_=lambda n: n.type == 'dir')
res1 = 0
for d in dirs:
    d_sum = sum(node.size for node in d.descendants)
    if d_sum <= 100000:
        res1 += d_sum
print(res1)

total_space = 70000000
unused_space = 30000000
available_space = total_space - sum(node.size for node in root.descendants)
res2 = total_space
for d in dirs:
    d_sum = sum(node.size for node in d.descendants)
    cur_sum = d_sum + available_space
    if unused_space <= cur_sum and d_sum < res2:
        res2 = d_sum
print(res2)
