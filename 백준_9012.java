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

        for(int i = 0; i < count; i++){
            int isVPS = 0;
            int judge = 1;
            for(int j = 0; j < testcase[i].length(); j++){
                if(judge == 0)
                    continue;
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
