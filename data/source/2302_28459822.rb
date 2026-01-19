fibo = [1,1,2,3]
for i in 4..40
    fibo << fibo[i-1] + fibo[i-2]
end

ans = 1
n = gets.to_i
fixed_seats = []
gets.to_i.times do
    fixed_seats << gets.to_i
end
fixed_seats << n + 1
fixed_seats = fixed_seats.sort
crt = 0
fixed_seats.each do |fixed_seat|
    ans *= fibo[fixed_seat - crt -1] 
    crt = fixed_seat
end
puts ans
