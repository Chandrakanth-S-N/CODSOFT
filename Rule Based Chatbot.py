import re 
import random
class RuleBot:
    negative_response = ('no', 'nope', 'nah', 'not', 'never', 'not at all', 'not a chance', 'sorry')
    exit_commands = ('quit', 'exit', 'bye', 'goodbye', 'later')
    random_questions = (
        'What is your favorite hobby?', 
        'Which book are you reading?', 
        'Do you like traveling?', 
        'What is your favorite movie?'
    )
    def __init__(self):
        self.introduction = {
            'introductory': r'.*\s*your purpose.*',
            'answer_why_intent': r'why\sare.*',
            'about_chatbot': r'.*\s*chatbot'
        }
    def greet(self):
        self.name = input("What's your name?\n")
        will_help = input(f"Hi {self.name}, I am a RuleBot. Would you chat with me?\n")
        if will_help.lower() in self.negative_response:
            print("Okay, have a great day!")
            return 
        self.chat() 
    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Alright, talk to you later!")
                return True
        return False
    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply)).lower()
    def match_reply(self, reply):
        for key, value in self.introduction.items(): 
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'introductory':
                return self.introductory()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'about_chatbot':
                return self.about_chatbot()
        return self.no_match_intent()
    def introductory(self):
        responses = ("I'm here to have a friendly chat with you.\n", "I was created to make conversations more fun!\n")
        return random.choice(responses)

    def answer_why_intent(self):
        responses = ("I want to learn more about humans.\n", "I'm just curious about your world.\n", "I'm here to understand what you like.\n")
        return random.choice(responses)

    def about_chatbot(self):
        responses = ("I'm a simple chatbot designed for casual conversations.\n", "I'm here to make your day a little brighter!\n")
        return random.choice(responses)

    def no_match_intent(self):
        responses = (
            "That's interesting! Tell me more.\n", "Can you explain that a bit more?\n", "I'd love to hear more about that.\n", "Why do you say that?\n", "Can you elaborate on that?\n")
        return random.choice(responses)
bot = RuleBot()
bot.greet()