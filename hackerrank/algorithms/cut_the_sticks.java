// https://www.hackerrank.com/challenges/cut-the-sticks/problem

import java.util.*;
import java.lang.Math;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] a = new int[n];
        int prevNum;
        for (int i = 0; i < n; i++){
            a[i] = in.nextInt();
        }
        Arrays.sort(a);
        prevNum = a[0];
        System.out.println(n);
        for (int i = 0; i<n; i++){
            if (a[i] != prevNum){
                System.out.println(n - i);
                prevNum = a[i];
            }
        }
    }
}
