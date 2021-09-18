import java.util.HashMap;
import java.util.Map;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int max = 0;
        int start = 0;
        Map<Byte, Integer> m = new HashMap<>();
        byte[] bytes = s.getBytes();
        for (int i = 0; i < bytes.length; i++) {
            byte b = bytes[i];
            Integer objI = m.get(b);
            if (objI != null && objI >= start) {
                start = objI + 1;
            }

            int length = i - start + 1;
            if (length > max) {
                max = length;
            }

            m.put(b, i);
        }
        return max;
    }
}

public class Main {

    public static void main(String[] args) {
        // write your code here
        Solution s = new Solution();
        int max = s.lengthOfLongestSubstring("abcabcbb");
        System.out.println(max);
    }
}