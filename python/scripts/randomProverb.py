from random import randint

# source
proverbs = [
    'Pierre qui roule n\'amasse pas mousse',
    'Il ne faut pas vendre la peau de l\'ours avant de l\'avoir tué',
    'Tra il dire e il fare c\'è di mezzo il mare',
    'Ad astra per aspera',
    'Une hirondelle ne fait pas le  printemps'
]

indexMax = len(proverbs) - 1
print(proverbs[randint(0,indexMax)])