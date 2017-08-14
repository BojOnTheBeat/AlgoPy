"""
Python implementation of a LinkedList.

"""
import copy


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        """
        String representation of a linked list
        Basically use runners technique to print out. 
        """
        contents = []
        temp = self.head

        while temp:
            contents.append(temp.data)
            temp = temp.next

        return "->".join([str(i) for i in contents])

    def search(self, item):
        """
        search for a specific item in the linked list
        If item exists return true, else return false
        """
        temp = self.head

        while(temp):
            if temp.data == item:
                return True
            temp = temp.next

        return False

    def reverse(self):
        """
        Reverse a linked list
        """

        '''
        1->2->3 .... 3->2->1
        '''

        # use deep copy because python is pass-by-assignment
        curr = copy.deepcopy(self.head)
        nextNode = None
        prevNode = None

        while(curr):
            nextNode = curr.next
            curr.next = prevNode
            prevNode = curr
            curr = nextNode

        return LinkedList(prevNode)

    # insert at the start

    def prepend(self, item):
        """
        Insert a node at the start of a linked list
        """

        new = Node(item, self.head)

        self.head = new

    # insert at the end

    # insert after element

    # insert in the middle

    # check if ll contains a loop/cycle

    # size

    # delete element

    # determine the kth element

    # determine kth element from the end

    # check if ll is a palindrome

    # find middle element in one pass

    # remove duplicate nodes in an UNSORTED linked list

    # check if sorted

    # sort

    # find the intersection of two linked lists

    # find the frequency of an element

    # see if elements are unique





