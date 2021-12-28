
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
public class 백준_1260 {
    public static int[][] arr;//목록저장소
	public static boolean[] visited;//방문여부

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
        
		int point = scan.nextInt();
		int line = scan.nextInt();
		int start = scan.nextInt();
		
		arr = new int[point+1][point+1];
		
		for(int i=1;i<=line;i++) {
			int a = scan.nextInt();
			int b = scan.nextInt();
			arr[a][b] = 1;
			arr[b][a] = 1;
		}
        //DFS
		visited = new boolean[point+1];
		dfs(start); 
		
		System.out.println();
        
        //BFS
		visited = new boolean[point+1];
		bfs(start); 

		
	}
	public static void dfs(int start) {
		visited[start] = true;
		System.out.print(start+ " ");
		
		if(start == arr.length) {
			return;
		}

		for(int a=1;a<arr.length;a++) {
			if(arr[start][a] == 1 && visited[a] == false) {
				dfs(a);
			}
		}
			
	}
	public static void bfs(int start) {
		Queue<Integer> que = new LinkedList<Integer>(); 
		
		que.add(start);
		visited[start] = true;
 		System.out.print(start+ " ");
		
		while(!que.isEmpty()) {
			int temp = que.peek();
			que.poll();
			for(int i=1; i<arr.length;i++) {
				if(arr[temp][i] ==1 && visited[i] == false) {
					que.add(i);
					visited[i] = true;
					System.out.print(i+ " ");
				}
			}
		}
	}
}
