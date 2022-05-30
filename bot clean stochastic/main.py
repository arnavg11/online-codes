import java.io.*;
import java.util.*;

public class Solution {
    static int move(int[] bot, String[] grid){
                if(grid[bot[0]].charAt(bot[1]) == 'd'){
            System.out.println("CLEAN");
            return 0;
        }
        for(int i = 0; i<5; i++){
            for(int j =0; j<5; j++){
                if(grid[i].charAt(j) == 'd'){
                    if(bot[1]!=j){
                        if(bot[1]>j){
                            System.out.println("LEFT");
                        }else{
                            System.out.println("RIGHT");
                        }
                    }else{
                        if(bot[0]<i){
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
        Scanner s = new Scanner(System.in);
        int[] bot = {s.nextInt(), s.nextInt()};
        s.nextLine();
        String[] grid = new String[5];
        for(int i = 0; i<5; i++){
            grid[i] = s.nextLine();
        }
        int x = move(bot,grid);
    }
}
