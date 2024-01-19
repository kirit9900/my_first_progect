welcome_message = "Hello"


# "send_to" - id пользователя, которому участник должен сделать подарок
def shuffle_users(user_data):
    import random
    user_ids=list(user_data.keys())
    shuffled=user_ids[::]
    random.shuffle(user_ids)
    while any(filter(lambda x: x[0]==x[1],zip(user_ids,shuffled))):
        random.shuffle(shuffled)
    for i,user in enumerate(shuffled):
        user_data[user]["sent to"]=shuffled[(i+1)%len(shuffled)]
    return user_data
