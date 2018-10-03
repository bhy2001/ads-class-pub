class Node:
    def __init__(self, init_value):
        self._value = init_value
        self._next = None
    
    def get_data(self):
        return self._value

    def set_data(self, new_data):
        self._value = new_data
    
    data = property(get_data, set_data)
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, new_next):
        self._next = new_next

    def __str__(self):
        return str(self._value)

class LinkedList:
    def __init__(self):
        self._head = None
        # self._tail = None
        self._size = 0
    
    def __len__(self) -> int:
        return self._size
    
    def __str__(self):
        list_str = '['
        current = self._head

        while current:
            list_str += str(current)
            if current.next:
                list_str += ', '
            current = current.next
        list_str += ']'
        return list_str
    
    def is_empty(self) -> bool:
        return self._head is None
    
    def size(self) -> int:
        return self._size
    
    def add(self, new_node: object) -> None:
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    def search(self, value) -> bool:
        current = self._head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def index(self, value) -> int:
        idx = 0
        current = self._head
        while current:
            if current.data == value:
                return idx
            current = current.next
            idx += 1
        return -1

    def append(self, new_node):
        pass

    def insert(self, pos: int, new_node: object) -> None:
        current = self._head
        idx = 0
        if pos <= 0:
            self.add(new_node)
            return
        if pos > self._size:
            self.append(new_node)
            return
        while idx < pos - 1:
            idx += 1
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self._size += 1


def main():
    # print('Working with nodes')
    # n = Node('A')
    # print(n.data)
    # print(n.next)
    # print(n)

    # m = Node('B')
    # n.next = m
    # print(n.next)

    print('Working with lists')
    ll = LinkedList()
    print(ll.size())  # 0
    print(type(ll))  # LinkedList
    print('Printing a list')
    print(ll)
    ll.add(Node('Q'))
    print(ll)  # [Q]
    ll.add(Node('A'))
    print(ll)  # [A, Q]
    ll.add(Node('D'))
    print(ll)  # [D, A, Q]
    print(len(ll))
    print(ll.search('Z'))
    print(ll)  # [D, A, Q]
    print(len(ll))
    print(ll.index('D'))  # 0
    print(ll)  # [D, A, Q]
    print(len(ll))
    print(ll.index('Z'))  # -1
    print(ll)  # [D, A, Q]
    print(len(ll))
    print('Inserting a new node')
    ll.insert(0, Node('K'))
    print(ll)  # [K, D, A, Q]
    print(len(ll))  # 4
    ll.insert(2, Node('M'))
    print(ll)  # [K, D, M, A, Q]
    print(len(ll))  # 5

if __name__ == '__main__':
    main()