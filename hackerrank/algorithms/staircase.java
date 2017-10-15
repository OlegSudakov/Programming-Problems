// https://www.hackerrank.com/challenges/staircase

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n;
        n = in.nextInt();
        for (int i = 0; i<n; i++){
            int j = 0;
            while (j<n-i-1){
                System.out.print(" ");
                j++;
            }
            while (j<n){
                System.out.print("#");
                j++;
            }
            System.out.print("\n");
        }

    }
}
