kill, death, assist = gets.split("/").map { |str| str.to_i }

if kill + assist < death or death == 0
    puts "hasu"
else
    puts "gosu"
end
