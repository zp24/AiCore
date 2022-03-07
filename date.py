from datetime import datetime
import dateutil.parser as parser

text = "24 February 1994"
date = parser.parse(text)

text1 = "29 December 1993"
date1 = parser.parse(text1)

date_obj = datetime.strptime(text, '%d %B %Y')
print("test", date_obj)
print(date.isoformat())
print(date1.isoformat())

text2 = datetime.now()

print(text2 - date)
print(text2 - date1)
print(text2 - date1 > text2 - date)
print(text2 - date1 < text2 - date)