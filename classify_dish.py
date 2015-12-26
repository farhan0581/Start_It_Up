from __future__ import division
import csv


veg_list=['veg','vegetarian','aloo','paneer','subzi','gobhi','beans','matar','daal','baingan','bhaji','coffee']
nonveg_list=['chicken','murg','pork','gosht','lamb','beef','fish','mutton','machi','ham']

file_handle=open('dish_upload_17122015_v1.csv','rt')
reader=csv.DictReader(file_handle)

results={}

# for line in reader:
# 	results[line['dish_name']]=""
# file_handle.seek(0,0)
# reader=csv.DictReader(file_handle)

for line in reader:
	var_dish=line['dish_name'].lower()
	v=0.0
	nv=0.0
	for i in range(len(nonveg_list)):
		if nonveg_list[i] in var_dish:
			# results[line['dish_name']]="Non-Veg"
			nv=1
		# elif nonveg_list[i] not in (line['dish_name']).lower() and results[line['dish_name']]=="":
		# 	results[line['dish_name']]=""
	for i in range(len(veg_list)):
		if veg_list[i] in var_dish:
			v=v+1
	len_dish=len(var_dish.split(" "))
	results[var_dish]=[v/len_dish,nv]


print results

# prob=[]

# file_handle.seek(0,0)
# reader=csv.DictReader(file_handle)

# for line in reader:
# 	words=(line['dish_name']).lower().split(" ")
# 	for i in range(len(words)):
# 		for j in range(len(nonveg_list)):
# 			if nonveg_list[j] in words[i]:



# strin="Veg Butter Tadka Pav Bhaji"
# res=strin.split(" ")
# print len(res)
