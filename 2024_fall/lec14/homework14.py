import datetime, gtts, bs4, random, speech_recognition

def what_time_is_it(lang, filename):
    '''
    Tell me what time it is.
    
    Parameters:
    lang (str) - language in which to speak
    filename (str) - the filename into which the audio should be recorded
    '''
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M")
    tts = gtts.gTTS(f'The time is {time_str}.', lang=lang)
    tts.save(filename)

    
def tell_me_a_joke(lang, audiofile):
    '''
    Tell me a joke.
    
    @params:
    filename (str) - filename containing the database of jokes
    lang (str) - language
    audiofile (str) - audiofile in which to record the joke
    '''
    joke = random.choice(jokes.get(lang, jokes["en"]))
    tts = gtts.gTTS(joke, lang=lang)
    tts.save(audiofile)


def what_day_is_it(lang, audiofile):
    '''
    Tell me what day it is.

    @params:
    lang (str) - language in which to record the date
    audiofile (str) - filename in which to read the date
    
    @returns:
    url (str) - URL that you can look up in order to see the calendar for this month and year
    '''
    today = datetime.datetime.now()
    day_str = today.strftime("%A, %B %d, %Y")
    tts = gtts.gTTS(f'Today is {day_str}.', lang=lang)
    tts.save(audiofile)


def personal_assistant(lang, filename):
    '''
    Listen to the user, and respond to one of three types of requests:
    What time is it?
    What day is it?
    Tell me a joke!
    
    @params:
    lang (str) - language
    filename (str) - filename in which to store the result
    '''
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your request...")
        audio = recognizer.listen(source)

    try:
        user_request = recognizer.recognize_google(audio, language=lang).lower()
        print(f"You said: {user_request}")

        if "time" in user_request:
            what_time_is_it(lang, filename)
        elif "day" in user_request:
            what_day_is_it(lang, filename)
        elif "joke" in user_request:
            tell_me_a_joke(lang, filename)
        else:
            print("Sorry, I didn't understand that.")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
