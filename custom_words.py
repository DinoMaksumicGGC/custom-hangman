import random

answer_directory = {
'Ella#197171': {'player':'Class', 'theme':'hacking a password', 'hint':'Numbers'}

}
keys = list(answer_directory.keys())
random.shuffle(keys)
shuffled_answers = dict([(key, answer_directory[key]) for key in keys])
