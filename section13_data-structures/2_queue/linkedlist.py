class LinkedList:
    """
    You should implement the methods of this class which are currently
    raising a NotImplementedError!
    Don't change the name of the class or any of the methods.
    """
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add_start_to_list(self, node):
        """
        You can reuse the method written for the previous assignment here.

        :param node: the node to add at the start
        :return: None
        """
        raise NotImplementedError()

    def remove_end_from_list(self):
        """
        Implement this method! It should:
        - Iterate over each node
        - Find both the second-to-last node and the last node
        - Set the second-to-last node's next to be None
        - Return the last node
        :return: the removed Node.
        """
        raise NotImplementedError()

    def print_list(self):
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()

    def find(self, name):
        """
        You can reuse the method written for the previous assignment here.

        :param name: the name of the Node to find.
        :return: the found Node, or raises a LookupError if not found.
        """
        raise NotImplementedError()

    def size(self):
        """
        You should implement this method!
        It should return the amount of Nodes in the list.
        :return: the amount of nodes in this list.
        """
        raise NotImplementedError()
