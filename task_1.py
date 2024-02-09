class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    # Метод для реверсування списку
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def sort(self):
        self.head = self.merge_sort(self.head)

    # Метод для сортування списку
    def merge_sort(self, head):
        if head is None or head.next is None:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        sorted_list = self.sorted_merge(left, right)
        return sorted_list

    def get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sorted_merge(self, a, b):
        result = None

        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)

        return result
    
    # Метод для об'єднання двох відсортованих списків
    @staticmethod
    def merge_sorted_lists(head1, head2):
        dummy = Node()
        tail = dummy

        while head1 and head2:
            if head1.data < head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        tail.next = head1 or head2
        return dummy.next
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

# Приклад використання
llist = LinkedList()

# Додавання елементів
llist.insert_at_end(3)
llist.insert_at_end(1)
llist.insert_at_end(2)
llist.insert_at_end(5)
llist.insert_at_end(4)

print("Оригінальний список:")
llist.print_list()

# Реверсування списку
llist.reverse()
print("\nРеверсований список:")
llist.print_list()

# Сортування списку
llist.sort()
print("\nВідсортований список:")
llist.print_list()

# Створення та об'єднання двох відсортованих списків
llist1 = LinkedList()
llist2 = LinkedList()
llist1.insert_at_end(1)
llist1.insert_at_end(3)
llist1.insert_at_end(5)
llist2.insert_at_end(2)
llist2.insert_at_end(4)
llist2.insert_at_end(6)

merged_head = LinkedList.merge_sorted_lists(llist1.head, llist2.head)
merged_list = LinkedList()
merged_list.head = merged_head
print("\nОб'єднаний відсортований список:")
merged_list.print_list()