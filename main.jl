dice = ["モ", "ン", "ダ", "ミ", "ン", "ン"]
diceroll = []
count = 0
result = false

while !result
    for i = 1:6
        push!(diceroll, dice[rand(1:6)])
        if diceroll[i] == dice[i] && i == 6
            global result = true
            break
        elseif diceroll[i] == dice[i]
            continue
        else
            global count += 1
            global diceroll = []
            break
        end
    end
end

println("Match")
println(diceroll, count)