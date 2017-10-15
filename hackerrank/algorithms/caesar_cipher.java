// https://www.hackerrank.com/challenges/caesar-cipher-1

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n;
        int k;
        n = in.nextInt();
        in.nextLine();
        String s = in.nextLine();
        char[] c = s.toCharArray();
        k = in.nextInt();
        for (int i = 0; i<n; i++){
            if (Character.isLetter(c[i])){
                if (Character.isLowerCase(c[i])){
                    c[i] = (char) ('a' + (c[i]-'a'+k)%26);
                }
                else {
                    c[i] = (char) ('A' + (c[i]-'A'+k)%26);
                }
            }
        }
        String outString = new String(c);
        System.out.print(outString);
    }
}
