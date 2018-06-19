import smtplib

emailContent = 'My Email Here - Hello World!'

mail = smtplib.SMTP('smtp.gmail.com',587)
mail.starttls()
mail.login('absurdjones@gmail.com', 'look to #00FF00')

mail.sendmail('absurdjones@gmail.com','mogsfromcongress@ymail.com', emailContent)

mail.close()
