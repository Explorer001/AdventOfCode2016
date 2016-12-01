import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;
import java.util.concurrent.TimeUnit;

public class Day1 {

    static int hdg = 0;
    static int mvx = 0;
    static int mvy = 0;
    static ArrayList<Visited> v = new ArrayList<>();

    static class Visited {
        int x;
        int y;

        public Visited(int x, int y){
            this.x = x;
            this.y = y;
        }
    }

    static class GUI extends JFrame {

        public GUI() {
            setTitle("ChickenHQ");
            setSize(400, 400);
            setResizable(false);
            setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
            setVisible(true);
        }

        public void paint(Graphics g) {
            int offset = 300;
            g.setColor(Color.BLUE);
            for (int i = 0; i < v.size() - 1; i++) {
                int x1 = v.get(i).x + offset - 100;
                int y1 = v.get(i).y + offset;
                int x2 = v.get(i + 1).x + offset - 100;
                int y2 = v.get(i + 1).y + offset;
                g.drawLine(x1, y1, x2, y2);
                try {
                    TimeUnit.MILLISECONDS.sleep(10);

                } catch (InterruptedException e) {
                    e.printStackTrace();
                }

            }

        }
    }

    public static void main(String[] args) {
        String data = "R4, R4, L1, R3, L5, R2, R5, R1, L4, R3, L5, R2, L3, L4, L3, R1, R5, R1, L3, L1, R3, L1, R2, R2, L2, R5, L3, L4, R4, R4, R2, L4, L1, R5, L1, L4, R4, L1, R1, L2, R5, L2, L3, R2, R1, L194, R2, L4, R49, R1, R3, L5, L4, L1, R4, R2, R1, L5, R3, L5, L4, R4, R4, L2, L3, R78, L5, R4, R191, R4, R3, R1, L2, R1, R3, L1, R3, R4, R2, L2, R1, R4, L5, R2, L2, L4, L2, R1, R2, L3, R5, R2, L3, L3, R3, L1, L1, R5, L4, L4, L2, R5, R1, R4, L3, L5, L4, R5, L4, R5, R4, L3, L2, L5, R4, R3, L3, R1, L5, R5, R1, L3, R2, L5, R5, L3, R1, R4, L5, R4, R2, R3, L4, L5, R3, R4, L5, L5, R4, L4, L4, R1, R5, R3, L1, L4, L3, L4, R1, L5, L1, R2, R2, R4, R4, L5, R4, R1, L1, L1, L3, L5, L2, R4, L3, L5, L4, L1, R3";
        String[] parts = data.split(", ");
        v.add(new Visited(mvx, mvy));
        for (int i = 0; i < parts.length; i++) {
            moveOn(parts[i]);
        }
        System.out.println(getDistance(mvx, mvy));
        Visited f = first();
        GUI g = new GUI();
        System.out.println(getDistance(f.x, f.y));
    }

    private static void moveOn(String cmd) {
        Character dir = cmd.charAt(0);
        int dist = Integer.parseInt(cmd.substring(1));
        if (dir == 'R') hdg = (((++hdg % 4) + 4) % 4);
        if (dir == 'L') hdg = (((--hdg % 4) + 4) % 4);
        switch (hdg) {
            case 0 : for (int i = 0; i < dist; i++) {
                mvy += 1;
                v.add(new Visited(mvx, mvy));
            } break;
            case 1 : for (int i = 0; i < dist; i++) {
                mvx += 1;
                v.add(new Visited(mvx, mvy));
            } break;
            case 2 : for (int i = 0; i < dist; i++) {
                mvy -= 1;
                v.add(new Visited(mvx, mvy));
            } break;
            case 3 : for (int i = 0; i < dist; i++) {
                mvx -= 1;
                v.add(new Visited(mvx, mvy));
            } break;
        }
    }

    private static Visited first() {
        int fl = 0;
        Visited re = new Visited(1, 1);
        for (int i = 1; i < v.size(); i++) {
            for (int k = 0; k < i; k++) {
                if (v.get(k).x == v.get(i).x && v.get(k).y == v.get(i).y && fl == 0) {
                    re.x = v.get(i).x;
                    re.y = v.get(i).y;
                    fl = 1;
                }
            }
        }
        return re;
    }

    private static int getDistance(int x, int y) {
        return Math.abs(x) + Math.abs(y);
    }

}
