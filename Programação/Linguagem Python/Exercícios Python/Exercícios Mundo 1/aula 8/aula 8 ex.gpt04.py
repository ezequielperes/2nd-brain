from emoji import emojize
import datetime
emoji = ':five_o’clock: '
date = str(datetime.datetime.today())
hour = date[11:19]
print('-'*30)
print(emojize(f'{emoji + hour :-^42}'))
print('-'*30)
