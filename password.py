#密碼重試
#先設密碼password = 'a123456'
#讓使用者重複輸入
#讓使用者[最多3次]
#不對就印出"密碼錯誤! 還有__次機會"
#對的就印出"登入成功!"
pwd1 = 'a123456'
y = 3
while y > 0:
	y = y - 1
	pwd2 = input('請輸入密碼: ')		
	if pwd2 == pwd1:
		print('登入成功!')
		break
	else:
		if y > 0:		
			print('密碼錯誤! 還有', y, '次機會')
		else:
			print('密碼錯誤! 沒有機會')			