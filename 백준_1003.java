import java.util.Scanner;

public class 백준_1003 {
    static int zCount = 0;
    static int oCount = 0;
    static int fibonacci(int a){
        if (a == 0){
            zCount += 1;
            return 0;
        }
        else if (a == 1){
            oCount += 1;
            return 1;
        }
        else{
            return fibonacci(a-1) + fibonacci(a-2);
        }
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        for(int i = 0; i < sc.nextInt(); i++){
            fibonacci(sc.nextInt());
            System.out.printf("%d %d\n", zCount, oCount);
            zCount = 0;
            oCount = 0;
        }
    }
}
