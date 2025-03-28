weekly_menu = []

for meal in range(0,7):
    weekly_menu.append(input("What meal would you like to add to the menu? "))


print(f"Here's your weekly menu\nMonday: {weekly_menu[0]}\nTusday: {weekly_menu[1]}\nWednesday: {weekly_menu[2]}\nThursday: {weekly_menu[3]}\nFriday: {weekly_menu[4]}\nSaturday: {weekly_menu[5]}\nSunday: {weekly_menu[6]}")



try:
    change_day = int(input("What day's menu would you like to change? Choose between 0 (Monday) and 6 (Sunday): "))
    meal = input(f"What meal would you like to replace {weekly_menu[change_day]} with? ")
    weekly_menu[change_day] = meal

except IndexError:
    print("Yeah, I wish there were more days in a week - but here we are. Let's try again")

except ValueError:
    print("Please, use numbers from 0 to 6")

else:
    print(f"Very well. Here's the updated menu\nMonday: {weekly_menu[0]}\nTusday: {weekly_menu[1]}\nWednesday: {weekly_menu[2]}\nThursday: {weekly_menu[3]}\nFriday: {weekly_menu[4]}\nSaturday: {weekly_menu[5]}\nSunday: {weekly_menu[6]}")
finally:
    print("Have a good day")
