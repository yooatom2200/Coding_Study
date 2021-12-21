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
        long[] answers = new long[testcase];
        for(int i = 0; i < testcase; i++){
            String[] ncr = bf.readLine().split(" ");
            int n = Integer.parseInt(ncr[0]);
            int r = Integer.parseInt(ncr[1]);
            if(n < r){
                int tmp = n;
                n = r;
                r = tmp;
            }
            if(n/2 < r)
                r = n - r;
            long top = 1;
            for(int j = n; j >= n-r+1; j--){
                top *= j;
            }
            long bottom = fact(r);
            answers[i] = top / bottom;
        }
        for(int i = 0; i < testcase; i++){
            System.out.println(answers[i]);
        }
    }

    public static long fact(long a){//팩토리얼재귀함수
        if(a <= 1)
            return 1;
        else
            return fact(a-1) * a;
    }
}