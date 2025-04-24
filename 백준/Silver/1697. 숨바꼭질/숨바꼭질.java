import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
  static int MAX = 100000;

  static int bfs(int n, int k) {
    int[] visited = new int[MAX + 1];
    Queue<Integer> q = new LinkedList<>();

    int x = n;
    while (true) {
      if (x == k) break;
      
      int[] nexts = { x - 1, x + 1, x * 2 };
      for (int next : nexts) {
        if (next > MAX || next < 0 || visited[next] > 0)
          continue;

        q.add(next);
        visited[next] = visited[x] + 1;
      }
      x = q.poll();
    }

    return visited[x];
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int k = sc.nextInt();
    sc.close();

    System.out.println(bfs(n, k));
  }
}
