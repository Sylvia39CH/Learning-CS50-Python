date = str(input("Input a date, anno Domini, in month-day-year order: ")).replace("-"," ").replace(","," ").replace("."," ")
#把所有分隔符都换成空格

list = date.split(" ")
#用空格划分，形成列表

YYYY = list[2].zfill(4)
MM = list[0].zfill(2)
DD = list[1].zfill(2)
# 如果不足4位数或者2位数，用0补足

month = {
"January":"01",
"February":"02",
"March":"03",
"April":"04",
"May":"05",
"June":"06",
"July":"07",
"August":"08",
"September":"09",
"October":"10",
"November":"11",
"December":"12"
}

if str(MM).title() in month:
    M = month[str(MM).title()]
else:
    M = MM
#对于在第八行中仍然是单词的月份，转化为数字



print(f" YYYY-MM-DD: {YYYY}/{M}/{DD}")
