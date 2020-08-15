'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if word[len(word)-1: len(word)].isdigit():
        count = int(word[len(word)-1:len(word)])
        print(f'count in str line 9: {count}')
    else:
        count = 0

    index = word.find("th")
    print(f'line 16 index of earlist th: {index}')
    if index!= -1:
        count += 1
        print(f'word on line 19: {word}')
        new_word = word[index:len(word) - count] + str(count)
        new_word = new_word[2:]
        print(f'new word on line 21: {new_word}')
        print(f'count one line 22: {count}')
        return count_th(new_word)

    print(f'count line 25: {count}')
    return count


print(count_th('ThasbBThthththhhth'))
