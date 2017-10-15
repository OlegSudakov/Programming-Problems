// https://www.hackerrank.com/challenges/a-very-big-sum

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n;
        n = in.nextInt();
        long []a = new long[n];
        long sum = 0;
        for (int i = 0; i<n; i++){
            sum += in.nextLong();
        }
       System.out.println(sum);

    }
}
