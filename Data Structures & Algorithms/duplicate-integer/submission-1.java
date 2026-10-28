class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> setNums = new HashSet<>();
        for (int n : nums) {
            setNums.add(n); 
        }
        return nums.length != setNums.size();
    }
}