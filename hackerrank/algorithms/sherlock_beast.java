// https://www.hackerrank.com/challenges/sherlock-and-the-beast

import java.util.*;
import java.math.BigInteger;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        int n, numFives, numThrees; boolean printed;
        for (int i = 0; i < t; i++){
            n = in.nextInt();
            numFives = n;
            numThrees = 0;
            while(numFives >= 0){
                if (numFives % 3 == 0 && numThrees % 5 == 0){
                    System.out.println(new String(new char[numFives]).replace("\0", "5")+new String(new char[numThrees]).replace("\0", "3"));
                    break;
                }
                numFives -= 5;
                numThrees += 5;
            }
            if (numFives < 0){
                System.out.println("-1");
            }
        }
    }
}
