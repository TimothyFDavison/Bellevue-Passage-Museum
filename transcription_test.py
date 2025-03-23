from scraibe import Scraibe


model = Scraibe()
text = model.autotranscribe('deshields_interview-short.mp3')
print(text)