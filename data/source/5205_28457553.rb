def dis(a,b)
  return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2
end

for tc in 1..gets.to_i
  n = gets.to_i
  l = []
  for i in 1..n
    l << gets.split.map(&:to_i)
  end
  answers,mx = [0]*3
  for i in 0..n-1
    for j in i+1..n-1
      crt = dis(l[i],l[j])
      if mx < crt
        mx = crt
        answers = [[i,j]]
      elsif mx == crt
        answers << [i, j]
      end
    end
  end
  puts "Data Set #{tc}:"
  answers.each do |answer|
    puts "#{answer[0]+1} #{answer[1]+1}"
  end
end