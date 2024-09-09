import java.io.*;

public class lab7 {

    public static void main(String[] args) {
        DataInputStream inputStream=null;
        
        // Example 1: ClassNotFoundException
        try {
            Class.forName("NonExistentClass");
        } catch (ClassNotFoundException e) {
            System.out.println("ClassNotFoundException occurred: " + e.getMessage());
        }

        // Example 2: EOFException
        try {
            inputStream = new DataInputStream(new FileInputStream("nonexistent.txt"));
            
            while (true) {
                try {
                    char c = (char)inputStream.readByte();
                    System.out.print(c);
                } catch (EOFException eof) {
                    System.out.println("\nEnd of file reached.");
                    break;
                } catch (IOException ioe) {
                    ioe.printStackTrace();
                    break;
                }
            }
        } catch (FileNotFoundException fnfe) {
            System.out.println("File not found: nonexistent.txt");
        } finally {
            try {
                inputStream.close();
            } catch (IOException ioe) {
                ioe.printStackTrace();
            }
        }
    }
}
