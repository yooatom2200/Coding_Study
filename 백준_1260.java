import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
public class 백준_1260 {
    static int[][] check;
    public static void main(String[] args) throws IOException{
        

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String testcase = bf.readLine();
        String[] NMV = testcase.split(" ");
        int N = Integer.parseInt(NMV[0]);
        int M = Integer.parseInt(NMV[1]);
        int V = Integer.parseInt(NMV[2]);
        check = new int[10][10];
    }
}
