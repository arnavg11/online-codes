import java.io.*;
import java.util.*;

public class Solution {
    static int move(int[] bot, String[] grid, int[] gridDimensions){
                if(grid[bot[0]].charAt(bot[1]) == 'd'){
            System.out.println("CLEAN");
            return 0;
                }
        
        for(int i = 0; i<gridDimensions[0]; i++){
            for(int j =0; j<gridDimensions[1]; j++){
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
    };

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int[] bot = {s.nextInt(), s.nextInt()};
        int[] gridDimensions = {s.nextInt(), s.nextInt()};//h,w
        s.nextLine();
        String[] grid = new String[gridDimensions[0]];
        for(int i = 0; i<gridDimensions[0]; i++){
            grid[i] = s.nextLine();
        }
        int x = move(bot,grid, gridDimensions);
    }
}
