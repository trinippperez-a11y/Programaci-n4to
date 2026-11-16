import random


class TicTacToe:
    """Juego de Ta-Te-Ti (Tres en línea) para 2 jugadores."""

    def __init__(self):
        self.board = []

    def create_board(self):
        """Crea el tablero 3x3 vacío."""
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        """Devuelve 0 u 1 al azar para decidir quién empieza."""
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        """Coloca la ficha del jugador en la casilla indicada."""
        self.board[row][col] = player

    def is_player_win(self, player):
        """Devuelve True si el jugador tiene 3 en línea."""
        n = len(self.board)

        # Comprobar filas
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return True

        # Comprobar columnas
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return True

        # Diagonal principal
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return True

        # Diagonal secundaria
        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return True

        return False

    def is_board_filled(self):
        """Devuelve True si no quedan casillas libres."""
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        """Devuelve el otro jugador."""
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        """Imprime el tablero en pantalla."""
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        """Bucle principal del juego."""
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'

        while True:
            print(f"\nTurno del jugador {player}")
            self.show_board()

            # Leer fila y columna del usuario
            try:
                row, col = list(
                    map(int, input("Introduzca fila y columna (ej: 1 1): ").split())
                )
            except ValueError:
                print("❌ Entrada inválida. Escribe dos números separados por espacio.\n")
                continue

            # Validar rango
            if not (1 <= row <= 3 and 1 <= col <= 3):
                print("❌ Fuera del tablero. Usa números del 1 al 3.\n")
                continue

            # Validar casilla libre
            if self.board[row - 1][col - 1] != '-':
                print("❌ Casilla ya ocupada. Elige otra.\n")
                continue

            # Colocar ficha
            self.fix_spot(row - 1, col - 1, player)

            # Comprobar victoria
            if self.is_player_win(player):
                print(f"\n🏆 ¡El jugador {player} gana la partida!")
                break

            # Comprobar empate
            if self.is_board_filled():
                print("\n🤝 ¡Empate!")
                break

            # Cambiar turno
            player = self.swap_player_turn(player)

        # Mostrar tablero final
        print("\nTablero final:")
        self.show_board()


# Iniciar el juego
if __name__ == "__main__":
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()