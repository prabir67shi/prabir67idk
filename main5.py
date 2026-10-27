import random
import re
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored terminal text
init(autoreset=True)

# Predefined responses and data for expanded features
WEATHER_DATA = {
    "columbus": "Sunny with a high of 75°F and a gentle breeze.",
    "new york": "Partly cloudy with a temperature of 68°F.",
    "london": "Overcast with light rain and 55°F.",
    "tokyo": "Clear skies and 72°F."
}

NEWS_HEADLINES = [
    "Tech industry sees a massive surge in AI-driven automation tools.",
    "Global renewable energy adoption reaches a new milestone this quarter.",
    "Local community center hosts annual science and tech fair this weekend."
]

TIME_ZONES = {
    "eastern": "EDT (UTC-4)",
    "pacific": "PDT (UTC-7)",
    "utc": "UTC+0"
}

def get_weather(location):
    """Simulate weather information based on location."""
    loc_lower = location.lower()
    for city, forecast in WEATHER_DATA.items():
        if city in loc_lower:
            return f"{Fore.CYAN}Weather in {city.title()}: {forecast}{Style.RESET_ALL}"
    return f"{Fore.CYAN}Weather (Simulated): Partly cloudy, 70°F with light winds.{Style.RESET_ALL}"

def get_news():
    """Return simulated latest news updates."""
    headline = random.choice(NEWS_HEADLINES)
    return f"{Fore.GREEN}Latest News Update: {headline}{Style.RESET_ALL}"

def get_time(query):
    """Return local time or time zone info."""
    now = datetime.now().strftime("%I:%M %p")
    return f"{Fore.YELLOW}Current local time is {now}.{Style.RESET_ALL}"

def chat_response(user_input):
    """Process user input using regex and keyword matching to return a chatbot response."""
    text = user_input.lower()
    
    # Greeting patterns
    if re.search(r'\b(hi|hello|hey|greetings)\b', text):
        return f"{Fore.MAGENTA}Hello! I'm your enhanced rule-based assistant. How can I help you today?{Style.RESET_ALL}"
    
    # Weather patterns
    elif re.search(r'\b(weather|forecast|temperature)\b', text):
        # Extract city if mentioned
        for city in WEATHER_DATA:
            if city in text:
                return get_weather(city)
        return get_weather("default")
    
    # News patterns
    elif re.search(r'\b(news|headline|updates)\b', text):
        return get_news()
    
    # Time patterns
    elif re.search(r'\b(time|clock|hour)\b', text):
        return get_time(text)
    
    # Help / Capabilities
    elif re.search(r'\b(help|features|what can you do)\b', text):
        return (
            f"{Fore.BLUE}I can assist you with:\n"
            f"- Checking weather conditions (e.g., 'What's the weather in Columbus?')\n"
            f"- Providing news headlines (e.g., 'Give me the news')\n"
            f"- Checking the current time (e.g., 'What time is it?')\n"
            f"- General chat and farewells!{Style.RESET_ALL}"
        )
    
    # Farewell patterns
    elif re.search(r'\b(bye|exit|quit|goodbye)\b', text):
        return f"{Fore.MAGENTA}Goodbye! Have a wonderful day ahead.{Style.RESET_ALL}"
    
    # Default fallback response
    else:
        return f"{Fore.RED}I'm not quite sure I understand. Type 'help' to see what I can do!{Style.RESET_ALL}"

def main():
    """Main execution loop for the chatbot."""
    print(f"{Fore.GREEN}=== Enhanced Rule-Based Chatbot Initialized ==={Style.RESET_ALL}")
    print(f"Type {Fore.YELLOW}'bye'{Style.RESET_ALL} or {Fore.YELLOW}'exit'{Style.RESET_ALL} to end the conversation.\n")
    
    while True:
        try:
            user_input = input(f"{Fore.WHITE}You: {Style.RESET_ALL}")
            if not user_input.strip():
                continue
                
            response = chat_response(user_input)
            print(f"Bot: {response}\n")
            
            if re.search(r'\b(bye|exit|quit|goodbye)\b', user_input.lower()):
                break
        except (KeyboardInterrupt, EOFError):
            print(f"\n{Fore.MAGENTA}Goodbye!{Style.RESET_ALL}")
            break

if __name__ == "__main__":
    main()