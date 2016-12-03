import java.io.File;
import java.io.IOException;

public class Day3 {

    public static void main(String[] args) {
        Files f = new Files();
        try {
            String in = f.readString(new File(args[0]), "UTF8");
            String[] tr = in.split("\n");
            int count = 0;
            System.out.println(tr.length);
            for (int i = 0; i < tr.length; i++) {
                if (isValid(tr[i])) count++;
            }
            System.out.println(count);
        } catch (IOException e){
            e.printStackTrace();
        }
    }

    private static boolean isValid(String triangle) {
        triangle = triangle.replaceAll("\\s+","A");
        String[] fnum = triangle.split("A");
        int[][] mask = {
                {1, 2, 3},
                {1, 3, 2},
                {2, 3, 1}
        };
        for (int i = 1; i < fnum.length; i++) {
            if (Integer.parseInt(fnum[mask[i-1][0]]) + Integer.parseInt(fnum[mask[i-1][1]]) <= Integer.parseInt(fnum[mask[i-1][2]])) return false;
        }
        return true;
    }

}
