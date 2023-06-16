# a function that turns text into pig latin: a simple text transformation that 
# modifies each word moving the first character to the end
# and appending "ay" to the end. For example, python ends up as ythonpay.
def pig_latin(text):
    say = ''
    words = text.split()
    for word in words:
        pig_latin_sentence = word[1:] + word[0] + 'ay'+ ' '
        say += pig_latin_sentence
    return say
print(pig_latin('hello sweetie how are you'))
