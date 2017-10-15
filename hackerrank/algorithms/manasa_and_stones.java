// https://www.hackerrank.com/challenges/manasa-and-stones

import java.util.*;
import java.lang.Math;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        int n, a, b;
        for (int i = 0; i<t; i++){
            n = in.nextInt();
            a = in.nextInt();
            b = in.nextInt();
            if (a > b){
                int temp = a;
                a = b;
                b = temp;
            }
            for (int j = 0; j<n; j++){
                if (a == b){
                    System.out.print((long)a*(n-1-j) + b*j);
                    break;
                }
                System.out.print((long)a*(n-1-j) + b*j);
                System.out.print(" ");
            }
            System.out.println();
        }
    }
}
