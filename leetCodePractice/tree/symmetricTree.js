/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
 var isSymmetric = function(root) {

    if (root === null) return false;
    
    
    let leftStack = [root.left];
    let rightStack = [root.right];
    
    while (leftStack.length && rightStack.length) {
        
        let currLeft = leftStack.pop();
        let currRight = rightStack.pop();
        if (currLeft && !currRight) {
            return false;
        }
        if (!currLeft && currRight) {
            return false;
        }
        if (!currLeft && !currRight) {
            continue;
        }
        if (currLeft.val !== currRight.val) {
            return false;
        }
        leftStack.push(currLeft.left, currLeft.right);
        rightStack.push(currRight.right, currRight.left);
    }
    if (leftStack.length !== rightStack.length) {
            return false;
    }
    return true;
    
};