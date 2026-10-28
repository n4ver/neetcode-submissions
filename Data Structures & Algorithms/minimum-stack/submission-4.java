class MinStack {

    private Stack<Integer> stack;
    private Stack<Integer> minStack;
    private Integer minimum = Integer.MAX_VALUE;

    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }
    
    public void push(int val) {
        stack.push(val);
        if (val < minimum) {
            minimum = val;
        }
        minStack.push(minimum);
    }
    
    public void pop() {
        stack.pop();
        minStack.pop();
        
        if (!minStack.empty()) minimum = minStack.peek();
        else minimum = Integer.MAX_VALUE;
        System.out.println(minimum);
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
