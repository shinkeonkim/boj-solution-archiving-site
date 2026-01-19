n = gets.to_i
l = Array.new(n) { gets.split.map(&:to_i) }
puts Math.sqrt((l[0][0] - l[n - 1][0]) ** 2 + (l[0][1] - l[n - 1][1]) ** 2)
