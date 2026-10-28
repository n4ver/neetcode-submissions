class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> sHash = new HashMap<>();
        for (int i=0; i < s.length(); i++) {
            if (sHash.containsKey(s.charAt(i))) {
                sHash.put(s.charAt(i), sHash.get(s.charAt(i)) + 1);
            } else {
                sHash.put(s.charAt(i), 1);
            }
        }
        for (int i=0; i < t.length(); i++) {
            if (sHash.containsKey(t.charAt(i))) {
                sHash.put(t.charAt(i), sHash.get(t.charAt(i)) - 1);
            } else {
                return false;
            }
        }
        for (Map.Entry<Character, Integer> e : sHash.entrySet()) {
            if (sHash.get(e.getKey()) != null) {
                if (sHash.get(e.getKey()) > 0) { return false; }
            }
        }
        return true;
    }
}
