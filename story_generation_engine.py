import random

class StoryGenerationEngine:
    def __init__(self, genre="fantasy", theme="adventure"):
        self.genre = genre
        self.theme = theme

    def generate_character(self):
        characters = {
            "fantasy": ["Elf Warrior", "Dragon", "Wizard", "Goblin"],
            "sci-fi": ["Space Marine", "Alien", "AI Robot", "Time Traveler"],
            "mystery": ["Detective", "Criminal", "Ghost", "Forensic Scientist"],
            "adventure": ["Explorer", "Pirate", "Spy", "Treasure Hunter"]
        }
        return random.choice(characters.get(self.genre, ["Unnamed Character"]))

    def generate_setting(self):
        settings = {
            "fantasy": "a mystical forest filled with ancient magic",
            "sci-fi": "a distant planet with advanced alien technology",
            "mystery": "a foggy city where a murder has just occurred",
            "adventure": "a lost island with hidden treasure"
        }
        return settings.get(self.genre, "an interesting place")

    def generate_plot(self):
        plots = {
            "fantasy": "A hero embarks on a quest to defeat a powerful enemy...",
            "sci-fi": "A group of explorers discover a hidden alien technology...",
            "mystery": "A detective uncovers a conspiracy while solving a murder...",
            "adventure": "An explorer finds a map leading to a dangerous treasure..."
        }
        return plots.get(self.genre, "An exciting adventure unfolds...")

if __name__ == "__main__":
    engine = StoryGenerationEngine(genre="adventure", theme="exploration")
    print("Character:", engine.generate_character())
    print("Setting:", engine.generate_setting())
    print("Plot:", engine.generate_plot())
