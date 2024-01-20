import linked_list as ll


def test_insert():
    llist = ll.LinkedList()
    llist.insert_at_beginning(1)
    llist.insert_at_beginning(2)
    assert llist.head.data == 2
    assert llist.head.next.data == 1

def test_reverse():
    llist = ll.LinkedList()
    llist.insert_at_end(1)
    llist.insert_at_end(2)
    llist.insert_at_end(3)
    llist.reverse_list()
    assert llist.print_list() == [3, 2, 1]
    return "test_reverse passed"

def test_sort():
    llist = ll.LinkedList()
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(3)
    llist.insert_at_beginning(4)
    llist.sort_list()
    assert llist.print_list() == [3, 4, 5]   
    return "test_sort passed"

def test_merge():
    llist1 = ll.LinkedList()
    llist1.insert_at_beginning(5)
    llist1.insert_at_beginning(3)
    llist1.insert_at_beginning(4)
    llist2 = ll.LinkedList()
    llist2.insert_at_beginning(2)
    llist2.insert_at_beginning(0)
    llist2.insert_at_beginning(1)
    llist1.merge_sorted_lists(llist2)
    assert llist1.print_list() == [0, 1, 2, 3, 4, 5]
    return "test_merge passed"

if __name__ == "__main__":
    print(test_reverse())
    print(test_sort())   
    print(test_merge())