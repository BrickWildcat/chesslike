# ChessLike: a roguelike on a chess board
*Started for MTU SYP 2022*

Play as a white pawn capturing hordes of enemies, doing your best to survive. Click on your piece to move. Collect hearts to increase your HP and upgrade your piece.

# Pieces
**Pawn** *(Common enemy)*:
Unlike in chess, the pawn is able to both move and capture one space in any direction. While its range may seem underwhelming, pawns' adaptable movement is very valuable in ChessLike.
The pawn is always available to the player.

**Knight** *(Uncommon enemy)*:
The knight moves in an "L"-shape (2 spaces in a cardinal direction, then 1 space 90° to the left or right), and is able to jump over other pieces.
The knight is unlocked for the player at 3 HP.

**Bishop** *(Uncommon enemy)*:
The bishop moves any amount of spaces diagonally, as long as its path isn't blocked. Due to its diagonal movement, the bishop cannot change the color of the square that it is on.
The bishop is unlocked for the player at 3 HP.

**Rook** *(Rare enemy)*:
The rook moves any amount of spaces in a cardinal direction, as long as its path isn't blocked. It can access any square on the board in at most 2 turns. It is impossible for the rook to spawn as the first enemy, but it will become more common as the game progresses.
The rook is unlocked for the player at 5 HP.

**Queen** *(Very rare enemy)*:
The queen combines the movement of the bishop and rook, allowing it to move any amount of spaces in any direction, as long as its path isn't blocked. The queen is the most powerful piece in the game, and will not spawn until the player has made considerable progress.
The queen is unlocked for the player at 9 HP.

# Running
ChessLike was exclusively developed for and on Linux, and uses a Linux-specific command to play audio. This may cause crashes on other OSes.

To run, either double click on `chesslike.py` (in the `game` folder) or run it in the terminal (`./chesslike.py`).

(Note: `__main__.py` has been renamed to `chesslike.py`)