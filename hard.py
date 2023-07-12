def find_combinations(numbers, target):
    result = []

    def back(remaining, comb):
        if sum(comb) == target:
            result.append(comb)
        elif sum(comb) < target:
            for i in range(len(remaining)):
                new_combination = comb + [remaining[i]]
                new_remaining = remaining[:i] + remaining[i+1:]
                back(new_remaining, new_combination)

    back(numbers, [])
    return result


number_list = input("Tam sayı dizisini girin (virgülle ayırarak): ").split(",")
number_list = [int(num.strip()) for num in number_list]

target_number = int(input("Hedef sayıyı girin: "))


combinations = find_combinations(number_list, target_number)


print("Hedef sayıya ulaşan kombinasyonlar:")
for combination in combinations:
    print(combination)




