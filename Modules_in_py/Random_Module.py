import random
value = random.random()
value1 = random.uniform(1,400) #random floating value betwee 1 to 10
print(value1)
val_int =random.randint(0,1)
print(val_int)

# random.choice

greetings = ['Hello' , 'Namaste' , 'Hi', 'Hey' , 'Hola']
values = random.choice(greetings)
print(values + ' JP')

# random .choices 

Col_list = ['Red','Black' ,'Blue']
result = random.choices(Col_list , k= 10) # k = require sequence
result = random.choices(Col_list ,weights=[18,18,4], k= 10) # 18 is the chances of selection
print(result)

# .suffle() Method

deck_card = list(range(1,52))
random.shuffle(deck_card)  # it can select duplicate value
print(deck_card)


# .samle method
hand_card = random.sample(deck_card, k=5) #chooses the unique sample number
print(hand_card)


