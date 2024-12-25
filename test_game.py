import pytest
from gameparts import Board


@pytest.fixture
def empty_board():
    """Фикстура для создания пустого игрового поля."""
    return Board()


def test_board_initialization(empty_board):
    """Тест инициализации игрового поля."""
    assert empty_board.board == [[' ' for _ in range(3)] for _ in range(3)]


def test_make_move(empty_board):
    """Тест выполнения хода игрока."""
    empty_board.make_move(0, 0, 'X')
    assert empty_board.board[0][0] == 'X'


def test_make_multiple_moves(empty_board):
    """Тест нескольких ходов и их правильной записи."""
    empty_board.make_move(0, 0, 'X')
    empty_board.make_move(1, 1, 'O')
    assert empty_board.board[0][0] == 'X'
    assert empty_board.board[1][1] == 'O'


def test_check_win_horizontal(empty_board):
    """Тест проверки победы по горизонтали."""
    empty_board.make_move(0, 0, 'X')
    empty_board.make_move(0, 1, 'X')
    empty_board.make_move(0, 2, 'X')
    assert empty_board.check_win('X') is True


def test_check_win_vertical(empty_board):
    """Тест проверки победы по вертикали."""
    empty_board.make_move(0, 0, 'O')
    empty_board.make_move(1, 0, 'O')
    empty_board.make_move(2, 0, 'O')
    assert empty_board.check_win('O') is True


def test_check_win_diagonal(empty_board):
    """Тест проверки победы по диагонали."""
    empty_board.make_move(0, 0, 'X')
    empty_board.make_move(1, 1, 'X')
    empty_board.make_move(2, 2, 'X')
    assert empty_board.check_win('X') is True


def test_check_win_reverse_diagonal(empty_board):
    """Тест проверки победы по обратной диагонали."""
    empty_board.make_move(0, 2, 'O')
    empty_board.make_move(1, 1, 'O')
    empty_board.make_move(2, 0, 'O')
    assert empty_board.check_win('O') is True


def test_is_board_full(empty_board):
    """Тест проверки заполненности игрового поля."""
    for i in range(3):
        for j in range(3):
            empty_board.make_move(i, j, 'X' if (i + j) % 2 == 0 else 'O')
    assert empty_board.is_board_full() is True


def test_is_board_not_full(empty_board):
    """Тест для проверки, что поле не заполнено."""
    empty_board.make_move(0, 0, 'X')
    assert empty_board.is_board_full() is False


def test_no_win_on_empty_board(empty_board):
    """Тест отсутствия победителя на пустом поле."""
    assert empty_board.check_win('X') is False
    assert empty_board.check_win('O') is False
