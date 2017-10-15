// https://www.hackerrank.com/challenges/taum-and-bday/problem

import java.util.*;
import java.lang.Math;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        long b, w, x, y, z;
        long sum;
        for(int i = 0; i < t; i++){
            b = in.nextLong();
            w = in.nextLong();
            x = in.nextLong();
            y = in.nextLong();
            z = in.nextLong();
            sum = 0;
            if (x < y+z) sum += b*x;
            else sum += b*(y+z);
            if (y < x+z) sum += w*y;
            else sum += w*(x+z);
            System.out.println(sum);

        }
    }
}
