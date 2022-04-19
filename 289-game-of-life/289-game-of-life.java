class Solution {
    public void gameOfLife(int[][] board) {
        int[][] dupboard = new int[board.length][board[0].length];
        for(int i = 0;i<board.length;i++){
          for(int j = 0; j<board[0].length;j++){
            int livesCount = 0;
            if (i - 1 >= 0 &&  j - 1 >= 0 && board[i - 1][j - 1] == 1)
                livesCount = livesCount + 1;
            if (j - 1 >= 0 && board[i][j - 1] == 1)
                livesCount = livesCount + 1;
            if  (i + 1 < board.length && j - 1 >= 0 && board[i + 1][j - 1] == 1)
                livesCount = livesCount + 1;
            if (i - 1 >= 0 && j + 1 < board[0].length &&  board[i - 1][j + 1] == 1)
                livesCount = livesCount + 1;
            if (j + 1 < board[0].length &&  board[i][j + 1]  == 1)
                livesCount = livesCount + 1;    
            if (j + 1 < board[0].length && i + 1 < board.length  && board[i + 1][j + 1] == 1)
                livesCount = livesCount + 1;
            if (i - 1 >= 0 && board[i - 1][j] == 1)
                    livesCount = livesCount + 1;
            if (i + 1 < board.length && board[i + 1][j] == 1)
                livesCount = livesCount + 1;
                    
            if (board[i][j] == 0){
                if (livesCount == 3){
                    dupboard[i][j] = 1;
                }else {
                    dupboard[i][j] = 0;
                }
            }
                                    
            if (board[i][j] == 1){
                if ((livesCount == 2) || (livesCount == 3)){
                    dupboard[i][j] = 1;
                }else{dupboard[i][j] = 0;
                   }
            }      
          }  
        }
      for(int i = 0; i <dupboard.length; i++){
          for(int j = 0; j < dupboard[0].length; j++){
              board[i][j] = dupboard[i][j];
          }
      }
    }
}