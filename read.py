data = []
count = 0
with open('reviews.txt', 'r')as f:
	for line in f: #逐一讀取檔案中的每一行，將其存放在變數 line 中
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print(len(data))

print(f'檔案讀取完了,總共有{len(data)}筆資料')

sum_len = 0
for w in data:
	sum_len += len(w)
print('留言的平均長度為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])



