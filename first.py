class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next 
            current.next = prev      
            prev = current          
            current = next_node     
        self.head = prev  

    def sort(self):
        self.head = self.mergeSort(self.head)

    def mergeSort(self, head):
        if not head or not head.next:
            return head

        middle = self.getMiddle(head)
        next_to_middle = middle.next

        middle.next = None   

        left = self.mergeSort(head)
        right = self.mergeSort(next_to_middle)

        sorted_list = self.sortedMerge(left, right)
        return sorted_list

    def getMiddle(self, head):
        if not head:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sortedMerge(self, a, b):
        if not a:
            return b
        if not b:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result

def mergeTwoLists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    else:
        tail.next = l2

    return dummy.next


llist = LinkedList()
llist.insert(3)
llist.insert(1)
llist.insert(4)
llist.insert(2)

print("Початковий список:")
llist.printList()

llist.reverse()
print("Реверсований список:")
llist.printList()

llist.sort()
print("Відсортований список:")
llist.printList()

llist2 = LinkedList()
llist2.insert(5)
llist2.insert(0)
llist2.sort()

print("Другий відсортований список:")
llist2.printList()

merged_head = mergeTwoLists(llist.head, llist2.head)
merged_list = LinkedList()
merged_list.head = merged_head

print("Об'єднаний відсортований список:")
merged_list.printList()

