# Insert a card in a list of sorted cards

card_lists = []
total_cards = int(input("Enter the total number of cards : "))
for card in range(1, total_cards + 1):
    card_lists.append(card)
print(f'Sorted Card List : {card_lists}')
card_number = int(input(f"Enter a card number that you want to insert into the sorted card list {card_lists} : "))
position = int(input(f"Enter the position that the card to be inserted in ... The position is to be less than {total_cards} : "))
if(position < total_cards):
    card_lists.insert(position - 1, card_number)
    print(f"Cards : {card_lists}")
else :
    card_lists.append(card_number)
    print(f"Cards : {card_lists}")
