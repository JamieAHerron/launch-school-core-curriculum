# Madlibs is a simple game where you create a story template with "blanks" for words. You, or another player, then construct a list of words and place them into the story, creating an often silly or funny story as a result.

# Create a simple madlib program that prompts for a noun, a verb, an adverb, and an adjective, and injects them into a story that you create.

# Enter a noun: dog
# Enter a verb: walk
# Enter an adjective: blue
# Enter an adverb: quickly

# Do you walk your blue dog quickly? That's hilarious!
# The blue dog walks quickly over the lazy dog.
# The dog quickly walks up to Joe's blue turtle.

def get_correct_input(prompt):
    while True:
        value = input(prompt + '\n')
        if value.strip() == '':
            print('Please enter the correct input')
        elif not value.isalpha():
            print('Please enter alphabetic characters')
        else:
            return value



noun = get_correct_input('Enter a noun:')
verb = get_correct_input('Enter a verb:')
adjective = get_correct_input('Enter a adjective:')
adverb = get_correct_input('Enter a adverb:')

print(f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious! The {adjective} {noun} {verb}s {adverb} over the lazy dog. The {noun} {adverb} {verb}s up to Joe's {adjective} turtle.")

#LYBL vs EAFP approaches to error checking