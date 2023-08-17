import unittest
from tictactoe import TicTacToe

class TestTicTacToe(unittest.TestCase):

    def test_never_loses(self):
        game = TicTacToe()
        
        # Player X plays move 0.
        game.make_move(0, "X")
        
        # Machine should block at the center.
        machine_move = game.best_move()
        game.make_move(machine_move, "O")
        self.assertEqual(machine_move, 4)
        
        # Player X plays move 1.
        game.make_move(1, "X")
        
        # machine should block the win by playing at position 2.
        machine_move = game.best_move()
        game.make_move(machine_move, "O")
        self.assertEqual(machine_move, 2)
        
        # Player X plays move 3.
        game.make_move(3, "X")
        
        # At this point, the machine should be thinking of winning, but 
        # for simplicity, we just check that the machine doesn't allow X to win.
        machine_move = game.best_move()
        game.make_move(machine_move, "O")
        
        # Check if the game is still ongoing (i.e., no winner yet).
        self.assertEqual(game.check_winner(game.board), 10, "machine should win. code for machine win is 10.")

if __name__ == '__main__':
    unittest.main()
