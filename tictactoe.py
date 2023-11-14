class TicTacToe:
  def __init__(self):
      self.board = [' ' for _ in range(9)]

  def display_board(self):
      for i in range(0, 9, 3):
          print(' | '.join(self.board[i:i + 3]))
          if i < 6:
              print('---------')

  def available_moves(self):
      return [i for i, spot in enumerate(self.board) if spot == ' ']

  def check_win(self, player):
      win_conditions = [
          [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
          [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
          [0, 4, 8], [2, 4, 6]  # Diagonals
      ]

      for condition in win_conditions:
          if all(self.board[i] == player for i in condition):
              return True
      return False

  def game_over(self):
      if ' ' not in self.board or self.check_win('X') or self.check_win('O'):
          return True
      return False

  def minimax(self, maximizing):
      if self.game_over():
          if self.check_win('X'):
              return 1
          elif self.check_win('O'):
              return -1
          else:
              return 0

      if maximizing:
          best_score = float('-inf')
          for move in self.available_moves():
              self.board[move] = 'X'
              score = self.minimax(False)
              self.board[move] = ' '
              best_score = max(score, best_score)
          return best_score
      else:
          best_score = float('inf')
          for move in self.available_moves():
              self.board[move] = 'O'
              score = self.minimax(True)
              self.board[move] = ' '
              best_score = min(score, best_score)
          return best_score

  def best_move(self):
      best_score = float('-inf')
      best_move = None
      for move in self.available_moves():
          self.board[move] = 'X'
          score = self.minimax(False)
          self.board[move] = ' '
          if score > best_score:
              best_score = score
              best_move = move
      return best_move

  def play(self):
      while not self.game_over():
          self.display_board()

          user_input = int(input("Your move (0-8): "))
          if user_input in self.available_moves():
              self.board[user_input] = 'O'
          else:
              print("Invalid move. Try again.")
              continue

          if self.game_over():
              continue

          best_move = self.best_move()
          self.board[best_move] = 'X'

      self.display_board()
      if self.check_win('X'):
          print("AI wins!")
      elif self.check_win('O'):
          print("You win!")
      else:
          print("It's a tie!")


game = TicTacToe()
game.play()
