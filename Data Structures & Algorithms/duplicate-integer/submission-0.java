class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet frequencies = new HashSet<>();
        for (int i=0; i<nums.length; i++) {
            frequencies.add(nums[i]);
        }
        return (frequencies.size() != nums.length);
    }
}