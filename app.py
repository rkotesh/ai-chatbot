import google.generativeai as genai


API_KEY = "AIzaSyAl9aufrPeGZF3JmFs-PzKCMqfkdarYyd4"
genai.configure(api_key=API_KEY)


model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()




print("Chat with Gemini! Type 'exit' to quit.")
while True:
    User_input = input("You:")
    if User_input.lower() == "exit":
        break
    response = chat.send_message(User_input)
    print("Gemini:", response.text)