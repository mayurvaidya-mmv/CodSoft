import random

class RuleBot:
    def __init__(self):
        self.exit_commands = ("quit", "exit", "bye")

    def greet(self):
        name = input("Your name?\n")
        will_help = input(f"Hello {name}, I'm a bot. Can you help me learn about your planet?\n")
        if will_help.lower() in ("no", "nope", "sorry"):
            print("Enjoy your day on Earth!")
        else:
            self.chat()

    def chat(self):
        while True:
            user_input = input(self.get_random_question()).lower()
            if self.make_exit(user_input):
                print("Have a good day!")
                break
            else:
                self.respond(user_input)

    def get_random_question(self):
        questions = [
            "What's the reason behind your visit?",
            "Are there others like you?",
            "What do you eat here?",
            "Is there intelligent life here?",
            "Is there a leader here?"
        ]
        return random.choice(questions) + "\n"

    def make_exit(self, user_input):
        return user_input in self.exit_commands

    def respond(self, user_input):
        if "your planet" in user_input:
            print(self.describe_planet_intent())
        elif "why are" in user_input:
            print(self.answer_why_intent())
        elif "codehub" in user_input:
            print(self.about_codehub())
        else:
            print(self.no_match_intent())

    def describe_planet_intent(self):
        responses = [
            "My planet is full of different beings.",
            "I've heard the food here is great."
        ]
        return random.choice(responses)

    def answer_why_intent(self):
        responses = [
            "I come in peace.",
            "I'm here to understand your planet and its inhabitants.",
            "I've heard the food here is good."
        ]
        return random.choice(responses)

    def about_codehub(self):
        responses = [
            "Codehub is an educational platform.",
            "Codehub helps in learning new things.",
            "Codehub is a place for growth."
        ]
        return random.choice(responses)

    def no_match_intent(self):
        responses = [
            "Could you tell me more?",
            "Please share more.",
            "Why?"
        ]
        return random.choice(responses)

bot = RuleBot()
bot.greet()
