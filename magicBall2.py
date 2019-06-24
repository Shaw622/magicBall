import random

messages = ['確かにそうだ',
            '間違いなくそうだ',
            'はい',
            '何とも。もう一度やってみて',
            'あとでもう一度聞いてみて',
            '集中してもう一度聞いてみて',
            '私の答えはノーです',
            '見通しはそれ程良くない',
            'とても疑わしい']

print(messages[random.randint(0, len(messages) -1)])
