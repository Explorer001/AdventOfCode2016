import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

public class Day4 {

    public static void main(String[] args) {
        try {
            Files f = new Files();
            String in = f.readString(new File("/home/lukas/AdventOfCode2016/Day4/puzzleinput"), "UTF8");
            String[] i2 = in.split("\\n");
            int sum = 0;
            for (int i = 0; i < i2.length; i++) {
                sum += checkRoom(i2[i]);
            }
            System.out.println(sum);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static String getCommon(String s) {
        s = s.replaceAll("-", "");
        s = s.replaceAll("\\d+.*", "");
        Character[] ch = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
        int[] in = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
        for (int i = 0; i < s.length(); i++) {
            char check = s.charAt(i);
            for (int j = 0; j < ch.length; j++) {
                if (check == ch[j]) {
                    in[j] += 1;
                    break;
                }
            }
        }
        String re  = "";
        for (int i = 0; i < 5; i++) {
            re += ch[posMax(in)];
            in[posMax(in)] = 0;
        }
        return re;
    }

    private static int posMax(int[] in) {
        int max = 0;
        int pos = 0;
        for (int i = 0; i < in.length; i++) {
            if (in[i] > max) {
                max = in[i];
                pos = i;
            }
        }
        return pos;
    }

    public static int checkRoom(String room) {
        String[] parts = room.split("-");
        String[] ctrl = parts[parts.length - 1].split("\\[");
        ctrl[1] = ctrl[1].replaceAll("\\]", "");
        String cm = getCommon(room);
        boolean flag;
        for (int i = 0; i < ctrl[1].length(); i++) {
            flag = false;
            for (int j = 0; j < cm.length(); j++) {
                if (cm.charAt(j) == ctrl[1].charAt(i)) flag = true;
            }
            if (flag == false) return 0;
        }
        return Integer.parseInt(ctrl[0]);
    }
}
