#testing.py
fortune = [
    'Be a generous friend and a fair enemy.',
    '傷心有多少 在乎就有多少',
    'A bargain is something you don\'t need at a price you can\'t resist.',
    'A single conversation with a wise man is better than ten years of study.',
    'All the water in the world can\'t sink a ship unless it gets inside.',
    'Ask a friend to join you on your next voyage.',
    'Back away from individuals who are impulsive.',
    'Bad luck and misfortune will follow you all your days.',
    'Be a good friend and a fair enemy.',
    'Bread today is better than cake tomorrow.',
    'Circumstance does not make the man; it reveals him to himself.',
    'Cookie says, "You crack me up."',
    'Do not be covered in sadness or be fooled in happiness;  they both must exist.',
    'Do not fear what you don\'t know.',
    'Do not follow where the path may lead. Go where there is no path...and leave a trail.'
]

def numberChooser(list):
    a = random.randint(0,len(list))
    print(list[a])

numberChooser(exampleList)
