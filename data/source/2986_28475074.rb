N = gets.to_i
l = [1]
for i in 2..(Math.sqrt(N).to_i)
    if N % i == 0
        l << i
        l << N/i unless i*i == N
    end
end
print N - l.max
