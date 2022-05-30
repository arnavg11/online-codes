import java.io.*;
import java.util.*;

public class Solution {
    boolean notDone(int[][] grid){
        for(int[] i:grid){
            for(int j:i){
                if(j==0){
                    return true;
                }
            }
        }
        return false;
    }
    
    void solve(int[][] grid){
        Random r = new Random();
        int x,y;
        for(;;)
            x = r.nextInt(9); y = r.nextInt(9);
            if(grid[y][x] == 0){
                ArrayList<int> nums = new ArrayList<String>(Arrays.asList(1,2,3,4,5,6,7,8,9));
                int leftOvers = 9;
                for(int i = 0; i<9; i++){
                    if(grid[i][x]!=0&&nums.contains(grid[i][x])){
                        
                        nums[grid[i][x]-1] = 0;
                        leftovers--;
                        
                    }
                    if(grid[y][i]!=0&&nums.contains(grid[y][i])){
                        nums[grid[y][i]-1] = 0;
                    }
                }
                int R = x/3, C = y/3;
                for(int i = 0; i<3; i++){
                    for(int j = 0; j<3; j++){
                        if(nums.contains(grid[R+i][R+j])){
                            nums[grid[R+i][C+j]-1] = 0;
                            leftOvers--;
                        }
                    }
                }
                if(leftOvers==1){
                    for(int res:nums){
                        if(res>0){
                            grid[y][x] = res;
                            break;
                        }
                    }
                }
                if(notDone(grid))break;
            }
            for(int[] i:grid){
                for(int j:i){
                    System.out.printf("%d ",j);
                }
                System.out.println();
            }
        }
    }
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int N = s.nextInt();
        for(int i = 0; i<N; i++){
            int[][] board = new int[9][9];
            for(int j = 0;j<9;j++){
                for(int k = 0; k<9; k++){
                    board[i][j] = s.nextInt();
                }
            }
            solve(board);
        }
    }
}
