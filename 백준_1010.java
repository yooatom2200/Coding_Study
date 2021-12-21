/*
순열과 조합문제
해당 경우 조합의 문제
nCr 로 계산하면 된다
*/
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 백준_1010 {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int testcase = Integer.parseInt(bf.readLine());
        int[] answers = new int[testcase];
        for(int i = 0; i < testcase; i++){
            String[] pnc = bf.readLine().split(" ");
            int n = Integer.parseInt(pnc[0]);
            int r = Integer.parseInt(pnc[1]);
            if(n < r){
                int tmp = n;
                n = r;
                r = tmp;
            }

            int top = 1;
            for(int j = n; j <= n-r+1; j--){
                top *= j;
            }
            int bottom = fact(r);
            answers[i] = top / bottom;
        }
        for(int i = 0; i < testcase; i++){
            System.out.println(answers[i]);
        }
    }

    public static int fact(int a){//팩토리얼재귀함수
        if(a <= 1)
            return a;
        else
            return fact(a-1) * a;
    }
}