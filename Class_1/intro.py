"""
Jen drives her ice cream truck to her local elementary school at recess. All the kids rush to line up
in front of her truck. Jen is overwhelmed with the number of students (there are 2n of them), so
she calls up her associate, Berry, to bring his ice cream truck to help her out. Berry soon arrives
and parks at the other end of the line of students. He offers to sell to the last student in line, but the
other students revolt in protest: “The last student was last! This is unfair!”

The students decide that the fairest way to remedy the situation would be to have the back half of
the line (the n kids furthest from Jen) reverse their order and queue up at Berry’s truck, so that the
last kid in the original line becomes the last kid in Berry’s line, with the (n+1)st kid in the original
line becoming Berry’s first customer.

(a) Given a linked list containing the names of the 2n kids, in order of the original line
formed in front of Jen’s truck (where the first node contains the name of the first kid
in line), describe an O(n)-time algorithm to modify the linked list to reverse the order
of the last half of the list. Your algorithm should not make any new linked list
"""
class Node():
    def __init__(self, item = None) -> None:
        self.item = item
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None

    def print(self):
        if self.head == None:
            print ("Empty LinkedList")
            return

        printStr = ""
        current = self.head
        while (current):
            printStr += f"{current.item} -> "
            current = current.next

        print(printStr)


    def insert_at_end(self, item):
        if self.head == None:
            self.head = Node(item)
            return

        current = self.head
        while (current.next):
            current = current.next

        current.next = Node(item)

    def insert_many(self, items):
        for item in items:
            self.insert_at_end(item)



students = LinkedList()
students.insert_many(["Joe", "James", "Martha"])
students.print()