#Andrew Ryan
#Part 1 of assignment
def stringCount(aList):
    import collections
    newList = collections.Counter(aList)
    for key,val in sorted(newList.items()):
        print(key, val)
    return None

#Part 2 of assignment
def isFloat(value):
    if(value.find('.') > -1):
        try:
            if(float(value)):
                print("returned true")
                return True
        except:
            print("not a float")
            return False
    return False

#Part 3 of assignment
class Node(object):
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, value):
        new_node = Node(value, None)
        if self.first == None:
            self.first = new_node
            self.last = self.first
        else:
            new_node.next = self.first
            self.first = new_node
        # Use this to insert at end of list
        #     self.last.next = new_node
        # self.last = new_node

    def printLL(self):
        cur_node = self.first
        while cur_node:
            print(cur_node.value, end=" ")
            cur_node = cur_node.next
        print()

    def delete(self, value):
        cur_node = self.first
        prev_node = None
        while cur_node:
            if cur_node.value == value:
                if prev_node != None:
                    prev_node.next = cur_node.next
                else:
                    self.first = cur_node.next
            prev_node = cur_node
            cur_node = cur_node.next

    def search(self, value):
        cur_node = self.first
        while cur_node:
            if cur_node.value == value:
                return True
            else:
                cur_node = cur_node.next
        return False

    def size(self):
        count = 0
        cur_node = self.first
        while cur_node:
            count = count + 1
            cur_node = cur_node.next
        return count


# # !!! TESTING - REMOVE WHEN DONE !!!
# ll = LinkedList()
# ll.insert(1)
# ll.insert(2)
# ll.printLL()
# ll.delete(2)
# ll.printLL()
# if ll.search(2):
#     print("Value 2 found")
# else:
#     print("Value 2 not found")
# if ll.search(1):
#     print("Value 1 found")
# else:
#     print("Value 1 not found")
# ll.insert(4)
# ll.printLL()
# print(str(ll.size()))
#
# isFloat("apple")
# isFloat("%23.766")
# isFloat("!345s.5")
# isFloat("8.8.8.0")
# isFloat("4.0O0")
# isFloat("+4.0+d")
# isFloat("-x0.99")
# isFloat("8.8.80")
# isFloat("-+4.5")
# isFloat("+.4")
# isFloat(".5")
# isFloat("-.7")
# isFloat("-1.00")
# isFloat("+4.54")
#
# aList = []
# aList = ['z',"a","b","c","b","g","a","g","t",'z',"y","a"]
# stringCount(aList)
