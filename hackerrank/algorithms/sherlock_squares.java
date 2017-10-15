// https://www.hackerrank.com/challenges/sherlock-and-squares

import java.util.*;
import java.lang.Math;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        in.nextLine();
        long a,b;
        long res;
        for (int i = 0; i < t; i++){
            a = in.nextLong();
            b = in.nextLong();
            a = (long) Math.ceil(Math.sqrt(a));
            b = (long) Math.floor(Math.sqrt(b));
            if (b-a+1<0) res = 0;
            res = (b-a+1);
            System.out.println(res);

        }
    }
}
