import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

static void nextMove(int n, int r, int c, String [] grid){
    int [] bot = {c,r};//x,y
    int [] princess = new int[2];
    for(int i = 0; i<n; i++){
        for(int j = 0; j<n; j++){
            if(grid[i].charAt(j) == 'p'){
                princess[0] = j;
                princess[1] = i;
                break;
            }
        }
    }
        if(bot[0]!=princess[0]){
            if(bot[0]-princess[0]>0){
                System.out.println("LEFT");
                bot[0]--;
            }else{
                System.out.println("RIGHT");
                bot[0]++;
            }
        }else if(bot[1]!=princess[1]){
            if(bot[1]-princess[1]>0){
                System.out.println("UP");
                bot[1]--;
            }else{
                System.out.println("DOWN");
                bot[1]++;
            }
        }
  }

public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n,r,c;
        n = in.nextInt();
        r = in.nextInt();
        c = in.nextInt();
        in.useDelimiter("\n");
        String grid[] = new String[n];


        for(int i = 0; i < n; i++) {
            grid[i] = in.next();
        }

    nextMove(n,r,c,grid);

    }
}
