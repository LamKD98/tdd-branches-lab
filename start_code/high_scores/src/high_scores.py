def latest(scores):
    # return scores[len(scores) -1]
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    sorted_scores = sorted(scores, reverse = True)
    return sorted_scores[0:3]
    

def high_to_low(scores):
    return sorted(scores, reverse = True)

