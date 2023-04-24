class MyQueue {
    private Stack<Integer> S = new Stack<Integer>();
    public MyQueue() {
        
    }
    
    public void push(int x) {
        this.S.push(x);
    }
    
    public int pop() {
        Stack<Integer> temp = new Stack<Integer>();
        while(this.S.size() != 1){
            temp.push(this.S.pop());
        }
        int y = this.S.pop();
        while(temp.size() != 0){
            this.S.push(temp.pop());
        }
        return y;
    }
    
    public int peek() {
        Stack<Integer> temp = new Stack<Integer>();
        while(this.S.size() != 1){
            temp.push(this.S.pop());
        }
        int y = this.S.peek();
        while(temp.size()!=0){
            this.S.push(temp.pop());
        }
        return y;
    }
    
    public boolean empty() {
        return this.S.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
