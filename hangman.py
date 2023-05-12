import random
from words import word_list
from hangman_art import logo
from hangman_art import stages
#word_list=['toyota','honda','international','brazil','korea']

lives = 6
selected_word=random.choice(word_list)
print(logo)
# print(selected_word +"\n")


empty_list=[]
for _ in selected_word:
    empty_list +='_'
print(empty_list)


#check_blank()




end=False

while end == False:
    #check_blanks()       
    guess=input('guess any letter : ')
    
#print(empty_list)

    for position in range (len(selected_word)):
        letter=selected_word[position]
        
        if letter==guess:
            empty_list[position]=letter
    print(empty_list)
    
   
    
    if '_' not in empty_list:
        end = True
        print('you win')
    
    if guess not in selected_word:
        lives -=  1
        
        print(stages[lives])
        if lives == 0:
            end = True
            print("GAME OVER")
        
    
        print(lives)   