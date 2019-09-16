class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.kids = []
        
    def __str__(self):
        return self.char.lower()
    
    def stuc(self):
        lev = len(self.kids)
        l = " "
        for x in range(lev):
            l += l
        print(l + self.char)
        if self.kids:
            for kid in self.kids:
                kid.stuc()
        else:
            print("this is a terminal node")
            
    def add(self, word):
        node = self
        tars = 'atcg'
        for char in word:
            char = char.lower()
            if char in tars:   # this is to get rid of the BOM char at the front
                in_kids = False
                for kid in node.kids:
                    if kid.char.lower() == char:
                        node = kid
                        in_kids = True
                        break
                if not in_kids:
                    new_node = TrieNode(char)
                    node.kids.append(new_node)
                    node = new_node

    def search(self, file):
        cur = 0
        end = 1
        pn = self
        string = file.read()
        for c in string:
            cur += 1
            if c.lower() in "catg":
                in_kids = False
                for kid in pn.kids:
                    if kid.char.lower() == c.lower():
                        in_kids = True
                        pn = kid
                        end += 1
                        break
                if not in_kids:
                    pn = self
                    end = 0
                elif len(pn.kids) == 0:
                    print("\t" + str(hex(cur-end).zfill(8)) + "\t" + string[cur-(end):cur])
                    pn = self
                    end = 0
                # else we are not at a terminal node, but we ARE still in the trie possible path   
            else:
                pn = self
                end = 0
