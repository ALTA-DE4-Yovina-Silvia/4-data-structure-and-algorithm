## PART 2 – Searching and Sorting
# Problem 1- Find Min and Max Number 
def find_min_max(arr):
    if not arr:
        return None, None, None, None

    min_val = max_val = arr[0]
    min_index = max_index = 0

    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
            min_index = i
        if arr[i] > max_val:
            max_val = arr[i]
            max_index = i

    return min_val, min_index, max_val, max_index

input1 = [5, 7, 4, -2, -1, 8]
input2 = [2, -5, -4, 22, 7, 7]

min_val, min_index, max_val, max_index = find_min_max(input1)
print(f"Input: {input1}")
print(f"Output: min: {min_val} index: {min_index} max: {max_val} index: {max_index}")

min_val, min_index, max_val, max_index = find_min_max(input2)
print(f"Input: {input2}")
print(f"Output: min: {min_val} index: {min_index} max: {max_val} index: {max_index}")


# Problem 2 - Maximum Buy Product
def max_items(money, productPrice):
    unique_prices = sorted(set(productPrice))
    
    count = 0
    for price in unique_prices:
        if money >= price:
            money -= price
            count += 1
        else:
            break
            
    return count

money1 = 50000
productPrice1 = [25000, 25000, 10000, 14000]
output1 = max_items(money1, productPrice1)
print(f"Input: money = {money1}, productPrice = {productPrice1}")
print(f"Output: {output1}")

money2 = 30000
productPrice2 = [15000, 10000, 12000, 5000, 3000]
output2 = max_items(money2, productPrice2)
print(f"Input: money = {money2}, productPrice = {productPrice2}")
print(f"Output: {output2}")


# Problem 3 - Playing Domino
def playingDomino(kartu, deck):
    suggested_card = []
    max_sum = -1

    for card in kartu:
        if deck[0] in card or deck[1] in card:
            card_sum = sum(card)
            if card_sum > max_sum:
                max_sum = card_sum
                suggested_card = card

    return suggested_card

kartu1 = [[6, 5], [3, 4], [2, 1], [3, 3]]
deck1 = [4, 3]
output1 = playingDomino(kartu1, deck1)
print(f"Input: kartu = {kartu1}, deck = {deck1}")
print(f"Output: {output1}")


# Problem 4 - Count Item and Sort
def most_appear_item(items):
    item_count = {}
    for item in items:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1
    
    sorted_items = sorted(item_count.items(), key=lambda x: x[1])
    
    result = []
    for item, count in sorted_items:
        result.append(f"{item}->{count}")
    
    return ' '.join(result)

# Sample Test Case
input_items = ["js", "js", "golang", "ruby", "ruby", "js", "js"]
output = most_appear_item(input_items)
print(f"Input: {input_items}")
print(f"Output: {output}")


