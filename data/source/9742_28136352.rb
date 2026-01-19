STDIN.each_line do |line|
    str,n = line.split
    n = n.to_i
    arr = str.split("")
    
    result_permutation = arr.permutation(arr.length).to_a[n-1]
    
    print str, " ", n, " = "
    unless result_permutation.nil?
        result_permutation.each do |number|
            print number
        end
        puts ""
    else
        puts "No permutation"
    end
end