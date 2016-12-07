import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

public class Day7 {

    public static void main(String[] args) {
       //try {
            Files f = new Files();
            String input = "rhamaeovmbheijj[hkwbkqzlcscwjkyjulk]ajsxfuemamuqcjccbc";//f.readString(new File("/home/lukas/AdventOfCode2016/Day7/puzzleinput"), "UTF8");
            String[][] parts = format(input);
            int count = 0;
            int c = 0;
            for (String[] s : parts) {
                if (supportsTLS(s)) count++;
                if (supportsSSL(s)) c++;
            }
            System.out.println(count + " | " + c);
       //} catch (IOException e) {
         //   e.printStackTrace();
       //}
    }

    private static boolean supportsSSL(String[] s) {
        ArrayList<String> open = new ArrayList<>();
        ArrayList<String> close = new ArrayList<>();
        ArrayList<String> temp;
        for (int i = 1; i < s.length; i += 2) {
            temp = hasABA(s[i]);
            if (!temp.isEmpty()) {
                for (String s1 : temp) close.add(s1);
            }
        }
        for (int i = 0; i < s.length; i += 2) {
            temp = hasABA(s[i]);
            if (!temp.isEmpty()) {
                for (String s2 : temp) open.add(s2);
            }
        }
        for (String s1 : open) {
            for (String s2 : close) {
                if (close(s1, s2)) return true;
                System.out.println(s1 + " | " + s2);
            }
        }
        return false;
    }

    private static boolean close(String s, String t) {
        if (s.charAt(1) == t.charAt(0) && t.charAt(0) == s.charAt(1)) return true;
        return false;
    }

    private static ArrayList<String> hasABA(String s) {
        String sub;
        ArrayList<String> re = new ArrayList<>();
        for (int i = 0; i < s.length() - 2; i++) {
            sub = s.substring(i, i+3);
            if (isPal(sub)) re.add(sub);
        }
        return re;
    }

    private static boolean supportsTLS(String[] s) {
        for (int i = 1; i < s.length; i += 2) if (hasABBA(s[i])) return false;
        for (int i = 0; i < s.length; i += 2) if (hasABBA(s[i])) return true;
        return false;
    }

    private static boolean hasABBA(String s) {
        String sub;
        for (int i = 0; i < s.length() - 3; i++) {
            sub = s.substring(i, i+4);
            if (isPal(sub)) return true;
        }
        return false;
    }

    private static boolean isPal(String s) {
        String rev = "";
        for (int i = 0; i < s.length(); i++) {
            rev += Character.toString(s.charAt(s.length() - 1 - i));
        }
        if (!isABBA(s)) return false;
        if (s.equals(rev)) return true;
        return false;
    }

    private static boolean isABBA (String s) {
        int flag = 1;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != s.charAt(0)) flag = 0;
        }
        if (flag == 0) return true;
        return false;
    }

    private static String[][] format(String s) {
        String[] parts = s.split("\n");
        String[][] re = new String[parts.length][];
        for (int i = 0; i < re.length; i++) {
            re[i] = _format(parts[i]);
        }
        return re;
    }

    private static String[] _format(String s) {
        String[] re = s.split("[\\[\\]]");
        return re;
    }
}
