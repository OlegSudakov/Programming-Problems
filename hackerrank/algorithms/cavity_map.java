// https://www.hackerrank.com/challenges/cavity-map/problem

import java.util.*;
import java.lang.Math;

public class Main {

    private static boolean checkCell(char[][]map, int i, int j){
        boolean flag = true;
        for (int k = -1; k<=1; k+=2){
            if (map[i+k][j] >= map[i][j]) flag = false;
        }
        for (int k = -1; k<=1; k+=2){
            if (map[i][j+k] >= map[i][j]) flag = false;
        }
        return flag;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        in.nextLine();
        boolean flag = false;
        char[][] map = new char[100][100];
        for (int i = 0; i<n; i++){
            map[i] = in.nextLine().toCharArray();
        }
        char[][] mapCpy = new char[100][100];
        for (int i = 0; i<n; i++){
            for (int j = 0; j<n; j++){
                mapCpy[i][j] = map[i][j];
            }
        }
        for (int i = 1; i<n-1; i++){
            for (int j = 1; j<n-1; j++){
                if (checkCell(map, i, j)) mapCpy[i][j] = 'X';
            }
        }
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                System.out.print(mapCpy[i][j]);
            }
            System.out.println();
        }
    }
}
