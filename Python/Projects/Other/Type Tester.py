##Type speed tester
import time
import Levenshtein
import keyboard

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            break  # finishing the loop
    except:
        break  # if user pressed a key other than the given key the loop will break
            
##from essential_generators import DocumentGenerator
##gen = DocumentGenerator()
##
##sentence = gen.sentence()
##
##
##word_list = sentence.split()
##
##number_of_words = len(word_list)
##
##print("NUMBER OF WORDS", number_of_words)
##
##
##
##
##
##def write():
##    print("")
##    print(sentence)
##    print("")
##    print("")
##    
##    tic = time.perf_counter()
##    sentence_typed = str(input("Type Here    "))
##    toc = time.perf_counter()
##    time_total = (toc - tic)
##
##    time_total = float(round(time_total, 2))
##
##    wpm = 60/(time_total/number_of_words)
##
##    wpm = float(round(wpm, 2))
##    
##    print("------------------------------------------------------------------------")
##    print("")
##    print("Time:", time_total)
##    print("")
##    print("Words per Minute:", wpm)
##    print("")
##    print("Levenshtein Accuracy = ", Levenshtein.distance( sentence, sentence_typed))
##        
##        
##
##
##ready = input("Press Enter when your ready and start typing as soon as you see the sentence")
##
##
##write()
