
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)  

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def generate_chat_message(prompt):


    completion = openai.ChatCompletion.create(
    model="gpt-4",
    # model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ],
    max_tokens = 256,


    )
    answer1 = completion.choices[0].message["content"]
    print('answer1:')
    print(answer1)
    # exit()
############################################################################
    completion = openai.ChatCompletion.create(
    model="gpt-4",
    # model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": answer1},
        {"role": "user", "content": string2}
    ],
    max_tokens = 256,
    # temperature = 0.8

    )
    answer2 = completion.choices[0].message["content"]
    print('answer2:')
    print(answer2)
    # exit()
############################################################################
    completion = openai.ChatCompletion.create(
    model="gpt-4",
    # model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": answer1},
        {"role": "user", "content": string2},
        {"role": "assistant", "content": answer2},
        {"role": "user", "content": string3}
    ],
    max_tokens = 256,
    # temperature = 0.8

    )
    answer3 = completion.choices[0].message["content"]
    print('answer3:')
    print(answer3)
    # exit()
############################################################################
    completion = openai.ChatCompletion.create(
    model="gpt-4",
    # model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": answer1},
        {"role": "user", "content": string2},
        {"role": "assistant", "content": answer2},
        {"role": "user", "content": string3},
        {"role": "assistant", "content": answer3},
        {"role": "user", "content": string4}
    ],
    max_tokens = 256,
    # temperature = 0.8

    )
    answer4 = completion.choices[0].message["content"]
    print('answer4:')
    print(answer4)
    # exit()

    return answer4


