# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
#Here, despite G.B. Shaw's quote, our characters have started with       
##different amounts of apples so we can better observe the results. 
#We're going to have Martin and Johanna exchange ALL their apples with one another.
        temp = you.apples
        you.apples = me.apples
        me.apples = temp
        return you.apples, me.apples
    
def exchange_ideas(you, me):
    sum = you.ideas + me.ideas
    you.ideas = sum
    me.ideas = sum
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))



