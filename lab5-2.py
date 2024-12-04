def knapsack(weights, values, W):
    n = len(values)  # Нийт эд зүйлсийн тоо
    # dp[i][w] нь эхний i эд зүйлсийг ашиглан багтаамж w хүртэл үүргэвчинд багтаах боломжтой хамгийн их үнэ цэнэ
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # dp хүснэгтийг дүүргэх
    for i in range(1, n + 1):  # Эд зүйлсийг гүйцэтгэх
        for w in range(1, W + 1):  # Багтаамжийг гүйцэтгэх
            if weights[i - 1] <= w:  # Одоогийн эд зүйл үүргэвчинд багтах эсэх
                # Энэ эд зүйлийг авах болон авахгүй тохиолдлуудын аль ихийг сонгох
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                # Энэ эд зүйлийг авч болохгүй
                dp[i][w] = dp[i - 1][w]

    # Үүргэвчний багтаамж W доторх хамгийн их үнэ цэнэ
    return dp[n][W]

# Жишээ ашиглалт:
values = [60, 100, 120]  # Эд зүйлсийн үнэ цэнэ
weights = [10, 20, 30]  # Эд зүйлсийн жин
W = 50  # Үүргэвчний дээд багтаамж
result = knapsack(weights, values, W)
print(f"Үүргэвчинд багтах хамгийн их үнэ цэнэ: {result}")
