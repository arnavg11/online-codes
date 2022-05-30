import java.io.*;
import java.util.*;

public class Solution {
    byte[][] shipsSunk = {{0,2},{0,2},{0,3},{0,4},{0,5}};//submarine, destroyer, cruiser, battleship, carrier
    static int move(String[] board){
        byte[] moves = {1,-1};
        // if all discovered ships are not sunk.
        for(int i = 0; i<10; i++){
            for(int j = 0; j<10; j++){
                if(board[i].charAt(j) == 'h'){
                    for(int x:moves){
                        try{
                            if(board[i].charAt(j+x) == '-'){
                            System.out.printf("%d %d\n",i,(j+x));
                            return 0;
                            }
                        }catch(StringIndexOutOfBoundsException e){}
                        try{
                            
                            if(board[i+x].charAt(j)=='-'){
                            System.out.printf("%d %d\n",(i+x),j);
                            return 0;
                            }
                        }catch(ArrayIndexOutOfBoundsException e){}
                    }
                }
            }
        }
        
        
        //else
        Random r = new Random();
        int x = r.nextInt(10), y = r.nextInt(10);
        for(;;){
            if(board[y].charAt(x)=='-'){
                System.out.println(y+" "+x);
                break;
            }else{
                x = r.nextInt(9);
                y = r.nextInt(9);
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        
        Scanner s = new Scanner(System.in);
        byte N = s.nextByte();
        s.nextLine();
        String[] board = new String[N];
        for(int i = 0; i<N; i++){
            board[i] = s.nextLine();
        }
        move(board);
    }
}
