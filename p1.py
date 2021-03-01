products =[]

while True:
	name = input('请输入商品名称:')
	if name == 'q':
		break

	price = input('价格:')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)         # 省略写法为products.append([name,price])
print(products)

for p in products:
	print(p[0])

	print(p[0],'的价格是:', p[1])


with open ('products.txt','w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')


#寫入檔案
with open ('products.csv','w', encoding = 'utf-8') as f:
	f.write('商品 ,价格\n')      #写入栏位名称
	for p in products:
		f.write(p[0] + "," + p[1] + '\n')    #真正的寫入檔案
    	                                     # csv檔以逗點做區格

