import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class Files {
    private Files() {
    }
    public static void writeBytes(byte[] in, int offset, int count, File file, boolean append) throws IOException {
        FileOutputStream fos = null;
        try {
            fos = new FileOutputStream(file, append);
            fos.write(in, offset, count);
        } finally {
            if (fos != null)
                fos.close();
        }
    }
    public static void writeString(String s, String charset, File file, boolean append) throws IOException {
        byte[] data = s.getBytes(charset);
        writeBytes(data, 0, data.length, file, append);
    }
    public static byte[] readBytes(File file, int length) throws IOException {
        byte[] content = new byte[length];
        FileInputStream fis = null;
        try {
            fis = new FileInputStream(file);
            int read = 0;
            int offset = 0;
            while (offset < length && read != -1) {
                read = fis.read(content, offset, length - offset);
                offset += read;
            }
        } finally {
            if (fis != null)
                fis.close();
        }
        return content;
    }
    public static String readString(File file, String charset) throws IOException {
        return new String(readBytes(file, (int) file.length()), charset);
    }
}
