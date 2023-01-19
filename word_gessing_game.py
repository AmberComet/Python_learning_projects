from random import randint

def main():
    word_list=[]
    words_file=open("python_test\\words_alpha.txt","r")

    for x in words_file:
        word_list.append(x)

    words_file.close()
    word = word_list[randint(0,len(word_list))]
    word= word.replace("\n","")

    user_answer = generate_empty_user_answer(word)
    char_list = generate_answer_list(word)

    #print(word)
    win=False
    while user_answer != char_list:
        
        try:
            char_indexes=[]
            guess_char=input("enter a charicter type ""exit"" to exit\n")

            if guess_char.casefold()!="exit":
                guess_char = guess_char[0] #this pulls the first char of the userinput and uses it as the guess

        
                if char_list.count(guess_char) != 0 and user_answer.count(guess_char)==0:
                    char_indexes=find_char_index(char_list,guess_char)

                    for i in char_indexes:
                        user_answer[i]=guess_char

                elif char_list.count(guess_char) == 0 and user_answer.count(guess_char)==0:
                    print("the word doent contain: ",guess_char)
            
                else:
                    print("you already have guessed: ",guess_char)

            elif guess_char.casefold()=="exit":
                break
        except:
                print("invalid input")

        print(user_answer)

    if user_answer==char_list:
        win=True
    
    if win:
        print("you win the word was",word)
    else:
        print("you have exited the game")
    

def generate_answer_list(answer):
    answer_char=[]
    for c in answer:
        answer_char.append(c)
    return answer_char

def generate_empty_user_answer(answer):
    user_answer=[]
    for c in answer:
        user_answer.append('_')
    return user_answer

def find_char_index(char_array,compair_char):
    indexes=[]
    i=0
    for c in char_array:
        if c==compair_char:
            indexes.append(i)
        i+=1
        #print(indexes)
    return indexes


main()