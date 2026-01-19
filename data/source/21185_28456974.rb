n = gets.to_i
if n % 2 == 1
    print 'Either'
elsif (n/2) % 2 == 1
    print 'Odd'
else
    print 'Even'
end
