import random

def load_words(file_path):
    words = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words.append(line.strip())
    return words

def quiz_user(words):
    quizzed_words = []
    correct_list = []
    incorrect_list = []

    while len(quizzed_words) < len(words):
        word = random.choice(words)
        if word not in quizzed_words:
            print('Translate the following word/phrase to Mandarin Chinese:', word)
            user_input = input('Your answer: ')

            if user_input.lower() == 'q':
                break

            quizzed_words.append(word)

            if user_input.lower() == word.lower():
                print('Correct!\n')
                correct_list.append(word)
            else:
                print(f'Incorrect! The correct translation is: {word}\n')
                incorrect_list.append(word)

    total_words = len(correct_list) + len(incorrect_list)
    if total_words > 0:
        percentage_correct = (len(correct_list) / total_words) * 100
    else:
        percentage_correct = 0

    print(f'Percentage of words/phrases correct: {percentage_correct}%\n')
    return percentage_correct, incorrect_list

def is_learned(scores, incorrects):
    if len(scores) < 3:
        print('You have not successfully learned the material yet.')
        return False

    #all() checks each run(loop). shortened version of checking the score each time
    if all(score > 80 for score in scores):
        increasing_scores = True
        for i in range(len(scores) - 1):
            if scores[i] > scores[i + 1]:
                increasing_scores = False
                break

        if increasing_scores:
            unique_incorrects = []
            for incorrect_list in incorrects:
                for word in incorrect_list:
                    if word not in unique_incorrects:
                        unique_incorrects.append(word)

            repeat_incorrects = []
            for word in unique_incorrects:
                count = 0
                for incorrect_list in incorrects:
                    if word in incorrect_list:
                        count = count + 1
                if count > 1:
                    repeat_incorrects.append(word)

            if len(repeat_incorrects) > 0:
                print('Although you have achieved high scores, it is recommended to study the following words/phrases:')
                for word in repeat_incorrects:
                    print(word)
            else:
                print('Congratulations! You have learned the material.')
            return True

    print('You have not successfully learned the material yet. Keep practicing！')
    return False

def learn_mandarin(file_path):
    words = load_words(file_path)
    if len(words) == 0:
        print('The file is empty or could not be read.')
        return 0, []
    else: 
        return quiz_user(words)

def main():
    file_path = "chinese_words.txt"
    attempts = 0
    scores = []
    incorrects = []

    while True:
        action = input('Do you want to (L)earn/study or (Q)uit\n')

        if action.lower() == 'l':
            print("Chinese keyboard(pinyin - simplified) is needed to do this.\nType your answer in pinyin, press spacebar, then return.")
            score, incorrect_list = learn_mandarin(file_path)
            scores.append(score)
            incorrects.append(incorrect_list)
            attempts + attempts + 1

            if is_learned(scores, incorrects):
                break

        elif action.lower() == 'q':
            break

        else:
            print('Invalid input. Please try again.\n')

if __name__ == '__main__':
    main()

