class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
def sort_list(list1, list2):
    head = Node()
    last_node = head
    while list1 and list2:
        if list1.data <= list2.data:
            last_node.next = list1
            list1 = list1.next
        else:
            last_node.next = list2
            list2 = list2.next
        last_node = last_node.next
    if list1:
        last_node.next = list1
    if list2:
        last_node.next = list2
    return head.next
list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(3)
list2 = Node(4)
list2.next = Node(5)
list2.next.next = Node(6)
sorted_list = sort_list(list1, list2)
while sorted_list:
    print(sorted_list.data, end=" ")
    sorted_list = sorted_list.next
