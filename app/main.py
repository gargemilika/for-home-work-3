first_score = 7
second_score = 10
third_score = 10

detractors_count = 0
neutrals_count = 0
promoters_count = 0

if first_score < 7:
    # detractors_count = detractors_count + 1
    detractors_count += 1

if 7 <= first_score <= 8:
    neutrals_count += 1

if first_score > 8:
    promoters_count += 1

# как интерпретировать невалидные данные?

if second_score < 7:
    # detractors_count = detractors_count + 1
    detractors_count += 1

if 7 <= second_score <= 8:
    neutrals_count += 1

if second_score > 8:  # Ctrl + Shift + Alt + левой кнопкой мыши кликать (множественные курсоры)
    promoters_count += 1

if third_score < 7:
    # detractors_count = detractors_count + 1
    detractors_count += 1

if 7 <= third_score <= 8:
    neutrals_count += 1

if third_score > 8:  # Ctrl + Shift + Alt + левой кнопкой мыши кликать (множественные курсоры)
    promoters_count += 1

result = round((promoters_count - detractors_count) / 3 * 100)
print(result)
