class ListNode:
    """
    Class representing a node in a singly linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val           # Integer value stored in the node
        self.next = next         # Reference to the next node

def print_linked_list(head):
    """
    Prints all the elements of a linked list.
    :param head: The head node of the linked list.
    :return: None
    """
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

def add_node_at_end(head, val):
    """
    Adds a new node at the end of a linked list.
    :param head: The head node of the linked list.
    :param val: Integer value to store in the new node.
    :return: The head node of the linked list after adding the new node.
    """
    new_node = ListNode(val)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

def free_linked_list(head):
    """
    Frees a linked list.
    :param head: The head node of the linked list.
    :return: None
    """
    while head:
        temp = head
        head = head.next
        del temp

def insert_node(head, val):
    """
    Inserts a new node at the right position in a sorted linked list.
    :param head: The head node of the sorted linked list.
    :param val: Integer value to store in the new node.
    :return: The head node of the linked list after inserting the new node.
    """
    new_node = ListNode(val)
    if not head or val <= head.val:
        new_node.next = head
        return new_node
    current = head
    while current.next and current.next.val < val:
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head

