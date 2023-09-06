import openai

api_key = "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"

# Prompt for generating lyrics
prompt = """
Create a verse of lyrics based on this rhyme scheme and flow:
This song catchier than chickenpox is
I bet your house is where my other sock is
Woke up this morning, thought I'd write a pop hit
How quickly can you take your clothes off pop quiz?

examples:
I just wanna ride him like a rodeo / But first he gotta grow it like Pinocchio / Sorry Im so vulgar, San Antonio

This crowd is giving me all the endorphins / I wish someone could rearrange my organs / Philly is the city I was born in.

Was gonna throw some shade but that got vetoed / Does anybody have an extra pre-roll / Cause its 4/20, its my f*cking Greek show!

I'm sorry that this outro is chaotic / Don't call your ex Katie they are toxic / Baltimore I think that you're the hottest.

no repeats of the lines above. 1 verse, 4 lines each. make sure the last word of each line rhymes with the last word of the line before it, meaning all 4 lines rhyme with each other.

"""

num_lyrics = 1  

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=500,  # for longer responses if necessary
    n=num_lyrics,
    api_key=api_key
)

# Check if there are any errors in the response
if 'object' in response and response['object'] == 'error':
    print(f"Error: {response['error']['message']}")
else:
    # Print the generated lyrics
    for i, lyric in enumerate(response['choices']):
        print(f"{lyric['text'].strip()}\n")
