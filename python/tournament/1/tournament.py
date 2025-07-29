def tally(rows):
    scores = {}
    final_result = ["Team                           | MP |  W |  D |  L |  P"]
    for match in rows:
        match: str
        team1, team2, result = match.split(";")
        if not team1 in scores: scores[team1] = {
            'MP'    : 0,
            'W'     : 0,
            'D'     : 0,
            'L'     : 0,
            'P'     : 0
        }

        if not team2 in scores: scores[team2] = {
            'MP'    : 0,
            'W'     : 0,
            'D'     : 0,
            'L'     : 0,
            'P'     : 0
        }

        scores[team1]['MP'] += 1
        scores[team2]['MP'] += 1

        if result == 'win':
            scores[team1]['W'] += 1
            scores[team2]['L'] += 1
            scores[team1]['P'] += 3

        if result == 'loss':
            scores[team2]['W'] += 1
            scores[team1]['L'] += 1
            scores[team2]['P'] += 3

        if result == 'draw':
            scores[team2]['D'] += 1
            scores[team1]['D'] += 1
            scores[team2]['P'] += 1
            scores[team1]['P'] += 1

    score_tuples = [tuple([team, scores[team]['MP'],scores[team]['W'],scores[team]['D'],scores[team]['L'], scores[team]['P']]) for team in scores]
    sorted_score_tuples = sorted(score_tuples, key= lambda x : (-x[-1], x[0]))
    for tup in sorted_score_tuples:
        final_result.append("|".join([
            f"{str(tup[0]).ljust(31)}",
            f"{str(tup[1]).ljust(2).rjust(4)}",
            f"{str(tup[2]).ljust(2).rjust(4)}",
            f"{str(tup[3]).ljust(2).rjust(4)}",
            f"{str(tup[4]).ljust(2).rjust(4)}",
            f"{str(tup[5]).rjust(3)}",
        ]))


    return final_result

