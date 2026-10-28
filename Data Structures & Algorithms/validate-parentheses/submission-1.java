class Solution {
    public boolean isValid(String s) {
        char p1 = '(';
        char p2 = ')';
        char s1 = '[';
        char s2 = ']';
        char c1 = '{';
        char c2 = '}';


        Stack<Character> stack = new Stack<>();
        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if (c == p1 || c == s1 || c == c1) {
                stack.push(c);
            } else {
                if (stack.empty()) return false;
                if (stack.peek() == p1  && c == p2) {
                    stack.pop();
                } else if (stack.peek() == s1 && c == s2) {
                    stack.pop();
                } else if (stack.peek() == c1 && c == c2) {
                    stack.pop();
                } else return false;
            }
        }
        return stack.empty();
    }
}
