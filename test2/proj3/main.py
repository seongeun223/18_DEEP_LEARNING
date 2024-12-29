# step1 : import modules
import easyocr

# step2 : create inference object
reader = easyocr.Reader(['ko', 'en']) # this needs to run only once to load the model into memory

# step3 : load data
data = 'korean.jpg'

# step4 : inference
result = reader.readtext(data)
print(result)

# step5 : post processing
# if dddd == "주민등록등본":
#       ㅇㅇㅇㅇ

