// https://www.hackerrank.com/challenges/service-lane/problem

import java.util.*;
import java.lang.Math;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int t = in.nextInt();
        int i, j;
        int maxW;
        int[] hway = new int[n];
        for (int k = 0; k < n; k++){
            hway[k] = in.nextInt();
        }
        for (int k = 0; k < t; k++){
            maxW = 3;
            i = in.nextInt();
            j = in.nextInt();
            for (int l = i; l <= j; l++){
                if (hway[l] < maxW) maxW = hway[l];
            }
            System.out.println(maxW);
        }
    }
}
