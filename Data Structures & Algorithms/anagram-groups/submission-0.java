class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<>();
        HashMap<String, List<String>> freq = new HashMap<>();

        for (String s: strs) {
            int[] alpha = new int[26];
            List<String> sList = new ArrayList<>();
            for (int i=0; i<s.length(); i++) {
                alpha[s.charAt(i) - 'a'] += 1;
            }
            String key = Arrays.toString(alpha);
            if (freq.get(key) == null) {
                sList.add(s);
                freq.put(key, sList);
            }
            else {
                sList = freq.get(key);
                sList.add(s);
                freq.put(key, sList);
            }
        }

        for (Map.Entry<String, List<String>> entry : freq.entrySet()) {
            result.add(entry.getValue());
        }

        return result;
    }
}
