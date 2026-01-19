def isP(s)
    for i in 0..(s.size/2)
        return false if s[i] != s[s.size - i - 1]
    end
    return true
end
gets.to_i.times do
    n = gets.to_i
    l = []
    n.times do
        l << gets.chomp
    end
    chk = true
    (0...n).each do |i|
        (i+1...n).each do |j|
            if isP l[i]+l[j]
                puts l[i]+l[j]
                chk = false
                break
            end
            if isP l[j]+l[i]
                puts l[j]+l[i]
                chk = false
                break
            end
        end
        break unless chk
    end
    puts 0 if chk
end