// https://www.hackerrank.com/challenges/kaprekar-numbers

import java.util.*;
import java.lang.Math;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int p = in.nextInt();
        int q = in.nextInt();
        int count = 0; long square; int d; long iCpy;
        long r, l;
        for (long i = p; i<=q; i++){
            iCpy = i;
            d = 0;
            while (iCpy > 0){
                iCpy /= 10;
                d += 1;
            }
            square = i*i;
            d = (int) Math.pow(10, d);
            r =  square % d;
            l =  square / d;
            if (l + r == i){
                count += 1;
                System.out.print(i);
                System.out.print(" ");
                continue;
            }
        }
        if (count == 0) System.out.print("INVALID RANGE");
        }
}
