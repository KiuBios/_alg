def perm(n): 
	p = [] 
	return permNext(n, p) 

##def fac(n):
	f = 1
	for i in range(1, n+1):
		f = f * i
	return f

def permNext(n, p): # 已經排好 p[0..i-1], 繼續排下去 [i...n-1]
	i = len(p)
	if i == n:  # 全部排好了
		print(p)  # 印出排列
		return
	# 還沒排滿，繼續排下去
	for x in range(n): # 對本列的每一個 x 去嘗試
		if not x in p: # 若 x 不在排列中
			p.append(x)    # 把 x 放進盤面
			permNext(n, p) # 繼續遞迴尋找下一個排列
			p.pop()        # 把 x 移出盤面

n= int(input("排幾個 ?  "))		
perm(n)