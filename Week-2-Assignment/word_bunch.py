
def load_stop_words(filename):
    with open(filename, 'rt') as stopwords:
        return [line.strip().replace("'", "") for line in stopwords]

def show_top_ten(final_tally):
    key_words = final_tally.keys()
    word_ladder = sorted(key_words, key=final_tally.__getitem__)
    for i in range(10):
        num_words = len(word_ladder) - 1
        top_word = word_ladder[num_words - i]
        print(i+1, top_word, ':', final_tally[top_word])

def main():
    print('The Top 10 most common words:')
    file_stop_words = './stopwords'
    file_to_process = './98-0.txt'
    stop_words = load_stop_words(file_stop_words)
    tally_board = {}
    with open(file_to_process, 'rt') as full_text:
        # process each line of text in the file
        for line in full_text:
            import re
            # remove all unwanted characters in the line
            process_line = re.sub('(\W+)', ' ', line)
            process_line = process_line.strip().lower()
            # split the line using the space as the delimiter
            words = process_line.split(' ')
            for w in words:
                if w in stop_words or len(w) <= 1:
                    continue
                if not tally_board.get(w):
                    tally_board[w] = 1
                else:
                    tally_board[w] += 1
        show_top_ten(tally_board)

if __name__ == '__main__':
    main()
