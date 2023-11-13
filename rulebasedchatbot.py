import random

class RuleBot:
    negative_res = ("no", "nope", "sorry")
    exit_commands = ("quit", "exit", "bye")
    random_questions = [
        "Why are you here?",
        "Are there many humans like you?",
        "Is there intelligent life on this planet?",
        "Does Earth have a leader?"
    ]

    def __init__(self):
        self.alien_babble = {
            'describe_planet_intent': 'your planet',
            'answer_why_intent': 'why are',
            'about_codsoft': 'codsoft'
        }

    def greet(self):
        name = input("Your name?\n")
        will_help = input(f"Hi {name}, I'm a bot. Can you help me learn about your planet?\n")
        if will_help.lower() in self.negative_res:
            print("Enjoy your day on Earth!")
            return
        self.chat()

    def make_exit(self, reply):
        return reply in self.exit_commands

    def chat(self):
        while True:
            reply = input(random.choice(self.random_questions) + "\n").lower()
            if self.make_exit(reply):
                print("Goodbye!")
                break
            self.respond(reply)

    def respond(self, reply):
        if 'your planet' in reply:
            print(random.choice(["My planet is diverse.", "Food here is great."]))
        elif 'why are' in reply:
            print(random.choice(["I come in peace.", "I'm here to learn.", "Food is good here."]))
        elif 'codsoft' in reply:
            print("CodSoft is an innovative educational platform providing diverse learning opportunities and fostering skill development.")
        else:
            print(random.choice(["Please tell me more.", "Can you elaborate?", "Why?"]))

bot = RuleBot()
bot.greet()
