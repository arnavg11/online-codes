import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    static int next_move(int posr, int posc, String[] board) {
        //add logic here
        if (board[posr].charAt(posc) == 'd') {
            System.out.println("CLEAN");
            return 0;
        }
        for (int i = -1; i < 2; i++) {
            for (int j = -1; j < 2; j++) {
                try {

                    if (board[posr - i].charAt(posc - j) == 'd') {
                        if (j != 0) {
                            if (j == 1) {
                                System.out.println("LEFT");
                            } else {
                                System.out.println("RIGHT");
                            }
                        } else {
                            if (i == -1) {
                                System.out.println("DOWN");
                            } else {
                                System.out.println("UP");
                            }
                        }
                        return 0;
                    }
                } catch (ArrayIndexOutOfBoundsException e) {}
                catch(StringIndexOutOfBoundsException e){}
            }
        }
        for(int i = 0; i<5; i++){
            for(int j =0; j<5; j++){
                if(board[i].charAt(j) == 'o'){
                    if(posc!=j){
                        if(posc>j){
                            System.out.println("LEFT");
                        }else{
                            System.out.println("RIGHT");
                        }
                    }else{
                        if(posr<i){
                            System.out.println("DOWN");
                        }else{
                            System.out.println("UP");
                        }
                    }
                    return 0;
                }
            }
        }
        return 0;
    }

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int[] pos = new int[2];
        String board[] = new String[5];
        for (int i = 0; i < 2; i++) pos[i] = in .nextInt();
        for (int i = 0; i < 5; i++) board[i] = in .next();
        next_move(pos[0], pos[1], board);
    }
}
