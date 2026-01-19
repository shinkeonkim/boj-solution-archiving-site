a,b,x,y=gets.split.map(&:to_i)
p (a+b+x+y-[[a,x].min,[b,y].min].max)*2