
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
 * @return {TreeNode}
 */
 var invertTree = function(root) {
    if (!root) {
        return null;
    }
    let newTree = new TreeNode(root.val);
     newTree.left = invertTree(root.right);
     newTree.right = invertTree(root.left);
     
     return newTree;
     
     
 };