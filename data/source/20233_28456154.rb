a = gets.to_i # plan A monthly fee
x = gets.to_i # plan A minute fee
b = gets.to_i # plan B monthly fee
y = gets.to_i # plan B minute fee
daily_time = gets.to_i

plan_a_cost = a + 21 * [daily_time - 30, 0].max * x
plan_b_cost = b + 21 * [daily_time - 45, 0].max * y

print plan_a_cost, " ", plan_b_cost