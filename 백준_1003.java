import java.util.Scanner;

public class 백준_1003 {
    static int tcase = 0;
    static int fibonacci(int a){
        if (a == 0){
            return 0;
        }
        else if (a == 1){
            return 1;
        }
        else{
            return fibonacci(a-1) + fibonacci(a-2);
        }
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        tcase = sc.nextInt();
        
        for(int i = 0; i < tcase; i++){

        }
    }
    
}
