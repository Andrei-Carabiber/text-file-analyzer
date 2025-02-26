import os

running = True


def count_words(file: str):
    file.replace('\n', ' ')
    return len(file.split())

file_name = os.listdir('put-file-here')[0]
with open(f'put-file-here/{file_name}', 'r') as f:
    file_content = f.read()

def remove_punct(file: str):
    punctuation_marks = ['.', ',', '?', '!', ':', ';', "'", '"', '(', ')', '[', ']', '{', '}', '...', '-', '–', '/',
                         '\\', '&', '@', '$', '%', '^', '~', '<', '>', '=', '|', '_', '+', '*', '#', '`']
    trans_table = str.maketrans('', '', ''.join(punctuation_marks))
    file = file.translate(trans_table)
    return file


while running:
    print("""
    Please select an option:
    [1] Show number of words
    [2] Remove punctuation
    [3] Make text lowercase
    [4] Make text uppercase
    [5] Show most common words
    [6] Reset file
    [7] Exit
    """)
    valid = False

    while not valid:  # Get Option
        option = input("Please select an option: ")
        try:
            option = int(option)
            if 0 < option < 7:
                valid = True
            else:
                print("Invalid Choice")
        except TypeError:
            print("Invalid Choice")

    if option == 7:  # exit
        running = False
        print("Bye")
        continue

    if option == 1:  # print nr count
        print(count_words(file_content))

    if option == 2:  # remove punctuation
        with open(f'output/{file_name}', 'w') as f:
            f.write(remove_punct(file_content))
            file_content = remove_punct(file_content)

        print("Done!")
        print("Check the output folder for the result!")

    if option == 3:  # make text lowercase
        with open(f'output/{file_name}', 'w') as f:
            f.write(file_content.lower())
            file_content = file_content.lower()

        print("Done!")
        print("Check the output folder for the result!")

    if option == 4:  # make text uppercase
        with open(f'output/{file_name}', 'w') as f:
            f.write(file_content.upper())
            file_content = file_content.upper()

        print("Done!")
        print("Check the output folder for the result!")

    if option == 5:
        #  FORMAT TEXT
        with open(f'put-file-here/{file_name}', 'r') as f:
            file1 = f.read()
        file1 = remove_punct(file1).lower().replace('\n', ' ')
        words = file1.split(' ')

        # MAKE A DICTIONARY
        freq_counter = {}
        for word in words:
            if word in freq_counter:
                freq_counter[word] += 1
            else:
                freq_counter[word] = 1
        freq_sorted = sorted(freq_counter.items(),key=lambda x: x[1],reverse=True)

        valid = False

        while not valid:  # Get Option
            show_x_words = input("Show frequency for how many words? ")
            try:
                show_x_words = int(show_x_words)
                valid = True
            except TypeError:
                print("Must be an integer")

        print(freq_sorted[:show_x_words])


    if option == 6:
        file_name = os.listdir('put-file-here')[0]
        with open(f'put-file-here/{file_name}', 'r') as f:
            file_content = f.read()

        with open(f'output/{file_name}', 'w') as f:
            f.write(file_content)
