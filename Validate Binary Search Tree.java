class Solution {
    long prev=Long.MIN_VALUE;
    public boolean inOrder(TreeNode root){
        if(root==null)
            return true;
        boolean x=inOrder(root.left);
        if (prev>=root.val)
            return false;
        prev=root.val;
        boolean y=inOrder(root.right);
        if(x==false||y==false)
            return false;
        return true;
    }
    public boolean isValidBST(TreeNode root) {
        ArrayList <Integer> l1=new ArrayList<>();
        return inOrder(root);
    }
}
