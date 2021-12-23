import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 백준_9012 {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int count  = Integer.parseInt(bf.readLine());
        String testcase[] = new String[count];
        //값 입력 시작
        for(int i = 0; i < count; i++){
            testcase[i] = bf.readLine();
        }
        //VPS 판단 시작
        for(int i = 0; i < count; i++){
            int isVPS = 0;//VPS인지 판단. 0보다 아래인 경우와 최종결과값이 0이 아닌경우 VPS가 아님.
            int judge = 1;//YES, NO 트리거
            for(int j = 0; j < testcase[i].length(); j++){
                if(judge == 0)
                    continue;
                //시작괄호일시 +1, 닫힘괄호일시 -1
                if(testcase[i].charAt(j) == '(')
                    isVPS += 1;
                else if(testcase[i].charAt(j) == ')')
                    isVPS -= 1;               
                if(isVPS < 0)
                    judge = 0;
            }
            if(isVPS != 0)
                judge = 0;
            if(judge == 1)
                System.out.println("YES");
            else
                System.out.println("NO");
        }
    }
}
