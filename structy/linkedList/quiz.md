1) What is the optimal complexity we can achieve for searching for a target value in a standard, singly linked-list?

A: O(n) time and O(1) space if we do it iteratively. O(n) time and O(n) space if we do it recursively. 

2) What two properties are typically stored in the nodes of a singly linked-list?

A: Value and next. Value is the data stored and next is the reference to the next sequential node in the list. 

3) What term is commonly used for the last node in the linked-list?

A: Tail

4) What term is commonly used to describe the 'first node' of a linked list?

A: Head

5) What is the 'dummy head' pattern for linked lists?

A: The 'dummy head' pattern is where we use a fake node to act as the head of the linked list. The dummy node is used to simplify edge cases such as inserting the first node into an empty linked list. 

6) Why might the expression current.next.val be unsafe?

A: If current is the tail node, the expression throws an error because current.next is null and null does not have a val propoerty. 