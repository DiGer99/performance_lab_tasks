class Node:
    head = None

    def __init__(self, value):
        self.value = value
        self.next_node = None

        if Node.head is None:
            Node.head = self


def way_array(
    n: int,
    m: int,
) -> str:
    Node.head = None
    head = Node(1)
    current = head
    res = []
    for num in range(2, n + 1):
        current.next_node = Node(num)
        current = current.next_node

    current.next_node = head
    res.append(head.value)
    current = head

    for i in range(m - 1):
        current = current.next_node

    while current != head:
        res.append(current.value)
        for i in range(m - 1):
            current = current.next_node

    return "".join(map(str, res))
