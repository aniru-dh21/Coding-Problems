class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        if (source == destination) return true;
        HashMap<Integer, ArrayList<Integer>> hm = new HashMap<>();
        HashSet<Integer> visited = new HashSet<>();
        Stack<Integer> L = new Stack<>();
        ArrayList<Integer> a;

        for(int i=0; i<edges.length; i++) {
            if (hm.containsKey(edges[i][0])) {
                a = hm.get(edges[i][0]);
            } else {
                a = new ArrayList<Integer>();
            }
            a.add(edges[i][1]);
            hm.put(edges[i][0],a);
            if (hm.containsKey(edges[i][1])) {
                a = hm.get(edges[i][1]); 
            } else {
                a = new ArrayList<Integer>();
            }
            a.add(edges[i][0]);
            hm.put(edges[i][1], a);
        }

        L.push(source);

        while (!L.empty()) {
            int node = L.pop();
            if(visited.contains(node) || !hm.containsKey(node)) {
                continue;
            }
            if(node == destination) {
                return true;
            }
            visited.add(node);
            for(Integer each: hm.get(node)) {
                L.push(each);
            }
        }
        return false;
    }
}
