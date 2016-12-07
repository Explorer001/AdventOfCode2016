import java.io.File;
import java.io.IOException;

public class Day6 {

    public static void main(String[] args) {
        try {
            Files f = new Files();
            String data = f.readString(new File("/home/lukas/AdventOfCode2016/Day6/puzzleinput"), "UTF8");
            System.out.println(getTransmission(data, 0));
            System.out.println(getTransmission(data, 1));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static int posMax(int[] in) {
        int max = 0;
        int pos = 0;
        for (int i = 0; i < in.length; i++) {
            if (in[i] > max) {
                max = in[i] ;
                pos = i;
            }
        }
        return pos;
    }

    private static int posMin(int[] in) {
        int min = Integer.MAX_VALUE;
        int pos = 0;
        for (int i = 0; i < in.length; i++) {
            if (in[i] < min && in[i] != 0) {
                min = in[i] ;
                pos = i;
            }
        }
        return pos;
    }

    private static String getTransmission(String data, int mode) {
        String[] parts = data.split("\n");
        String re = "";
        for (int i = 0; i < parts[1].length(); i++) {
            re += getCommon(parts, i, mode);
        }
        return re;
    }

    private static String getCommon(String[] input, int pos, int mode) {
        char[] ch = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
        int[] in = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
        for (String s : input) {
           for (int i = 0; i < ch.length; i++) {
               if (s.charAt(pos) == ch[i]) in[i] += 1;
           }
        }
        if (mode == 0) return Character.toString(ch[posMax(in)]);
        else return Character.toString(ch[posMin(in)]);
    }
}
