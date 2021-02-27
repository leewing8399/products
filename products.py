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

	print(p[0],'的价格是', p[1])
	
