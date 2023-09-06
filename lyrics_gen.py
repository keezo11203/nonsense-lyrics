import openai

api_key = "api_key_here"

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

Water aint the only thing I swallow / I really wish I could play here tomorrow / My favorite city is Chicago.

He hit so hard Im walking on a slant-a / This body is in super high demand-a / I hear they like my peaches in Atlanta.

Ive got a personality but no tits / This song isnt about Joshua Bassett / Los Angeles, your energy is big dick

His ex is a motel, Im a villa / He says I taste better than vanilla / Whats your favorite city? Mines Manila.

Look at all those presents, that's a big sack / Boy, that package is too big to gift wrap / Woke up this morning, thought I'd write a 'Chrismash' / How quickly can you build a snowman? Think fast

Come over tonight my room is spotless/ Im sorry this outro is so chaotic/ Atlanta, its official: Youre the hottest.

This song harder than keeping a secret / He said my head's crazy, I'm a genius / What's better than one pop star? It's two, bitch / It's Coi Leray and Brina on the remix

felt so good he made me hit the top note / eras tickets girl you won the lotto / mexico I kinda think te amo

no repeats of the lines above. 1 verse, 4 lines each. the last word of all 4 lines have to rhyme with each other.
make sure this happens for all 4 lines. some lines being given are not all rhyming
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
