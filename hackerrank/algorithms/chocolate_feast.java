// https://www.hackerrank.com/challenges/chocolate-feast/problem

import java.util.*;
import java.lang.Math;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        int n, c, m;
        int chocNum = 0;
        int wraps;
        for (int i = 0; i<t; i++){
            n = in.nextInt();
            c = in.nextInt();
            m = in.nextInt();
            chocNum = n/c;
            wraps = chocNum;
            while (wraps / m > 0){
                chocNum += wraps / m;
                wraps = wraps % m + wraps / m;
            }
            System.out.println(chocNum);
        }
    }
}
