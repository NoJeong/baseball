import re, usercsv

English = 'she is a vegetarian. She dois not eat meat. She thinks that anials should not be killed. It is hard for her to hang out with people. Many people like to eat meat. She told gis parents not to have meat. They laughed at her. She realized they could\'t give up meat.'
Korean = '그녀는 채식주의자입니다. 그녀는 고기를 먹지 않습니다. 그녀는 동물을 죽이지 말아야한다고 생각합니다. 그녀가 사람들과 어울리는 것은 어렵습니다. 많은 사람들이 고기를 좋아합니다. 그녀는 부모에게 고기를 먹지 말라고 말했습니다. 그들은 그녀를 비웃었다. 그녀는 그들이 고기를 포기할 수 없다는 것을 꺠달았습니다.'

korean_list = re.split('\.',Korean)
english_list = re.split('\.',English)

# print(korean_list)

total = []

for i in range(len(english_list)):
    total.append([english_list[i],korean_list[i]])
usercsv.writecsv('korean_english.csv',total)