class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> freq = new HashMap<>();
        int[] result = new int[k];
        List<Integer>[] bucket = new List[nums.length + 1];

        for (int i: nums) {
            if (!freq.containsKey(i)) freq.put(i, 1);
            else freq.put(i, freq.get(i)+1);
        }
        System.out.println(freq);
        for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
            if (bucket[entry.getValue()-1] == null) bucket[entry.getValue()-1] = new ArrayList<>();
            bucket[entry.getValue()-1].add(entry.getKey());
        }
        int i = bucket.length - 1;
        while (k > 0 && i >= 0) {
            if (bucket[i] != null) {
                for (int j : bucket[i]){
                    result[k-1] = j;
                    k--;
                }
                
            }
            i--;
        }
        return result;
    }
}
