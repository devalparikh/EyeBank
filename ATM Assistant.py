import random
import time
import cv2
import sys
import speech_recognition as sr
import win32com.client as wincl
import requests
import json
import re
import os
from word2number import w2n
import subprocess
import winsound
frequency = 1500  # Set Frequency To 2500 Hertz
duration = 800  # Set Duration To 1000 ms == 1 second
#Speak is assigned Windows 10 TTS voice through creation of speak object
speak = wincl.Dispatch("SAPI.SpVoice")

#This line will call the detection model
# os.system("python flow --model cfg/test.cfg --load 155 --demo camera")
#End of important line
#subprocess.call(["./darkflow/flow.py", "--model", "cfggundet.cfg", "--load", "-1", "--demo", "camera"])
#python flow --model cfg/gundet.cfg --load -1 --demo camera
#sys.argv = ['--model' ,'cfg/gundetection.cfg', '--load' , '-1', '--demo', 'camera']
#exec( open("./darkflow/flow").read() )


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":
    # set the list of words, maxnumber of guesses, and prompt limit
    WORDS = ["deposit", "withdraw"]
    NUM_GUESSES = 3
    PROMPT_LIMIT = 5

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    #device_index = 3 is microphone for my laptop
    microphone = sr.Microphone(device_index = 3)

    # get a random word from the list
    word = random.choice(WORDS)

    # format the instructions string
    speak.speak("Welcome to your Capital One assistant.")
    # time.sleep(2)
    # speak.speak("Would you like to deposit, or withdraw?")
    withdraw = False
    deposit = False
    leave = False
    # while leave == False:
    #         #speak.speak('Guess {}. Speak!'.format(i+1))
    #         #print('Guess {}. Speak!'.format(i+1))
    #         guess = recognize_speech_from_mic(recognizer, microphone)
    #         if guess["transcription"]:
    #             print("Found transcription")
    #         if not guess["success"]:
    #             speak.speak("I didn't catch that. What did you say?")
    #         #formatting response to string
    #         theResponse = "{}".format(guess["transcription"])
    #         if("deposit" in theResponse and "withdraw" not in theResponse):
    #             print("Found deposit in string")
    #             deposit = True
    #             speak.speak("You mentioned depositting")
    #             break
    #         elif("withdraw" in theResponse and "deposit" not in theResponse):
    #             withdraw = True
    #             print("Found withdraw in string")
    #             speak.speak("You mentioned withdrawing")
    #             break
    #         else:
    #             speak.speak("You have selected to do " + theResponse + ". Would you like to deposit, or withdraw?")


        # load the required trained XML classifiers 
    # https://github.com/Itseez/opencv/blob/master/ 
    # data/haarcascades/haarcascade_frontalface_default.xml 
    # Trained XML classifiers describes some features of some 
    # object we want to detect a cascade function is trained 
    # from a lot of positive(faces) and negative(non-faces) 
    # images. 

    #This will whole block of code will initiate the facial detection
    speak.speak("Please stand in front of the camera to scan your face and access your account.")
    os.system("python flow --model cfg/test.cfg --load 155 --demo camera")
    # detection = 0
    # face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
      
    # # https://github.com/Itseez/opencv/blob/master 
    # # /data/haarcascades/haarcascade_eye.xml 
    # # Trained XML file for detecting eyes 
    # eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')  
      
    # # capture frames from a camera 
    # cap = cv2.VideoCapture(0) 
      
    # # loop runs if capturing has been initialized. 
    # while 1:  
      
    #     # reads frames from a camera 
    #     ret, img = cap.read()  
      
    #     # convert to gray scale of each frames 
    #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
      
    #     # Detects faces of different sizes in the input image 
    #     faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
      
    #     for (x,y,w,h) in faces: 
    #         # To draw a rectangle in a face  
    #         cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)  
    #         roi_gray = gray[y:y+h, x:x+w] 
    #         roi_color = img[y:y+h, x:x+w] 
    #         print("Detected")
    #         detection += 1
    #         # Detects eyes of different sizes in the input image 
    #         #eyes = face_cascade.detectMultiScale(roi_gray)  
      
    #         #To draw a rectangle in eyes 
    #         # for (ex,ey,ew,eh) in eyes: 
    #         #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2) 
      
    #     # Display an image in a window 
    #     cv2.imshow('img',img) 
      
    #     # Wait for Esc key to stop 
    #     k = cv2.waitKey(30) & 0xff
    #     if k == 27 or detection == 30: 
    #         break
    # # Close the window 
    # cap.release()
    # # De-allocate any associated memory usage 
    # cv2.destroyAllWindows()  
    #End of facial detection

    #Beggining to access user profile and information
    customerID ='5cb153a0322fa06b67794b52'
    apiKey = '89d6a84dc6823dc1173a7a301fdf19b6' 
    url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerID,apiKey)
    theAccount = requests.get(url)
    Account = theAccount.json()

    print(Account[1]["balance"])
    speak.speak("You are accessing " + Account[1]["nickname"]) 
    theBalance = Account[1]["balance"]
    price = str((Account[1]["balance"])) 
    #theBalance = Account[1]["balance"]
    speak.speak("Your current balance is: " + price + " dollars")
    quit = False
    while quit == False:
        speak.speak("Would you like to deposit, or withdraw?")
        while leave == False:
                    #speak.speak('Guess {}. Speak!'.format(i+1))
                    #print('Guess {}. Speak!'.format(i+1))
                    guess = recognize_speech_from_mic(recognizer, microphone)
                    if guess["transcription"]:
                        print("Found transcription")
                    if not guess["success"]:
                        speak.speak("I didn't catch that. What did you say?")
                    #formatting response to string
                    theResponse = "{}".format(guess["transcription"])
                    if("deposit" in theResponse and "withdraw" not in theResponse):
                        print("Found deposit in string")
                        deposit = True
                        speak.speak("You mentioned depositting")
                        break
                    elif("withdraw" in theResponse and "deposit" not in theResponse):
                        withdraw = True
                        print("Found withdraw in string")
                        speak.speak("You mentioned withdrawing")
                        break
                    else:
                        speak.speak("You have selected to " + theResponse + ". Would you like to deposit, or withdraw?")

        if(deposit == True):
            speak.speak("How much would you like to deposit?")
            while leave == False:
                #speak.speak('Guess {}. Speak!'.format(i+1))
                #print('Guess {}. Speak!'.format(i+1))
                guess = recognize_speech_from_mic(recognizer, microphone)
                if guess["transcription"]:
                    print("Found transcription")
                if not guess["success"]:
                    speak.speak("I didn't catch that. What did you say?")
                    continue
                #formatting response to string
                theResponse = "{}".format(guess["transcription"])
                theResponse = re.sub('[$,]','', theResponse)
                arr = [int(s) for s in theResponse.split() if s.isdigit()]
                print(arr)
                # theResponse = arr[0]
                if guess["success"] and theResponse != None:
                    print(theResponse)
                    if("$" in theResponse):
                        theResponse = theResponse[1:len(theResponse)]
                        print(theResponse)
                    try:
                        #amount = w2n.word_to_num(theResponse)
                        amount = arr[0]
                    except:
                        speak.speak("Please say a valid number. How much would you like to deposit?")
                        continue
                    if(amount > 0):
                        print("Depositing money")
                        speak.speak("You would like to deposit " + str(arr[0]) + " dollars")
                        theBalance = theBalance + amount
                        price = str(theBalance) 
                        speak.speak("Your current balance is now " + price)
                        deposit = False
                        break

        elif(withdraw == True):
            speak.speak("How much would you like to withdraw?")
            while leave == False:
                #speak.speak('Guess {}. Speak!'.format(i+1))
                #print('Guess {}. Speak!'.format(i+1))
                guess = recognize_speech_from_mic(recognizer, microphone)
                if guess["transcription"]:
                    print("Found transcription")
                if not guess["success"]:
                    speak.speak("I didn't catch that. What did you say?")
                    continue
                #formatting response to string
                theResponse = "{}".format(guess["transcription"])
                theResponse = re.sub('[$,]','', theResponse)
                arr = [int(s) for s in theResponse.split() if s.isdigit()]
                print(arr)
                if guess["success"] and theResponse != None:
                    print(theResponse)
                    if("$" in theResponse):
                        theResponse = theResponse[1:len(theResponse)]
                        print(theResponse)
                    try:
                        #amount = w2n.word_to_num(theResponse)
                        amount = arr[0]
                    except:
                        speak.speak("Please say a valid number. How much would you like to withdraw?")
                        continue
                    if(amount > 0):
                        print("Withdrawing money")
                        speak.speak("You would like to withdraw  " + str(arr[0]) + " dollars")
                        speak.speak("After the beep, please enter your bank pin to withdraw any money from the key in front of you.")
                        time.sleep(2)
                        winsound.Beep(frequency, duration)
                        # ret = subprocess.call(["ssh", "pi@172.20.10.5", "python3 /home/pi/Desktop/serv.py"]);
                        theBalance = theBalance - amount
                        price = str(theBalance) 
                        speak.speak("Your current balance is now " + price)
                        withdraw = False
                        break
        speak.speak("If there is anything else you would like to do, reply with yes or no.")
        while leave == False:
                #speak.speak('Guess {}. Speak!'.format(i+1))
                #print('Guess {}. Speak!'.format(i+1))
                guess = recognize_speech_from_mic(recognizer, microphone)
                if guess["transcription"]:
                    print("Found transcription")
                    theResponse = "{}".format(guess["transcription"])
                if not guess["success"]:
                    speak.speak("I didn't catch that. What did you say?")
                    continue
                if("yes" in theResponse):
                    break
                elif("no" in theResponse):
                    quit = True
                    break
                else:
                    speak.speak("Say yes or no.")

    speak.speak("Thank you for using Capital One Services. Have a nice day.")



    # cascPath = "./haarcascade_frontalface_default"
    # faceCascade = cv2.CascadeClassifier(cascPath)

    # video_capture = cv2.VideoCapture(0)

    # while True:
    #     # Capture frame-by-frame
    #     ret, frame = video_capture.read()

    #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #     faces = faceCascade.detectMultiScale(
    #         gray,
    #         scaleFactor=1.1,
    #         minNeighbors=5,
    #         minSize=(30, 30),
    #         flags = cv2.CASCADE_SCALE_IMAGE
    #     )

    #     # Draw a rectangle around the faces
    #     for (x, y, w, h) in faces:
    #         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #     # Display the resulting frame
    #     cv2.imshow('Video', frame)

    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break

    # # When everything is done, release the capture
    # video_capture.release()
    # cv2.destroyAllWindows()
    # instructions = (
    #     "I'm thinking of one of these words:\n"
    #     "{words}\n"
    #     "You have {n} tries to guess which one.\n"
    # ).format(words=', '.join(WORDS), n=NUM_GUESSES)

    #Added a sample of test instructions
    #speak.speak(instructions)

    # show instructions and wait 3 seconds before starting the game
    #print(instructions)
    #time.sleep(3)

    # for i in range(NUM_GUESSES):
        # get the guess from the user
        # if a transcription is returned, break out of the loop and
        #     continue
        # if no transcription returned and API request failed, break
        #     loop and continue
        # if API request succeeded but no transcription was returned,
        #     re-prompt the user to say their guess again. Do this up
        #     to PROMPT_LIMIT times
        # for j in range(PROMPT_LIMIT):
        #     speak.speak('Guess {}. Speak!'.format(i+1))
        #     print('Guess {}. Speak!'.format(i+1))
        #     guess = recognize_speech_from_mic(recognizer, microphone)
        #     if guess["transcription"]:
        #         break
        #     if not guess["success"]:
        #         break
        #         speak.speak("I didn't catch that. What did you say?")
        #     print("I didn't catch that. What did you say?\n")

        # if there was an error, stop the game
        # if guess["error"]:
        #     print("ERROR: {}".format(guess["error"]))
        #     break

        # show the user the transcription
        # speak.speak("You said: {}".format(guess["transcription"]))
        # print("You said: {}".format(guess["transcription"]))

        # determine if guess is correct and if any attempts remain
        # guess_is_correct = guess["transcription"].lower() == word.lower()
        # user_has_more_attempts = i < NUM_GUESSES - 1

        # determine if the user has won the game
        # if not, repeat the loop if user has more attempts
        # if no attempts left, the user loses the game
        # if guess_is_correct:
        #     speak.speak("Correct! You win!".format(word))
        #     print("Correct! You win!".format(word))
        #     break
        # elif user_has_more_attempts:
        #     speak.speak("Incorrect. Try again.")
        #     print("Incorrect. Try again.\n")
        # else:
        #     speak.speak("Sorry, you lose!\nI was thinking of '{}'.".format(word))
        #     print("Sorry, you lose!\nI was thinking of '{}'.".format(word))
        #     break