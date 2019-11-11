# Make a binary tree
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # My method to find if value exists
    # def findval(self, lkpval):
    #     if lkpval < self.data:
    #         if self.left is None:
    #             print(str(lkpval) + " is not found")
    #         else:
    #             self.left.findval(lkpval)
    #     elif lkpval > self.data:
    #         if self.right is None:
    #             print(str(lkpval) + " is not found")
    #         else:
    #             self.right.findval(lkpval)
    #     else:
    #         print(str(lkpval) + " is found")

    # findval method to compare the value with nodes

    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval) + " Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval) + " Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')

    # Print the tree. Going from left to right.
    def PrintTree(self):
        if self.left:  # is self.left exists
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()
print(root.findval(5))
print(root.findval(14))

# Make a binary tree that mirrors itself
#
# class Node:
#
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data
#
#     def insert(self, data):
#         if self.data:
#             if data < self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#             elif data > self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#         else:
#             self.data = data
#
#     # Print the tree. Going from left to right.
#     def PrintTree(self):
#             if self.left:  #is self.left exists
#                 self.left.PrintTree()
#             print(self.data)
#             if self.right:
#                 self.right.PrintTree()
#
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)
# root.PrintTree()
