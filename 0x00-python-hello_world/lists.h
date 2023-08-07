class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_list(head):
    """
    Prints the elements of a linked list.
    
    Args:
        head (ListNode): The head node of the linked list.
        
    Returns:
        int: The number of nodes in the linked list.
    """
    count = 0
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
        count += 1
    print("None")
    return count

def add_node(head, val):
    """
    Adds a new node with the given value to the beginning of the linked list.
    
    Args:
        head (ListNode): The head node of the linked list.
        val (int): The value to be added to the new node.
        
    Returns:
        ListNode: The new head node of the linked list.
    """
    new_node = ListNode(val)
    new_node.next = head
    return new_node

def free_list(head):
    """
    Frees the memory allocated for a linked list.
    
    Args:
        head (ListNode): The head node of the linked list.
    """
    while head:
        temp = head
        head = head.next
        del temp

def has_cycle(head):
    """
    Checks if a linked list has a cycle.
    
    Args:
        head (ListNode): The head node of the linked list.
        
    Returns:
        bool: True if a cycle is present, False otherwise.
    """
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

