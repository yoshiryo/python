def sushi_choice(cost_list,kcal_list,limit):
    list_len = len(kcal_list)
    dp_table = [[0 for j in range(limit + 1)] for i in range(list_len)]
 
    # 1品目を食べるか食べないか
    for j in range(limit + 1):
        if kcal_list[0] <= j:
            dp_table[0][j] = cost_list[0] # 食べるとき
 
    # 2品目以降を食べるか食べないか
    for i in range(1,list_len):
        for j in range(limit + 1):
            tmp_not_choice = dp_table[i-1][j]
            if kcal_list[i] > j: # カロリーオーバー
                dp_table[i][j] = tmp_not_choice # 食べられない
            else:
                tmp_choice = dp_table[i-1][j - kcal_list[i]] + cost_list[i]
                dp_table[i][j] = max(tmp_choice,tmp_not_choice)
 
    return dp_table[list_len - 1][limit]
 
 
cost = [120,150,140,110,100] # それぞれの寿司の値段
kcal = [8,10,7,6,7] # それぞれの寿司のカロリー [×10]
ans = sushi_choice(cost,kcal,30)
print(ans)