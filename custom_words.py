import random

answer_directory = {
'Ella#197171': {'player':'Class', 'theme':'hacking lindas facebook password', 'hint':'Numbers and one special character'},

}
keys = list(answer_directory.keys())
random.shuffle(keys)
shuffled_answers = dict([(key, answer_directory[key]) for key in keys])
