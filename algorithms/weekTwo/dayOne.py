class Node(object):
    def __init__(self, value):
        self.val = value
        self.next = None

class SLL(object):
    def __init__(self):
        self.head = None

    def display_values(self):
        runner = my_list.head
        while(runner != None):
            print(runner.val)
            runner = runner.next

    def find_max(self):
        # return the max value of the list
        pass

    def is_empty(self):
        # return a boolean on whether on not there are nodes in the list
        if self.head == None:
            return True
        else:
            return False
    
    def front(self):
        # return the first value in list
        pass

    def add_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        # add a new node to the beginning of the list

    def remove_front(self):
        # return node removed from list
        if self.is_empty() == True:
            return None
        else:
            node_to_remove = self.head
            self.head = self.head.next
            return node_to_remove

    def add_back(self, value):
        # add a node to the end of the list
        pass

    def remove_back(self):
        # remove and return the last node of the list
        pass




# Creating the SLL
my_list = SLL()
print(my_list)

my_list.add_front(8)
# print(my_list.is_empty())

my_list.add_front(7)
my_list.add_front(6)
my_list.display_values()
print(my_list.remove_front())
my_list.display_values()



# print(my_list.is_empty())
# # True
# my_list.add_front(4)
# print(my_list.front())
# # should print 4
# print(my_list.is_empty())
# # False

# # Add Nodes to list
# my_first_node = Node(4)
# print(my_first_node)

# my_list.head = my_first_node
# print(my_list.head)

# my_second_node = Node(8)
# print(my_second_node)
# my_first_node.next = my_second_node
# print(my_list.head.next)

# my_third_node = Node(2)
# my_second_node.next = my_third_node
# print(my_third_node)
# print(my_list.head.next.next)
# # End of adding Nodes to list

# # access values in the SLL
# my_list.display_values()
# max_value = my_list.find_max()
# print(max_value)
# # should print 8

# # # my_list.head = my_second_node
# # print('8'*40)
# # runner = my_list.head
# # print(runner)
# # print(runner.val)
# # print(my_list.head)
# # print(my_first_node)
# # print('8'*40)
# # runner = runner.next
# # print(runner)
# # print(runner.val)
# # print(my_second_node)
# # print('8'*40)
# # runner = runner.next
# # print(runner)
# # print(runner.val)
# # print(my_third_node)
# # print('8'*40)
# # runner = runner.next
# # print(runner)
# # # print(my_third_node)
# # print('8'*40)

# # runner = my_list.head

# # while(runner != None):
# #     print(runner.val)
# #     runner = runner.next