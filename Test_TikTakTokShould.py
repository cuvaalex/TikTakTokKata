import unittest
from TikTakTok import TikTakTokGame



class TikTakTokShould(unittest.TestCase):
    def test_first_player_win_if_first_row_full(self):
        game = TikTakTokGame()

        game.play(0, 0)
        game.play(0, 1)
        game.play(1, 0)
        game.play(1, 1)
        result = game.play(2, 0)
        self.assertEqual(result, "Player X Win")


if __name__ == '__main__':
    unittest.main()
