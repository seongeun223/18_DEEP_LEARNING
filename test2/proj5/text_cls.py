# step1 : import modules
from transformers import pipeline

# step2 : create inference object
classifier = pipeline("sentiment-analysis", model="stevhliu/my_awesome_model")

# stpe3 : prepare data
text = "This was a masterpiece. Not completely faithful to the books, but enthralling from beginning to end. Might be my favorite of the three."

# step4 : inference
result = classifier(text)

# step5 : post processing
print(result)