class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> sum = new HashMap<>();
        int[] indexArray = new int[2];
        int i = 0;
        while (true) {
            int diff = target - nums[i];
            if (sum.get(nums[i]) != null) {
                if (sum.get(diff) != null) {
                    int j = sum.get(diff);
                    if (j != i) {
                        if (i > j) {
                            indexArray[0] = j;
                            indexArray[1] = i;
                        } else {
                            indexArray[0] = i;
                            indexArray[1] = j;
                        }
                        return indexArray;
                    }
                }
            } else {
                sum.put(nums[i], i);
            }
            if (i < nums.length - 1) {
                i++;
            } else {
                i = 0;
            }
        }
    }
}
