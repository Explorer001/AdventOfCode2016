import java.io.IOException;
import java.security.*;

public class Day5 {

   public static void main(String[] args) {
       System.out.println(getPassword("ugkcyxxp"));
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
