// https://www.hackerrank.com/challenges/find-digits

import java.util.*;
import java.math.BigInteger;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        int[] digCount = new int[10];
        byte[] digDivisible = new byte [10];
        long n;
        int lastDig;
        int digSum, divSum;
        for (int i = 0; i < t; i++){
            n = in.nextLong();
            for (int j = 0; j<10; j++){
                digCount[j] = 0;
                digDivisible[j] = 0;
            }
            digDivisible[1] = 1;
            lastDig = (int) (n % 10);
            digSum = 0;
            if (lastDig % 2 == 0) digDivisible[2] = 1;
            if ((n % 100) % 4 == 0) digDivisible[4] = 1;
            if (lastDig == 0 || lastDig == 5) digDivisible[5] = 1;
            if (n % 7 == 0) digDivisible[7] = 1;
            if (n % 8 == 0) digDivisible[8] = 1;
            while (n > 0){
                lastDig = (int) (n % 10);
                digCount[lastDig] += 1;
                digSum += lastDig;
                n /= 10;
            }
            if (digSum % 3 == 0) digDivisible[3] = 1;
            if (digDivisible[2] == 1 && digDivisible[3] == 1) digDivisible[6] = 1;
            if (digSum % 9 == 0) digDivisible[9] = 1;
            
            divSum = 0;
            for (int j = 1; j<10; j++){
                divSum += digDivisible[j]*digCount[j];
            }
            System.out.println(divSum);
        }
    }
}
