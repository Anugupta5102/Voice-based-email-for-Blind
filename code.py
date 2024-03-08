import smtplib
import speech_recognition as sr
from gtts import gTTS
import os

# Function to convert text to speech
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("message.mp3")
    os.system("start message.mp3")

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

# Function to send an email
def send_email(subject, body, to_email):
    # Your email credentials
    sender_email = "anushreegupta@gmail.com"
    sender_password = "anushreeee12"

    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Create the email message
    message = f"Subject: {subject}\n\n{body}"

    # Send the email
    server.sendmail(sender_email, to_email, message)

    # Close the SMTP server
    server.quit()

# Main function
def main():
    # Ask the user for the recipient's email address
    speak("Please say the recipient's email address.")
    recipient_email = recognize_speech()
    
    if recipient_email:
        # Ask the user for the email subject
        speak("Please say the email subject.")
        subject = recognize_speech()

        # Ask the user for the email body
        speak("Please say the email body.")
        body = recognize_speech()

        # Send the email
        if subject and body:
            send_email(subject, body, recipient_email)
            speak("Email sent successfully.")
        else:
            speak("Email not sent. Please provide a subject and body.")

if __name__ == "__main__":
    main()
