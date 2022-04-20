class BSTNode:
    def __init__(self,info=None,val=None):
        self.val = val
        self.right = None
        self.left = None
        self.info = info
    def insert(self,info, val):
        if not self.val:
            self.val = val
            self.info = info
            return
        if self.val == val:
            return
        if val < self.val:
            if self.left:
                self.left.insert(info,val)
                return
            self.left = BSTNode(info,val)
            return
        if self.right:
            self.right.insert(info,val)
            return
        self.right = BSTNode(info,val)
    def find(self, val):
        if val == self.val:
            return self.info

        if val < self.val:
            if self.left == None:
                return -1
            return self.left.find(val)

        if self.right == None:
            return -1
        return self.right.find(val)


