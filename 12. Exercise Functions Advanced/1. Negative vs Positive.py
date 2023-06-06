def positive_or_negative(positive, negative):
    print(negative)
    print(positive)

    if positive > abs(negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


sequence_of_numbers = [int(x) for x in input().split()]
positive_nums = sum(x for x in sequence_of_numbers if x > 0)

negative_nums = sum(x for x in sequence_of_numbers if x < 0)

positive_or_negative(positive_nums, negative_nums)
# 1 2 -3 -4 65 -98 12 57 -84