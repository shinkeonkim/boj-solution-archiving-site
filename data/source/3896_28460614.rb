MAX_NUM = 1300000
prime = [2]
check = [true] * MAX_NUM
(3..MAX_NUM).step(2).each do |i| 
    if check[i]
        prime << i
        (i+i..MAX_NUM).step(i).each do |j|
            check[j] = false
        end
    end
end

gets.to_i.times do 
    k = gets.to_i
    idx = prime.bsearch_index {|i| i > k}
    if prime[idx-1] == k || prime[idx+1] == k
        puts 0
    else
        puts prime[idx] - prime[idx-1]
    end
end