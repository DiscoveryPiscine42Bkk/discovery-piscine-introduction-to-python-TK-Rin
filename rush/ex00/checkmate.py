def pos_in_board(board, x, y):
    return 0 <= x < len(board) \
        and 0 <= y < len(board)

def pos_has_piece(board, x, y):
    return board[y][x] != "."

def pos_has_king(board, x, y):
    return board[y][x] == "K"

def check_move(board, x, y):
    if not pos_in_board(board, x, y):
        return "stop"
    elif pos_has_king(board, x, y):
        return "king"
    elif pos_has_piece(board, x, y):
        return "stop"
    else:
        return "none"


def pawn_move(board, piece_x, piece_y):
    next_x = piece_x - 1
    next_y = piece_y - 1
    if pos_in_board(board, next_x, next_y) and pos_has_king(board, next_x, next_y):
        return True

    next_x = piece_x + 1
    next_y = piece_y - 1
    if pos_in_board(board, next_x, next_y) and pos_has_king(board, next_x, next_y):
        return True

    return False


def rook_move(board, piece_x, piece_y):
    size = len(board)

    y = piece_y
    while y > 0:
        y -= 1
        match check_move(board, piece_x, y):
            case "stop":
                break
            case "king":
                return True
            case "none":
                continue


    y = piece_y
    while y < size:
        y += 1
        match check_move(board, piece_x, y):
            case "stop":
                break
            case "king":
                return True
            case "none":
                continue

    x = piece_x
    while x > 0:
        x -= 1
        match check_move(board, x, piece_y):
            case "stop":
                break
            case "king":
                return True
            case "none":
                continue

    x = piece_x
    while x < size:
        x += 1
        match check_move(board, x, piece_y):
            case "stop":
                break
            case "king":
                return True
            case "none":
                continue


def bishop_move(board, piece_x, piece_y):
    size = len(board)

    x = piece_x
    y = piece_y
    while y > 0 and x < size:
        y -= 1
        x += 1
        match check_move(board, x, y):
            case "stop":
                break
            case "king":
                return True
            case "none":
                continue

    x = piece_x
    y = piece_y
    while y > 0 and x > 0:
        y -= 1
        x -= 1
        match check_move(board, x, y):
            case "stop":
                break
            case "king":
                return True
            case "none":
                continue

    x = piece_x
    y = piece_y
    while y < size and x > 0:
        y += 1
        x -= 1
        match check_move(board, x, y):
            case "stop":
                break
            case "king":
                return True
            case "none":
                continue

    x = piece_x
    y = piece_y
    while y < size and x < size:
        y += 1
        x += 1
        match check_move(board, x, y):
            case "stop":
                break
            case "king":
                return True
            case "none":
                continue


def queen_move(board, piece_x, piece_y):
    if bishop_move(board, piece_x, piece_y):
        return True
    if rook_move(board, piece_x, piece_y):
        return True
    return False


def parse_board(board_str):
    if not isinstance(board_str, str):
        raise ValueError("The board is not a String")

    board_str = board_str.strip()
    if len(board_str) == 0:
        raise ValueError("The board is empty")

    board = []
    board_width = 0
    for line in board_str.splitlines():
        line = line.strip()
        row = []
        row_width = len(line)

        if board_width == 0:
            board_width = row_width
        elif row_width != board_width:
            raise ValueError("The board has inconsistant width")

        for char in line:
            char_upper = char.upper()
            if char_upper in[".", "P", "B", "R", "Q", "K"]:
                row.append(char_upper)
            else:
                raise ValueError(f"Unknown character: {char}")

        board.append(row)

    board_height = len(board)
    if board_height != board_width:
        raise ValueError(f"The board is not a square ({board_width}x{board_height})")

    return board


def determine_check(board):
    size = len(board)
    for y in range(0, size):
        for x in range(0, size):
            piece = board[y][x]
            if piece == ".":
                continue
            match piece:
                case "R":
                    if rook_move(board, x, y):
                        return True
                case "P":
                    if pawn_move(board, x, y):
                        return True
                case "B":
                    if bishop_move(board, x, y):
                        return True
                case "Q":
                    if queen_move(board, x, y):
                        return True
                case ".":
                    continue
    return False


def checkmate(board_str):
    try:
        board = parse_board(board_str)
    except ValueError as err:
        print("Error:", err)
        return
    except TypeError as err:
        print("Error:", err)
        return

    if determine_check(board):
        print("Success")
    else:
        print("Fail")