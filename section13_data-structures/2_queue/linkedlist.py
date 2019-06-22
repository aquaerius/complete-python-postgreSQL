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
        if node:
            node.set_next(self.__root)
        self.__root = node

    def remove_end_from_list(self):
        marker = self.__root
        while marker:
            # Get the following node
            next_node = marker.get_next()
            # Verify it's not None
            if next_node:
                # Check if next node is None
                if not next_node.get_next():
                    # Set the value of marker's next node to None
                    marker.set_next(None)
                    removed_node = next_node
                    return removed_node
                marker = next_node
            else:
                self.__root = None
                return marker

    def print_list(self):
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()

    def find(self, name):
        marker = self.__root
        while marker:
            if marker.name == name:
                return marker
            marker = marker.get_next()
        raise LookupError("Name {} was not found in the linked list.".format(name))

    def size(self):
        marker = self.__root
        size = 0
        while marker:
            size += 1
            marker = marker.get_next()
        return size
