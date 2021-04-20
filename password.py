#密碼重試
#先設密碼password = 'a123456'
#讓使用者重複輸入
#讓使用者[最多3次]
#不對就印出"密碼錯誤! 還有__次機會"
#對的就印出"登入成功!"
paw1 = 'a123456'
x = 1
y = 3
while y > 0:
	paw2 = input('請輸入密碼: ')	
	y = y - 1
	if paw1 == paw2:
		print('登入成功!')
		break
	else:
		print('密碼錯誤! 還有', y, '次機會')
		x = x + 1