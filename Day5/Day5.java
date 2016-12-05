import java.io.IOException;
import java.security.*;

public class Day5 {

   public static void main(String[] args) {
       //System.out.println(getPassword("ugkcyxxp"));
       System.out.println(getPasswordIndex("ugkcyxxp"));
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

    private static String getPassword(String input) {
        try {
            String re = "";
            long c = 0;
            String hash = input;
            String s;
            while (re.length() < 8) {
                s = MD5(hash + c++).toString();
                if (s.substring(0, 5).equals("00000")) {
                    re += s.charAt(5);
                    System.out.println(re);
                }
            }
            return re;
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
