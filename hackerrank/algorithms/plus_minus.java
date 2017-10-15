// https://www.hackerrank.com/challenges/plus-minus

import java.io.*;
import java.text.DecimalFormat;
import java.util.*;
import java.math.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n;
        int pos = 0;
        int neg = 0;
        int zer = 0;
        int cur = 0;
        n = in.nextInt();
        int []m = new int[n];
        for (int i = 0; i<n; i++){
            cur = in.nextInt();
            if (cur > 0) ++pos;
            else if (cur == 0) ++zer;
            else ++neg;
        }
        DecimalFormat df = new DecimalFormat("0.000");
        System.out.println(df.format((float)pos/n));
        System.out.println(df.format((float)neg/n));
        System.out.println(df.format((float)zer/n));
    }
}
