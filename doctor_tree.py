from collections import deque

class DoctorNode:
    # A class to represent a node in the binary tree.#
    def __init__(self, name):
         self.name = name
         self.left = None
         self.right = None

class DoctorTree:
# A class to manage the overall doctor hierarchy.#
    def __init__(self):
        self.root = None

    def insert(self, supervisor_name, doctor_name, side):
        """
        Add doctor_name to the tree under supervisor_name on the given side ('left' or 'right').
        If the tree is empty, pass supervisor_name as None (or '') to create the head (root) doctor.
        Returns True on success, False otherwise.
        """
        # Create head doctor if tree is empty and no supervisor specified
        if self.root is None:
            if supervisor_name is None or supervisor_name == "":
                self.root = DoctorNode(doctor_name)
                print(f"✅ Head doctor '{doctor_name}' added as root.")
                return True
            else:
                print("⚠️ The head doctor (root) does not exist. Please add a head doctor first by passing supervisor_name=None.")
                return False

        # Find the supervisor using BFS
        q = deque([self.root])
        while q:
            node = q.popleft()
            if node.name == supervisor_name:
                if side == "left":
                    if node.left is None:
                        node.left = DoctorNode(doctor_name)
                        print(f"✅ {doctor_name} added to the LEFT of {supervisor_name}.")
                        return True
                    else:
                        print(f"⚠️ LEFT side of {supervisor_name} is already occupied.")
                        return False
                elif side == "right":
                    if node.right is None:
                        node.right = DoctorNode(doctor_name)
                        print(f"✅ {doctor_name} added to the RIGHT of {supervisor_name}.")
                        return True
                    else:
                        print(f"⚠️ RIGHT side of {supervisor_name} is already occupied.")
                        return False
                else:
                    print("❌ Invalid side. Please choose 'left' or 'right'.")
                    return False
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        print(f"❌ Supervisor '{supervisor_name}' not found in the hierarchy.")
        return False

    def print_tree(self, node=None, level=0):
        if node is None:
            if level == 0:
                if self.root is None:
                    print("⚠️ The doctor hierarchy is empty. Please add a head doctor first.")
                    return
                node = self.root
            else:
                return

        print("  " * level + "- " + node.name)
        if node.left:
            self.print_tree(node.left, level + 1)
        if node.right:
            self.print_tree(node.right, level + 1)

# Traversal methods #
    def preorder(self, node=None):
        """
        Root -> Left -> Right
        Returns a list of names.
        """
        if node is None:
            node = self.root
        def _pre(n):
            if n is None:
                return []
            return [n.name] + _pre(n.left) + _pre(n.right)
        return _pre(node)

    def inorder(self, node=None):
        """
        Left -> Root -> Right
        Returns a list of names.
        """
        if node is None:
            node = self.root
        def _in(n):
            if n is None:
                return []
            return _in(n.left) + [n.name] + _in(n.right)
        return _in(node)

    def postorder(self, node=None):
        """
        Left -> Right -> Root
        Returns a list of names.
        """
        if node is None:
            node = self.root
        def _post(n):
            if n is None:
                return []
            return _post(n.left) + _post(n.right) + [n.name]
        return _post(node)

# Test your DoctorTree and DoctorNode classes here
