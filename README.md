# EyeBank
An ATM for the visually impaired. This was the project my team and I submitted to Bitcamp 2019 Hackathon. We won the category "Best Financial Hack" which was sponsored by Capital One.

![atm](https://user-images.githubusercontent.com/10646691/60050055-b0b20780-969d-11e9-869d-9bf49bc80d18.jpg)

# How we built it
This ATM was created so that anyone with visual impairment could use an ATM at any time. This is to help those with such disabilities financial independence. We used a variety of technologies including Tensorflow, Python's Text-To-Speech and Speech-To-Text libraries, Capital One API, and Raspberry Pi.

### Python Object Detection 
First, we implemented the facial recognition for the ATM using Machine Learning. We added this feature so that a visually impaired individual could let the ATM detect their unique face so they could access their account. We built the facial recognition with a framework called Darkflow, which is a realtime object detection framework that is built on top of Tensorflow. We trained the model on a set of images of one person who would be a capital one client for demonstration purposes. With this implented, we could allow user authentication by using facial recognition for the ATM.

### Python's Text-To-Speech and Speech-To-Text
We initially setup Lambda on AWS to setup an Alexa skill to go with our project, but there were a lot of limitations to alexa that hindered our project, so we decided to switch to using Python's built-in Text to Speech and Speech to Text (pyttsx). This was a main part of the final product because speaking and listening was the main way to interact with the system. So by using this, we were able to allow users to access their account details by only speaking. We had to integrate the Capital One API with our script so that the user could access their specific capital one bank account and perform banking operations by just speaking.

### Raspberry Pi
And to top off the project, we connected a Raspberry Pi to our system and implemented this part into the script so that when a user would ask to withdraw money, the ATM would dispensene cash using the Servo Motor which was connected to the Raspberry Pi. 

[Check out the project on Devpost](https://devpost.com/software/eyebank)
