import sys


class error_argv(Exception):
    def __init__(self, message: str = "I reject to ans") -> None:
        super().__init__(message)


def turn_int(score_list: list[str]) -> list[int]:
    valid_list: list[int] = []
    for score in score_list:
        try:
            valid_list.append(int(score))
        except ValueError:
            print(f"Invalid parameter: '{score}'")
    return valid_list


def start_cal(score_list: list[str]) -> None:
    if len(score_list) < 1:
        raise error_argv("python3 ft_score_analytics.py <score1> <score2> ...")

    int_scores = turn_int(score_list)
    if not int_scores:
        raise error_argv("python3 ft_score_analytics.py <score1> <score2> ...")

    print(f"Scores processed: {int_scores}")
    print(f"Total players: {len(int_scores)}")
    print(f"Total score: {sum(int_scores)}")
    print(f"Average score: {sum(int_scores)/len(int_scores)}")
    print(f"High score: {max(int_scores)}")
    print(f"Low score: {min(int_scores)}")
    print(f"Score range: {max(int_scores) - min(int_scores)}\n")


print("=== Player Score Analytics ===")
try:
    score_list = sys.argv[1:]
    start_cal(score_list)
except error_argv as error:
    print(f"No scores provided. Usage: {error}")
