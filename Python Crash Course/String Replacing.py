# Replaces the end of a sentence if it matches the old substring
def replace_ending(sentence, old, new):
    if sentence.endswith(old):  # Check if sentence ends with 'old'
        # Replace the end with 'new'
        return sentence[:-len(old)] + new
    return sentence  # Return original if no match

print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# It's raining cats and dogs
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# She sells seashells by the seashore
print(replace_ending("The weather is nice in May", "may", "april"))
# The weather is nice in May
print(replace_ending("The weather is nice in May", "May", "April"))
# The weather is nice in April