/*
입력수를 2진수로 변경하고 2진수의 1의 개수를 파악
파악 후 b의 개수와 일치하면 0, 불일치시 1의 개수가 동일하도록 연산작업 진행
*/
import java.util.Scanner;

public class 백준_1052 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int cnt = 0;
		int point = 0;
        int ones = 0;
        String binaryN = Integer.toBinaryString(a);
		
		for(int i=0; i<binaryN.length(); i++) {// 1의 개수 출력
			if(binaryN.charAt(i) == '1') {
				ones++;
			}
        }
		
		if(ones <= b) {//상점에 안가도 되는경우
			System.out.println(0);
		}
        else {
			for(int i=0; i<binaryN.length(); i++) {
				if(binaryN.charAt(i) == '1') {
					cnt++;
					if(cnt == b) {
						point = i;
						break;
					}
				}
			}
			String stringAnswer = binaryN.substring(point);
			int answer = Integer.parseInt(stringAnswer, 2);
			int temp = 0;
			for(int i=0; i<binaryN.length()-point; i++) {
				temp = temp << 1;
				temp = temp+1;
			}
			answer ^= temp;
			answer = answer+1;
			System.out.println(answer);
		}

    }
}