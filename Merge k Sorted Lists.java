class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0)
            return null;
        Queue<ListNode> pq = new PriorityQueue<>((a, b) -> a.val - b.val);
        for (ListNode n : lists) {
            if (n != null)
                pq.offer(n);
        }
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        while (!pq.isEmpty()) {
            ListNode temp = pq.poll();
            curr.next = temp;
            if (temp.next != null) {
                pq.offer(temp.next);
            }
            curr = curr.next;
        }
        return dummy.next;
    }
}
