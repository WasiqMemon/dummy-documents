import math
#import openpyxl
'''

    2
   / \
  0   5
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class BST:
    def __init__(self, root):
        self.root = root
        self.size = 0
        self.maxsize = 0
        self.depth = 0

    def insert(self, root, key):
        # print(key)
        newNode = Node(key)
        depth = 0
        if self.root != None:
            current = self.root
        current = root
        parent = None
        while (current != None):
            parent = current
            if (key[0] < current.val[0]):
                current = current.left
            else:
                current = current.right
            depth += 1

        if parent == None:
            parent = newNode
            self.root = root
        elif (key[0] < parent.val[0]):
            parent.left = newNode
        else:
            parent.right = newNode
        self.size += 1  # working fine
        # checking if balancing is needed
        self.maxsize = max(self.maxsize, self.size)
        if depth > math.log(self.size, 3/2):
            ''' errors in this part of the code '''
            # finding the scapegoat
            scape = self.findScapegoat(self.root, newNode)
            if scape == None:
                return
            temp = self.rebalance(scape)
            # Assign the correct pointers to and from scapegoat
            scape.left = temp.left
            scape.right = temp.right
            scape.key = temp.key
            scape.left.parent = scape
            scape.right.parent = scape
        return parent

    def sizeOfSubtree(self, node):
        if node == None:
            return 0
        return 1 + self.sizeOfSubtree(node.left) + self.sizeOfSubtree(node.right)

    def isBalancedAtNode(self, node):
        if node == None:
            return False
        if node.left == None or node.right == None:
            if node.left == None:
                valeft = 0
            else:
                valright = 0
        valeft = self.sizeOfSubtree(node.left)
        valright = self.sizeOfSubtree(node.right)
        # print(valeft, valright)
        if abs(valeft - valright) <= 1:
            # print('isbalance', node.val)
            return True
        return False

    def findScapegoat(self, root, node):
        # print('find scapegoat', node.val)
        if node == root:
            return None
        while self.isBalancedAtNode(node) == True:
            if node == root:
                return None
            node = node.parent
        return node

    def rebalance(self, root):
        def flatten(node, nodes):
            if node == None:
                return
            flatten(node.left, nodes)
            nodes.append(node)
            flatten(node.right, nodes)

        def buildTreeFromSortedList(nodes, start, end):
            if start > end:
                return None
            mid = int(math.ceil(start + (end - start) / 2.0))
            node = Node(nodes[mid].key)
            node.left = buildTreeFromSortedList(nodes, start, mid-1)
            node.right = buildTreeFromSortedList(nodes, mid+1, end)
            return node

        nodes = []
        flatten(root, nodes)
        return buildTreeFromSortedList(nodes, 0, len(nodes)-1)

    def search(self, root, key):

        current = root
        parent = None
        while (current.val[0] != key):
            parent = current
            if (key < current.val[0]):
                current = current.left
            else:
                current = current.right

        return current.val

    def remove(key):
        pass  # implement this function

    # Outputing the data
    def Inorder(self, root):

        if (root == None):
            return
        else:
            self.Inorder(root.left)
            # print(root.val)
            self.Inorder(root.right)


def main():
    # Input list
    data = excel_data()
    root = None
    bst = BST(root)
    root = bst.insert(root, data[0])
    for i in range(1, len(data) - 1):
        bst.insert(root, data[i])
        # print(data[i])
    bst.Inorder(root)
    print(bst.search(root, 'e'))


def excel_data():
    # loc = 'data.xlsx'
    # wb = openpyxl.load_workbook(loc)
    # sheet = wb.active
    # data = []
    # for row in sheet.iter_rows(max_row=sheet.max_row):
    #     temp = []
    #     for cell in row:
    #         if len(temp) < 2:
    #             temp.append(cell.value)
    #     data.append(temp)
    # # correcting the data
    # for i in data:
    #     i[0] = i[0].replace('\n', "")
    #     i[1] = i[1].replace('\n', "")
    l1 = ['a', 34, 65]
    l2 = ['b', 35, 65]
    l3 = ['c', 36, 65]
    l4 = ['d', 39, 65]
    l5 = ['e', 37, 65]
    l6 = ['f', 38, 65]
    data = [l2, l1, l4, l5, l3, l6]
    return data

    # root = None
    # bst = BST(root)
    # root = bst.insert(root, 50)
    # bst.insert(root, 30)
    # bst.insert(root, 20)
    # bst.insert(root, 40)
    # bst.insert(root, 70)
    # bst.insert(root, 60)
    # bst.insert(root, 80)
    # bst.insert(root, 100)
    # bst.insert(root, 10)
    # bst.insert(root, 230)
    # bst.insert(root, 650)
    # bst.insert(root, 450)
    # bst.insert(root, 90)

    # # Prinoder traversal of the BST
    # bst.Inorder(root)
# main()
