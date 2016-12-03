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
            int[][] col;
            for (int i = 0; i < tr.length; i++) {
                rows = getRowNums(tr[i]);
                if (isValid(rows[0], rows[1], rows[2])) count++;
            }
            int c2 = 0;
            for (int i = 0; i < tr.length - 2; i = i + 3) {
                col = getColumnNums(tr[i], tr[i+1], tr[i+2]);
                for (int j = 0; j < col.length; j++) {
                   if (isValid(col[j][0], col[j][1], col[j][2])) c2++;
                }
            }
            System.out.println(count);
            System.out.println(c2);
        } catch (IOException e){
            e.printStackTrace();
        }
        }

    private static boolean isValid(int a, int b, int c) {
        if (a + b <= c || a + c <= b || b + c <= a) return false;
        return true;
    }

    private static int[][] getColumnNums(String c1, String c2, String c3) {
        int[][] re = new int[3][3];
        c1 = c1.replaceAll("\\s+","A");
        c2 = c2.replaceAll("\\s+","A");
        c3 = c3.replaceAll("\\s+","A");
        String[] c1n = c1.split("A");
        String[] c2n = c2.split("A");
        String[] c3n = c3.split("A");
        for (int i = 0; i < re.length; i++) {
            re[i][0] = Integer.parseInt(c1n[i+1]);
            re[i][1] = Integer.parseInt(c2n[i+1]);
            re[i][2] = Integer.parseInt(c3n[i+1]);
        }
        return re;
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
