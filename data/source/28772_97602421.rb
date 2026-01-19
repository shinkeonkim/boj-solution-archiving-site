s = gets.chomp.split
h = Hash.new(0)
s.each { |word|  h[word] += 1 if word.start_with?("#") and word[1..] !~ /#/ and word.length > 1 }

puts h.size
h.each do |word, count|
  puts "#{word} #{count}"
end
