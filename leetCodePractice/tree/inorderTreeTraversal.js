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
 * @return {number[]}
 */
 var inorderTraversal = function(root) {
    let result = [];
    
    const dfs = (root) => {
        if (root === null) {
            return;
        }
        console.log(root.val)
        if (root.left) {
            dfs(root.left);
        }
        if (root.val !== null) {
            result.push(root.val);
        }
        if (root.right) {
            dfs(root.right);
        }
        return;
    }
    dfs(root);
    return result;
    
};