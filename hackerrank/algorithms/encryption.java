// https://www.hackerrank.com/challenges/encryption/submissions

import java.util.*;
import java.lang.Math;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        char[] message = new char[81];
        message = in.nextLine().toCharArray();
        int l = message.length;
        int rows, cols;
        double root = Math.sqrt(l);
        rows = (int) Math.floor(root);
        if (rows*rows >= l){
            cols = rows;
        }
        else if (rows*(rows+1)>=l){
            cols = rows + 1;
        }
        else {
            rows = rows+1;
            cols = rows;
        }
        char[][] grid = new char [rows][cols];
        int index = 0;
        int i = 0, j = 0;
        while (index < l){
            grid[i][j] = message[index];
            j += 1;
            index += 1;
            if (! (j < cols)){
                i += 1;
                j = 0;
            }
        }
        for (j = 0; j< cols; j++){
            for (i = 0; i<rows; i++){
                if (grid[i][j] != 0) System.out.print(grid[i][j]);
            }
            System.out.print(" ");
        }

    }
}
