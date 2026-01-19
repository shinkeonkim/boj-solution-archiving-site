gets.to_i.times do
    n = gets.to_i
    ans,min = 0, n+1
    l = []
    n.times do
        l << gets.split.map(&:to_i)
    end
    l = l.sort_by { |e| e[0] }
    
    l.each do |item|
        if min > item[1]
            ans+=1
            min = item[1]
        end
    end
    puts ans
end