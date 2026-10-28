class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String s : strs) {
            sb.append(s.length());
            sb.append("#");
            sb.append(s);
        }
        return sb.toString();
    }

    public List<String> decode(String str) {
        int len = 0;
        StringBuilder length = new StringBuilder();
        List<String> result = new ArrayList<>();
        StringBuilder subString = new StringBuilder();
        for (char c : str.toCharArray()) {
            if (len > 0) {
                subString.append(c);
                len--;
                if (len == 0) {
                    result.add(subString.toString());
                    subString = new StringBuilder();
                }
            }
            else {
                if (Character.isDigit(c)) length.append(c);
                else if (c == '#') {
                    len = Integer.valueOf(length.toString());
                    length = new StringBuilder();
                    if (len == 0) result.add("");
                }
            }
        }
        return result;
    }
}
