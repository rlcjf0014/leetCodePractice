package Study.Tree;

import java.util.*;

class Solution {
    static class node {
        int data;
        node left;
        node right;
        public node(int val) {
            this.data = val;
            this.left = null;
            this.right = null;
        }
    }

    public List<List<Integer>> levelOrder(node root) {
        List<List<Integer>> res = new LinkedList<>();
        Queue<node> q = new LinkedList<>();

        if (root == null) {
            return res;
        }

        while(!q.isEmpty()) {
            int len = q.size();
            List<Integer> subres = new LinkedList<>();

            for (int i = 0; i < len; i++) {
                if (q.peek().left != null) {
                    q.offer(q.peek().left);
                }
                if (q.peek().right != null) {
                    q.offer(q.peek().right);
                }

            }
            subres.add(q.poll().data);
        }

        return res;
    }

    public static node makeTree(node root) {
        Scanner scn = new Scanner(System.in);
        System.out.println("Enter the value to put in Tree: ");
        int data = scn.nextInt();

        root = new node(data);
        if (data == -1) {
            scn.close();
            return null;
        }

        System.out.println("Enter data for left value " + data);
        root.left = makeTree(root.left);
        System.out.println("Enter data for right value " + data);
        root.right = makeTree(root.right);

        scn.close();
        return root;
    }

    public static void main(String[] args) {
        node root = null;
        root = makeTree(root);
        return;
    }

}