import pyttsx3

def confession(boy, girl):
    story = f"""
One evening, under the quiet sky, {boy} looked into {girl}’s eyes and said:

"{girl}, from the moment I met you, my world changed.
Your smile makes my days brighter, and your presence makes me stronger.
I tried to hide it, but I can’t anymore…
I am in love with you."

{girl} felt her heart racing. With a soft smile, she replied:

"{boy}, I have been waiting to hear this from you.
Every moment with you feels special, and I can’t imagine my life without you.
Yes, I love you too."

From that day, {boy} and {girl} walked forward together —
two hearts, one soul, bound by love forever.
"""
    print(story)
    engine = pyttsx3.init()
    engine.say(story)
    engine.runAndWait()


boy = input("Enter the boy's name: ")
girl = input("Enter the girl's name: ")

confession(boy, girl)
