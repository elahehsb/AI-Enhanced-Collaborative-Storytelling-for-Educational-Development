import time

class CollaborativePlatform:
    def __init__(self):
        self.story_content = []
        self.interaction_log = []

    def add_contribution(self, student, contribution):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        self.story_content.append(f"{timestamp} - {student}: {contribution}")
        self.log_interaction(student, contribution, "Human")
        return self.get_story()

    def ai_suggestion(self, suggestion):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        self.story_content.append(f"{timestamp} - AI: {suggestion}")
        self.log_interaction("AI", suggestion, "AI")
        return self.get_story()

    def log_interaction(self, author, content, source):
        self.interaction_log.append({
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
            "author": author,
            "content": content,
            "source": source
        })

    def get_story(self):
        return "\n".join(self.story_content)

    def get_interaction_log(self):
        return self.interaction_log

if __name__ == "__main__":
    platform = CollaborativePlatform()
    platform.add_contribution("Student1", "Once upon a time in a galaxy far away...")
    platform.ai_suggestion("A mysterious signal is detected from an unknown planet.")
    print(platform.get_story())
    print("Interaction Log:", platform.get_interaction_log())
