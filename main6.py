import time
import sys
from textblob import TextBlob
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored terminal output
init(autoreset=True)

class SentimentSpy:
    def __init__(self, username):
        self.username = username
        self.history = []
        self.counts = {
            "positive": 0,
            "negative": 0,
            "neutral": 0
        }

    def show_processing_animation(self):
        """Displays a spy-themed loading animation while analyzing sentiment."""
        chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
        sys.stdout.write(f"{Fore.CYAN}[SpyBot] Analyzing intelligence... {Style.RESET_ALL}")
        sys.stdout.flush()
        for _ in range(3):
            for char in chars:
                sys.stdout.write(f"\b{char}")
                sys.stdout.flush()
                time.sleep(0.05)
        sys.stdout.write("\b✓ Done!\n")
        sys.stdout.flush()

    def analyze_sentiment(self, text):
        """Analyzes text sentiment using TextBlob and classifies it."""
        self.show_processing_animation()
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        # Thresholds: Positive > 0.25, Negative < -0.25, Neutral in between
        if polarity > 0.25:
            sentiment = "positive"
            color = Fore.GREEN
            desc = "Positive"
        elif polarity < -0.25:
            sentiment = "negative"
            color = Fore.RED
            desc = "Negative"
        else:
            sentiment = "neutral"
            color = Fore.YELLOW
            desc = "Neutral"

        self.counts[sentiment] += 1
        self.history.append({"text": text, "sentiment": sentiment, "polarity": polarity})

        print(f"{color}>> Intelligence Report: {desc} sentiment detected! (Polarity Score: {polarity:.2f}){Style.RESET_ALL}\n")

    def show_summary(self):
        """Displays the current sentiment analysis summary statistics."""
        print(f"\n{Fore.BLUE}=== Mission Summary (Live Statistics) ===")
        print(f"Positive messages: {self.counts['positive']}")
        print(f"Negative messages: {self.counts['negative']}")
        print(f"Neutral messages: {self.counts['neutral']}")
        print(f"Total analyzed: {sum(self.counts.values())}{Style.RESET_ALL}\n")

    def show_history(self):
        """Displays all previous messages and their sentiment analyses."""
        print(f"\n{Fore.MAGENTA}=== Conversation & Intelligence History ===")
        if not self.history:
            print("No intelligence recorded yet.")
        else:
            for idx, entry in enumerate(self.history, 1):
                print(f"{idx}. Text: \"{entry['text']}\" | Sentiment: {entry['sentiment'].upper()} (Polarity: {entry['polarity']:.2f})")
        print(f"{Style.RESET_ALL}")

    def reset_data(self):
        """Resets all stored conversation history and sentiment counters."""
        self.history = []
        self.counts = {"positive": 0, "negative": 0, "neutral": 0}
        print(f"{Fore.YELLOW}[SpyBot] All intelligence records and counters have been reset.{Style.RESET_ALL}\n")

    def show_help(self):
        """Lists available command options."""
        print(f"\n{Fore.CYAN}=== Available Spy Commands ===")
        print("- summary : Displays live sentiment statistics.")
        print("- history : Displays all previous messages and analyses.")
        print("- reset   : Resets all recorded conversation history and counters.")
        print("- help    : Lists available commands.")
        print(f"- exit    : Terminates session and generates final report file.{Style.RESET_ALL}\n")

    def execute_command(self, command):
        """Handles special command inputs."""
        cmd = command.strip().lower()
        if cmd == "summary":
            self.show_summary()
        elif cmd == "history":
            self.show_history()
        elif cmd == "reset":
            self.reset_data()
        elif cmd == "help":
            self.show_help()
        else:
            print(f"{Fore.RED}[SpyBot] Unknown command. Type 'help' for available commands.{Style.RESET_ALL}\n")

    def save_final_report(self):
        """Saves the final summary report to <username>_sentiment_analysis.txt."""
        filename = f"{self.username}_sentiment_analysis.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"=== Sentiment Spy: Mission Report ===\n")
                f.write(f"Agent/User: {self.username}\n\n")
                f.write(f"Positive messages: {self.counts['positive']}\n")
                f.write(f"Negative messages: {self.counts['negative']}\n")
                f.write(f"Neutral messages: {self.counts['neutral']}\n")
                f.write(f"Total messages analyzed: {sum(self.counts.values())}\n\n")
                f.write("=== Full Log ===\n")
                for idx, entry in enumerate(self.history, 1):
                    f.write(f"{idx}. [{entry['sentiment'].upper()}] {entry['text']} (Polarity: {entry['polarity']:.2f})\n")
            print(f"{Fore.GREEN}[SpyBot] Final report successfully encrypted and saved to '{filename}'.{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[SpyBot] Error saving report file: {e}{Style.RESET_ALL}")

def get_valid_name():
    """Prompts the user for their name, ensuring it contains only alphabetic characters."""
    while True:
        name = input(f"{Fore.WHITE}Agent, please enter your name: {Style.RESET_ALL}").strip()
        if name.isalpha():
            return name
        print(f"{Fore.RED}Invalid name. Please use alphabetic characters only.{Style.RESET_ALL}")

def main():
    print(f"{Fore.GREEN}=== Sentiment Spy: Mission Initialized ==={Style.RESET_ALL}")
    username = get_valid_name()
    
    spy = SentimentSpy(username)
    print(f"\n{Fore.CYAN}Welcome agent {username}! Type any sentence to analyze its sentiment, or type 'help' for commands.{Style.RESET_ALL}")
    print(f"Type {Fore.YELLOW}'exit'{Style.RESET_ALL} when you are ready to conclude your mission.\n")

    while True:
        try:
            user_input = input(f"{Fore.WHITE}Agent Input: {Style.RESET_ALL}").strip()
            if not user_input:
                continue

            if user_input.lower() == "exit":
                print(f"\n{Fore.MAGENTA}[SpyBot] Terminating session. Generating final mission debrief...{Style.RESET_ALL}")
                spy.show_summary()
                spy.save_final_report()
                print(f"{Fore.MAGENTA}Mission completed. Farewell, Agent {username}!{Style.RESET_ALL}")
                break

            elif user_input.lower() in ["summary", "history", "reset", "help"]:
                spy.execute_command(user_input.lower())
            else:
                spy.analyze_sentiment(user_input)

        except (KeyboardInterrupt, EOFError):
            print(f"\n{Fore.MAGENTA}[SpyBot] Emergency exit triggered. Saving progress...{Style.RESET_ALL}")
            spy.save_final_report()
            break

if __name__ == "__main__":
    main()