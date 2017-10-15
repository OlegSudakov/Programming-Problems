// https://www.hackerrank.com/challenges/acm-icpc-team/problem

import java.util.*;
import java.lang.Math;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        in.nextLine();
        char[][] a = new char[500][500];
        for (int i = 0; i<n; i++){
            a[i] = in.nextLine().toCharArray();
        }
        for (int i = 0; i<n; i++){
            for (int j = 0; j<m; j++){
                a[i][j] = (char) (a[i][j]-'0');
            }
        }
        int maxt = -1;
        int curmax;
        int nummax = 0;
        for (int i = 0; i<n-1; i++){
            for (int j = i+1; j<n; j++){
                curmax = 0;
                for (int k = 0; k<m; k++){
                    if ((a[i][k] | a[j][k]) == 1) curmax +=1;
                }
                if (curmax > maxt){
                    maxt = curmax;
                    nummax = 0;
                }
                else if (curmax == maxt){
                    nummax += 1;
                }
            }
        }
        nummax += 1;
        System.out.println(maxt);
        System.out.println(nummax);
    }
}
