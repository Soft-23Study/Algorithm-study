n = int(input())
countries = list(map(int, input().split()))
money = int(input())

total_sum = sum(countries)
budget = max(countries)

if money < total_sum:
    min_budget = 0
    max_budget = max(countries)

    while min_budget <= max_budget:
        sum_budget = 0
        mid = (min_budget + max_budget) // 2

        for country in countries:
            if country <= mid:
                sum_budget += country
            else:
                sum_budget += mid

        if sum_budget > money:
            max_budget = mid - 1
        else:
            min_budget = mid + 1
            budget = mid

print(budget)