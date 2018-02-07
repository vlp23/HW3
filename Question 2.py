
class Node:
    """ base class """
    def __init__(self, name, cost, utility):
        """
        :param name: name of this node
        :param cost: cost of this node
        :param utility: utility of this node
        """
        self.name = name
        self.cost = cost
        self.utility = utility

    def get_expected_cost(self):
        """ abstract method to be overridden in derived classes
        :returns expected cost of this node """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def get_expected_utility(self):
        '''abstract method to be overridden in derived classes
        :returns expected utility of this node'''
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes")

class ChanceNode(Node):

    def __init__(self, name, cost, future_nodes, probs, utility):
        """
        :param future_nodes: future nodes connected to this node
        :param probs: probability of the future nodes
        :param utility: utility
        """
        Node.__init__(self, name, cost, utility)
        self.futureNodes = future_nodes
        self.probs = probs
        self.utility = utility

    def get_expected_cost(self):
        """
        :return: expected cost of this chance node
        """
        exp_cost = self.cost  # expected cost initialized with the cost of visiting the current node
        i = 0
        for node in self.futureNodes:
            exp_cost += self.probs[i]*node.get_expected_cost()
            i += 1
        return exp_cost

    def get_expected_utility(self):
        '''

        :return: expected utility of this chance node
        '''

        exp_utility = self.utility
        i=0
        for node in self.futureNodes:
            exp_utility += self.probs[i]*node.get_expected_utility()
            i +=1
        return exp_utility



class TerminalNode(Node):

    def __init__(self, name, cost, utility):
        Node.__init__(self, name, cost, utility)

    def get_expected_cost(self):
        """
        :return: cost of this chance node
        """
        return self.cost

    def get_expected_utility(self):
        '''

        :return: utility of this chance node
        '''
        return self.utility

class DecisionNode(Node):

    def __init__(self, name, cost, future_nodes, utility):
        Node.__init__(self, name, cost, utility)
        self.futureNode = future_nodes

    def get_expected_costs(self):
        """ returns the expected costs of future nodes"""
        outcomes = dict() # dictionary to store the expected cost of future nodes along with their names as keys
        for node in self.futureNode:
            outcomes[node.name] = node.get_expected_cost()

        return outcomes

    def get_expected_utility(self):
        "returns the expected utility of future nodes"
        outcomes =dict() #dictionary to store the expected utility of future nodes along with their names as keys
        for node in self.futureNode:
            outcomes[node.name]=node.get_expected_utility()

        return outcomes


#######################
# See figure DT3.png (from the project menu) for the structure of this decision tree
########################

# create the terminal nodes
T1 = TerminalNode('T1', 10, .9)
T2 = TerminalNode('T2', 20, .8)
T3 = TerminalNode('T3', 30, .7)
T4 = TerminalNode('T4', 40, .6)
T5 = TerminalNode('T5', 50, .5)

# create C2
C2 = ChanceNode('C2', 35, [T1, T2], [0.3, 0.7], 0)
# create C1
C1 = ChanceNode('C1', 25, [C2, T3], [0.2, 0.8], 0)
# create C3
C3 = ChanceNode('C3', 45, [T4, T5], [0.1, 0.9], 0)

# create D1
D1 = DecisionNode('D1', 0, [C1, C3], 0)

# print the expect cost of C1
print(D1.get_expected_costs())

#print the expected utility

print (D1.get_expected_utility())
