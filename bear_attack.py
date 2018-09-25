#設定怪獸的初始體力值
import random
eblood = random.randint(1,100)
pblood = random.randint(1,100)

#故事背景
print('這是一個打怪獸的遊戲\n')
print('你是個旅人，在森林里迷路了\n')
print('GRAAAAHHHHHH，你的面前出現了一只噴火的小熊熊🐻\n')
A1 = input('你選擇\nA.進入戰鬥模式\nB.逃跑\n')

#玩家選擇不戰鬥，遊戲結束
if A1 == 'B':
	print('你轉身就跑，小熊熊追了上來，一熊掌把你打倒在地\n')
	print('你掙扎著想要爬起來，但是你被小熊熊一屁股坐死了\n')
	print('GAME OVER 登楞')

#玩家選擇戰鬥，設置無線廻圈，并重複產生攻擊所減少的體力值
elif A1 == 'A':
	print('\n你拔出了你的小劍劍，準備戰鬥\n')
	print('「系統提示」小熊熊的體力值是', eblood, '/100\n')
	print('「系統提示」你的體力值是', pblood, '/100\n')
	while True:
		i = 0
		strike = random.randint(1,100)
		bstrike = random.randint(1,100)
		i += 1
		print('你用劍砍了小熊熊一次\n')
		print('小熊熊憤怒地向你撲來\n')
		print('痛痛！小熊熊讓你的體力值減少了', bstrike, '\n')
		eblood = eblood - strike
		pblood = pblood - bstrike
		print('你的攻擊讓小熊熊的體力值減少了', strike,'\n')
		print('「系統提示」你的體力值還剩下', pblood,'\n')
		print('「系統提示」小熊熊的體力值還剩下', eblood,'\n')
		if eblood <= 0 and eblood < pblood:
			print('你成功的征服了小熊熊\n')
			print('你一共攻擊了', i, '次\n')
			print('遊戲結束，謝謝你玩我，希望你玩的愉快😙\n')
			break
		if pblood <= 0 and pblood < eblood:
			print('你被小熊熊打死了\n')
			print('希望你成功通過所有的審判，獲得重生\n')
			print('重生后要記得再來玩我哦😊\n')
			break
		
