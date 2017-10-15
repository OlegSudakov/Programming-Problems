// https://www.hackerrank.com/challenges/extra-long-factorials

import java.util.*;
import java.math.BigInteger;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n;
        n = in.nextInt();
        BigInteger res = new BigInteger("1");
        for (int i = 1; i<=n; i++){
            res = res.multiply(new BigInteger(Integer.toString(i)));
        }
        System.out.print(res);
    }
}
