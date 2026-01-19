$scenario = [
    "\"재귀함수가 뭔가요?\"",
    "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.",
    "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.",
    "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""
]

$final_scenario = [
    "\"재귀함수가 뭔가요?\"",
    "\"재귀함수는 자기 자신을 호출하는 함수라네\"",
    "라고 답변하였지."
]

def print_script(cnt, str)
    puts "_" * 4 * cnt + str

end

def recursive_professor(i, n)
    if i == 1
        puts "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."
    end

    $scenario.each do |str|
        print_script(i-1, str)
    end

    if i == n
        $final_scenario.each do |str|
            print_script(n, str)
        end
    else
        recursive_professor(i+1, n)
    end
    print_script(i-1, "라고 답변하였지.")
end

def main
    n = gets.to_i
    recursive_professor(1, n)
end

main