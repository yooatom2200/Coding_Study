import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 백준_9012 {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int count  = Integer.parseInt(bf.readLine());
        String testcase[] = new String[count];
        for(int i = 0; i < count; i++){
            testcase[i] = bf.readLine();
        }
        System.out.println("출력시작");
        for(int i = 0; i < count; i++){
            System.out.println(testcase[i]);
        }
    }
}
