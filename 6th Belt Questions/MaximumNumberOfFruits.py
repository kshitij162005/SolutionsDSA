def totalFruit(fruits):
    max_fruits = 0
    left = 0
    basket = {}

    for right in range(len(fruits)):
        basket[fruits[right]] = basket.get(fruits[right], 0) + 1

        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1

        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits


if __name__ == "__main__":
    n = int(input())
    fruits = list(map(int, input().split()))

    result = totalFruit(fruits)

    print(result)
