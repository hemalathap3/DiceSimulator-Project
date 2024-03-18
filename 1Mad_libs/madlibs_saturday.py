# Step 1: get_input function defining
def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}:")
    return user_input

# Step 2: Getting Values
name1 = get_input("name")
verb1 = get_input('verb1')
name2 = get_input('name2')
verb2 = get_input('verb2')

# Step 3: Adding the conversation
story = f"""
Once upon a time, there was a{name1} who loved to {verb1} all day
One day, {name2} walked into the room and caught the {name1} in the act.

{name2}: Hello {name1}, How are you?
{name1}: I'm fine, thankyou. what about you?
{name2}: I'm good but I am worried about my final examination.
{name1}: It is very common.You are serious about your studies.so you are worried.
{name2}: I know ,But I am really afraid because I have no good preparation for math.
         I am very much tensed about that subject.
{name1}: Oh, sorry to know.But I think you should do more practice. 
{name2}: Yeah, I think so can you help me a bit about this?
         I think I can overcome this problem.if you help me.
{name1}: Why not? I will help you. You just make some time.
         and come to my house.
{name2}: Yes,you are right.Thankyou so much {name1}. I hope you will do better in the 
         examination.
         
And so, {name2}  and the {name1} went off to {verb2} and had a great time.
The end.
"""    

# Step 3: print(story)
print(story)

