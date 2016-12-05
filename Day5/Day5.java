import java.io.IOException;
import java.security.*;

public class Day5 {

   public static void main(String[] args) {
       System.out.println(getPassword("ugkcyxxp"));
       //System.out.println(getPasswordIndex("ugkcyxxp"));
   }

    private static String getString(String[] s) {
        String re = "";
        for (int i = 0; i < s.length; i++) re += s[i];
        return re;
    }

    private static String getPasswordIndex(String input) {
        try {
            String[] s = new String[8];
            for (int i = 0; i < s.length; i++) s[i] = "_";
            long c = 0;
            String hash = input;
            String t;
            int pos;
            System.out.println(getString(s));
            while (!fin(s)) {
                t = MD5(hash + c++).toString();
                if (t.substring(0, 5).equals("00000")){
                    if (Character.isDigit(t.charAt(5))) {
                        pos = Integer.parseInt(Character.toString(t.charAt(5)));
                        if (pos < 8 && s[pos].equals("_")) s[pos] = Character.toString(t.charAt(6));
                        System.out.println(getString(s));
                    }
                }
            }
            return getString(s);
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return "foo";
        }
    }

    private static boolean fin(String[] s) {
        for (int i = 0; i < s.length; i++) {
            if (s[i].equals("_")) return false;
        }
        return true;
    }

    private static void visualize(String[] s) {
        String[] rnd = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"};
        String re = "";
        int rand;
        int count = 0;
        for (int i = 0; i < s.length; i++) {
            rand = (int) (Math.random() * 15);
            if (s[i].equals("_")) {
                re += rnd[rand];
            } else {
                count++;
                re += s[i];
            }
        }
        int p = (int) (12.5 * count);
        System.out.println(re + " | " + p + "%");

    }

    private static String getPassword(String input) {
        try {
            String[] s = new String[8];
            for (int i = 0; i < s.length; i++) s[i] = "_";
            long c = 0;
            String hash = input;
            String t;
            int pos = 0;
            while (!fin(s)) {
                t = MD5(hash + c++).toString();
                if (t.substring(0, 5).equals("00000")) {
                    s[pos++] = Character.toString(t.charAt(5));
                }
                visualize(s);
            }
            return getString(s);
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return "foo";
        }
    }

    private static StringBuilder MD5(String s) throws NoSuchAlgorithmException{
        try {
            byte[] bytesOfMessage = s.getBytes("UTF-8");
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] thedigest = md.digest(bytesOfMessage);
            StringBuilder sb = new StringBuilder();
            for (byte b :thedigest) {
                sb.append(String.format("%02X", b));
            }
            return sb;
        } catch (IOException e) {
             e.printStackTrace();
            return new StringBuilder();
        }
    }

}
