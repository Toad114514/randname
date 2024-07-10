import random
import os
import time
import ct
# github in https://github.com/Toad114514/randname
# 网盘链接 in https://pan.huang1111.cn/s/m78eS1?path=%2Fpython%2Frandname
# randname by toad114514

# 更新日志 
# 2024.7.09
# v0.126k 第一个版本
# v0.223k 加入了删除项目
# v0.225k 加入源码注释 以后更新也会加注释
# v1.02b 加入其他选项画饼
# v1.03b 加入点名动画
# 2024.7.10
# v1.031b 优化了循环loop
# v1.04b 加入配置文件保存与读取
# v1.05b 加入清除配置功能 (其他选项里的菜单)
# v1.06b 优化列表查看 加入所有列表提示
# v1.07b 通过 colortext 库优化输出
# v1.08b 新增跳过随机动画选项
# v1.09b 

print('''
随机点名系统
By Toad114514
v1.09b
''')

time.sleep(1)

# 检查列表文件是否存在
if not os.path.exists('./config.txt'):
    # 创建文件
    os.mknod('./config.txt')
    # 初始化文件
    newfile = open('./config.txt','w')
    newfile.write('[]')
    newfile.close()
    print(ct.info(),'无配置文件，已创建一个新的配置文件')
    time.sleep(1)

# 初始化变量
list = []
# 默认配置
# 配置 class
class option():
	skip_random_animation = False

# 保存列表位置
def save_config(sendlist):
	with open('./config.txt','w') as fuck:
	    # 遍历列表并保存
		for k in sendlist:
			fuck.write(k + ',')

# 动画
def animation():
    # 初始动画变量
	timewait = 0
	result = []
	# 设置等待时间
	for timeless in range(100):
	   	if timeless <= 50:
	   		timewait = 0.05
	   	elif timeless <= 70:
	   		timewait = 0.1
	   	elif timeless <= 90:
	   		timewait = 0.2
	   	elif timeless <= 95:
	   		timewait = 0.5
	   	elif timeless <= 96:
	   		timewait = 0.7
	   	elif timeless <= 97:
	   		timewait = 0.9
	   	elif timeless <= 98:
	   		timewait = 1
	   	elif timeless == 99:
	   		timewait = 1.2
	    # 随机元素
	   	result = random.sample(list,1)
	   	print(result)
	   	time.sleep(timewait)
	   	os.system('clear')
	return result

# 空命令
def em():
	return 0

# 随机点名
def randname():
    # 初始 while
	rand = True
	while rand:
	   print('开始点名')
	   time.sleep(1)
	   # 检查是否跳过动画
	   if option.skip_random_animation == False:
	    # 动画显示
	   	result = animation()
	   else:
	    # 直接随机点名
	   	result = random.sample(list,1)
	   os.system('clear')
	   # 显示结果
	   print('抽到的是',result)
	   gde = input('1 再抽一次  [其他] 返回')
	   if gde == '1':
	    # 一个空函数跳过并重新抽名
	   	em()
	   else:
	   	rand = False

# 初始 charkey
charkey = ''
# 打开配置文件
with open('./config.txt','r') as sb:
    # 读取列表
	listopen = sb.read()
	# 遍历读取
	for listby in listopen:
		charkey = charkey + listby
		if listby == ",":
			charkey = charkey.replace(',','')
			# 添加到列表在最后面
			list.append(charkey)
			charkey = ""

# 设置 while
whiles = True

while whiles:
	os.system('clear')
	# 显示菜单
	print('添加、查看或删除项目')
	sel = input('1 添加  2 查看  3 删除  4 开始点名  5 其他  6 退出\n')
	# 判断选项
	if sel == '1':
		print('请输入要添加的项目 (添加多个在每个名字中间用英文逗号隔开)')
		back = input('输入：')
		# 初始化 charkey
		charkey = ''
		back = back + ","
		# 遍历列表
		for back2 in back:
			charkey = charkey + back2
			if back2 == ',':
			    charkey = charkey.replace(',', "")
			    # 添加到列表结尾
			    list.append(charkey)
			    charkey = ''
		# 保存配置列表
		save_config(list)
		print(ct.done(),'添加完成')
	if sel == '2':
	    # 遍历查看列表
		for backey in list:
			print(backey)
		print(ct.info(),'已展示所有随机列表名字')
		input('')
	if sel == '3':
		back = input('请输入一个人的名字并删除')
		# 遍历查看删除
		for i in list:
			if i == back:
			    # 删除元素
				list.remove(i)
		# 保存列表
		save_config(list)
		print(ct.done(),'删除完成')
	if sel == "4":
	    # 随机名
		randname()
	if sel == "6":
	    # 设置 whiles 退出
		whiles = False
	if sel == "5":
	    # 内置菜单
		print('其他选项菜单\n1 清除列表数据文件  2 暗箱操作  3 选项  [任意] 退出')
		sel = input('')
		if sel == '1':
			os.system('clear')
			print('这很危险！\n删除配置文件后，下次启动随机系统列表将为空\n你确定要这样做吗[y/n]')
			sel = input('')
			if sel == 'y':
				os.remove('./config.txt')
				# 初始重启
				print(ct.done(),'已完成操作，请重新启动程序。')
				whiles = False
			elif sel == 'n':
			    # 空函数
				em()
		elif sel == '2':
			em()
		elif sel == '3':
		    # 跳过随机动画
			print('选项\n1 跳过随机动画  [任意] 返回')
			sel = input('')
			if sel == "1":
				skip_option_back = input('跳过随机动画？[y/n]')
				# 判断动画选项
				if skip_option_back == 'y':
					option.skip_random_animation = True
				elif skip_option_back == "n":
					option.skip_random_animation = False
				else:
					em()	
		else:
			em()