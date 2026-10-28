class Solution {
    public boolean isPalindrome(String s) {
        String upperCaseString = s.toUpperCase();
        int i = 0;
        int j = s.length() - 1;
        while (i < j) {
            while (i < j && !Character.isLetterOrDigit(upperCaseString.charAt(i))) i++;
            while (i < j && !Character.isLetterOrDigit(upperCaseString.charAt(j))) j--;
            if (upperCaseString.charAt(i) != upperCaseString.charAt(j)) {
                return false;
            }
            i++;
            j--;
        } 
        return true;
    }
}
