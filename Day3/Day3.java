import java.io.File;
import java.io.IOException;

public class Day3 {

    public static void main(String[] args) {
        Files f = new Files();
        try {
            String in = f.readString(new File(args[0]), "UTF8");
            String[] tr = in.split("\n");
            int count = 0;
            int[] rows;
            for (int i = 0; i < tr.length; i++) {
                rows = getRowNums(tr[i]);
                if (isValid(rows[0], rows[1], rows[2])) count++;
            }
            System.out.println(count);
        } catch (IOException e){
            e.printStackTrace();
        }
    }

    private static boolean isValid(int a, int b, int c) {
        if (a + b <= c || a + c <= b || b + c <= a) return false;
        return true;
    }

    private static int[] getRowNums(String triangle) {
        triangle = triangle.replaceAll("\\s+","A");
        String[] fnum = triangle.split("A");
        int[] re = new int[3];
        for (int i = 1; i < fnum.length; i++)
            re[i-1] = Integer.parseInt(fnum[i]);
        return re;
    }

}
