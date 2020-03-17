
def sort_scores(unsorted_scores, highest_possible_score):

    # Sort the scores in O(n) time.
    
    scores = [None] * (highest_possible_score + 1)
    
    for score in unsorted_scores:
        if scores[score]:
            scores[score] += 1
        else:
            scores[score] = 1

    final_scores = []
    
    for i in range(len(scores) - 1,-1,-1):
        if not scores[i]:
            continue
        score_list = [i] * scores[i]
        final_scores.extend(score_list)

    return final_scores