# {
#     "Home_score": 3,
#     "Away_score": 1,
# }

def get_result(final_score):
    if final_score["Home_score"] > final_score["Away_score"]:
        return "Home win"
    elif final_score["Home_score"] < final_score["Away_score"]:
        return "Away win"
    else:
        return "Draw"

def get_results(final_scores):
    results = [get_result(score) for score in final_scores]
    return results
    # (You could try and use a list comprehension for this)