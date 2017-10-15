// https://www.hackerrank.com/challenges/library-fine

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in) ;
        int da, ma, ya, de, me, ye;
        da = in.nextInt();
        ma = in.nextInt();
        ya = in.nextInt();
        de = in.nextInt();
        me = in.nextInt();
        ye = in.nextInt();
        int fine = 0;
        if (ya > ye){
            fine = 10000;
        }
        else if (ya == ye){
            if (ma > me){
                fine = 500*(ma-me);
            }
            else if (ma == me){
                if (da > de){
                    fine = 15*(da-de);
                }
            }
        }
        System.out.print(fine);

    }
}
