import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class 백준_1003 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int num;
        int[] num0=new int[41];
        int[] num1=new int[41];
        num0[0] = 1;
        num0[1] = 0;
        num1[0] = 0;
        num1[1] = 1;
        int tcase = Integer.parseInt(br.readLine());
        
        for(int i = 0; i < tcase; i++){
            num = Integer.parseInt(br.readLine());
            for(int j=2; j<=num; j++) {
                num0[j] = num0[j-2] + num0[j-1];
                num1[j] = num1[j-2] + num1[j-1];
            }
            bw.write(num0[num] + " " +num1[num] + "\n");
        }
        br.close();
        bw.close();
    }
}
