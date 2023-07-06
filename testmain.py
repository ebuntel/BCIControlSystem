from ControlTree import ControlTree
from DecisionNode import DecisionNode

def main():
    init_head = DecisionNode()
    init_head.content = "Head"
    init_head.ID = "0"

    tree = ControlTree()
    tree.manual_add_node(init_head)
    child_1 = DecisionNode("Child 1", tree.position)
    child_1._manual_set_ID("1A")
    tree.manual_add_node(child_1)
    child_2 = DecisionNode("Child 2", tree.position)
    child_2._manual_set_ID("1B")
    tree.manual_add_node(child_2)
    child_3 = DecisionNode("Child 3", tree.position)
    child_3._manual_set_ID("1C")
    tree.manual_add_node(child_3)

    tree.manual_move(tree.head.children[0])
    child_1_1 = DecisionNode("Child 1.1", tree.position)
    child_1_1._manual_set_ID("2A")
    tree.manual_add_node(child_1_1)
    child_1_2 = DecisionNode("Child 1.2", tree.position)
    child_1_2._manual_set_ID("2B")
    tree.manual_add_node(child_1_2)
    tree.manual_reset_position()

    tree.manual_move(tree.head.children[1])
    child_2_1 = DecisionNode("Child 2.1", tree.position)
    child_2_1._manual_set_ID("2C")
    tree.manual_add_node(child_2_1)
    child_2_2 = DecisionNode("Child 2.2", tree.position)
    child_2_2._manual_set_ID("2D")
    tree.manual_add_node(child_2_2)
    tree.manual_reset_position()

    tree.manual_move(tree.head.children[2])
    child_3_1 = DecisionNode("Child 3.1", tree.position)
    child_3_1._manual_set_ID("2E")
    tree.manual_add_node(child_3_1)
    child_3_2 = DecisionNode("Child 3.2", tree.position)
    child_3_2._manual_set_ID("2F")
    tree.manual_add_node(child_3_2)
    tree.manual_reset_position()
    
    tree.manual_decide()
    print("Position: ", tree.position.content)

    tree.manual_decide()
    print("Position: ", tree.position.content)

if __name__ == "__main__":
    main()