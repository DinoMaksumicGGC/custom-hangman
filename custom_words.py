import random

answer_directory = {
'Ella#197171': {
        'player': 'Class',
        'theme': 'hacking lindas facebook password',
        'hint': "Linda loves her 2 grandkids (Ella & Mason)\n"
                "Linda is a huge Braves baseball fan\n"
                "Her birthday is July 15, 1971\n"
                "She uses Facebook and checks email\n"
                "but isn't very tech-savvy.\n"
                "Hint: Numbers and one special character are included."
    }

}
keys = list(answer_directory.keys())
random.shuffle(keys)
shuffled_answers = dict([(key, answer_directory[key]) for key in keys])
