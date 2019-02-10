def calculate_nps(scores):


    detractors_count = 0
    neutrals_count = 0
    promoters_count = 0

    for score in scores:
        if score < 7:
            # detractors_count = detractors_count + 1
            detractors_count += 1

        if 7 <= score <= 8:
            neutrals_count += 1

        if score > 8:
            promoters_count += 1

    result = round((promoters_count - detractors_count) / len(scores) * 100)
    return result

print(calculate_nps([8,7]))
print(calculate_nps([1,3]))
print(calculate_nps([10,9]))