/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        // [1] -> [2] -> [3] -> [4]
        // [1] <- [2] <- [3] <- [4]
        if (head == null) return head;
        ListNode curr = head;
        ListNode next = null;
        ListNode prev = null;
        while (curr != null) {
            next = curr.next; // The next item in the linked list
            curr.next = prev; // Swap next value of our current node to the last node we visited
            prev = curr; // Move previous up by one node
            curr = next; // Move current node up by one node, will be null if end of list
        }
        return prev;

    }
}
