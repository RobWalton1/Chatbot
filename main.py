from fuzzywuzzy import fuzz
from fuzzywuzzy import process
print("Greetings, I am JARVIS, Tony Stark's loyal personal assistant, at your service. It is with the utmost pleasure that I extend my virtual hand to assist you in any way you require. How may I be of aid to you on this fine day?")

filename = "questions.txt"
running = True


def data_read(question, path):
    answerFound = False
    with open(path) as FAQData:
        lines = FAQData.readlines()
        for i in range(len(lines)):
            # Remove leading/trailing whitespaces from the line and store it in the variable 'line'.
            line = lines[i].strip()
            simularity = fuzz.partial_ratio(question, line)
            # Check if the current 'line' matches the 'question'.
            if simularity >= 80:
                answerFound = True
                # Check if the next line exists (i+1 < len(lines)).
                # If it does, it means there is an answer after the matched question.
                if i + 1 < len(lines):
                    # Get the next line, which contains the answer, and remove leading/trailing whitespaces.
                    answer = lines[i + 1].strip()

                    # Print the answer.
                    print("Jarvis:", answer)
                else:
                    # If the next line doesn't exist, there is no answer available for the question.
                    print("Jarvis: Regrettably, the answer is not at my disposal at this moment. My deepest apologies for any inconvenience this may cause.")
                
                # Break out of the loop since we found the answer or determined it is not available.
                break

        # If 'answerFound' is still False after the loop, it means the question was not found in the file.
        if not answerFound:
            print("Jarvis: My sincere apologies, but I'm afraid I do not possess an answer for that particular inquiry. Should you require assistance with any other matter, please do not hesitate to ask.")

while running:
    userInput = input("Jarvis awaits your command: ")
    if userInput == "exit":
        print("Jarvis: It has been a pleasure serving you. Farewell.")
        running = False
    else:
        data_read(userInput, filename)

