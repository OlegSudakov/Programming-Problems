// https://www.hackerrank.com/challenges/angry-professor

import java.util.*;
import java.math.BigInteger;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t, n, k;
        t = in.nextInt();
        boolean[] tarr = new boolean[t];
        for (int i = 0; i < t; i++){
            int numPres = 0;
            n = in.nextInt();
            k = in.nextInt();
            for (int j = 0; j < n; j++){
                if (in.nextInt() <= 0) {
                    ++numPres;
                }
            }
            if (numPres < k){
                tarr[i] = true;
            }
            else {
                tarr[i] = false;
            }
        }
        for (int i = 0; i < t; i++){
            if (tarr[i]){
                System.out.println("YES");
            }
            else {
                System.out.println("NO");
            }
        }
    }
}
