// https://www.hackerrank.com/challenges/diagonal-difference

import java.io.*;
import java.util.*;

public class Solution {
    
    static int getDifference(int[][] m, int n){
        int summ = 0;
        int suma = 0;
        for (int i=0; i<n; i++){
            summ += m[i][i];
            suma += m[n-i-1][i];
        }
        return Math.abs(summ - suma);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n;
        int res;
        n = in.nextInt();
        int [][]m = new int[n][n];
        for (int i = 0; i<n; i++){
            for (int j = 0; j<n; j++){
                m[i][j] = in.nextInt();
            }
        }
        res = getDifference(m, n);
        System.out.println(res);
    }
}
