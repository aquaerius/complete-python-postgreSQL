from linkedlist import LinkedList


class LinkedQueue:
    """
    This class is a queue wrapper around a LinkedList.

    This means that methods like `add_to_list_start` should now be called `push`, for example.

    Don't modify class or method names, just implement methods that currently raise
    a NotImplementedError!
    """

    def __init__(self):
        self.__linked_list = LinkedList()

    def push(self, node):
        """
        You should implement this method.
        It should add a node to the linked list property.
        :param node: The Node to add
        :return: None
        """
        raise NotImplementedError()

    def pop(self):
        """
        You should implement this method.
        It should remove a node from the end of the linked list, and return
        the removed node.
        :return: Node, the last node of the linked list after being removed.
        """
        raise NotImplementedError()

    def find(self, name):
        return self.__linked_list.find(name)

    def print_details(self):
        self.__linked_list.print_list()

    def __len__(self):
        """
        You should implement this method.
        It should return the amount of Nodes in the linked list.
        :return:
        """
        raise NotImplementedError()
