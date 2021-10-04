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
        self.length = 0

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
            self.length += 1
            return

        current = self.head
        while (current.next):
            current = current.next

        current.next = Node(item)
        self.length += 1

    def insert_many(self, items):
        for item in items:
            self.insert_at_end(item)

    def insert_with_S_names(self, count):
        """Test method to insert `count` students with names like S1, S2, etc."""
        for i in range(1, count+1):
            self.insert_at_end(f"S{i}")


    def reverse_second_half(self):
        """ O(n)-time  algorithm to modify the linked list to reverse the order
            of the last half of the list. Your algorithm should not make any new linked list 
            or instantiate any new non-constant-sized data structures during its operation"""
        
        # S1, S2, S3, * S4, S5, S6 *
        # S1, S2, S3, * S6, S5, S4 *
        
        # S1, S2, S3, S4, * S5, S6, S7, S8 *
        # S1, S2, S3, S4, * S8, S7, S6, S5 *

        n = int(self.length / 2)
        currentItem: Node = self.head

        # skip ahead to find last item in Jen's list
        for _ in range(n - 1):
            currentItem = currentItem.next

        jensLastStudent = currentItem # have to point this to the last item later
        bensFirstStudent = currentItem.next # have to point this to nothing later
        previousItem = currentItem
        currentItem = currentItem.next

        for _ in range(n):
            nextItem = currentItem.next # grab nextItem since we are about to overwrite it
            currentItem.next = previousItem # assign next item to previous item, the key idea of this algorithm
            previousItem, currentItem = currentItem, nextItem # move the pointers forward so we can do it all over again

        jensLastStudent.next = previousItem
        bensFirstStudent.next = None

students = LinkedList()
students.insert_with_S_names(8)
students.print()
students.reverse_second_half()
students.print()

students2 = LinkedList()
students2.insert_with_S_names(4)
students2.print()
students2.reverse_second_half()
students2.print()

students3 = LinkedList()
students3.insert_with_S_names(100)
students3.print()
students3.reverse_second_half()
students3.print()