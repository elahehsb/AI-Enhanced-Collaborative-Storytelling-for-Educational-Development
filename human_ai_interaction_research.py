from textblob import TextBlob

class HumanAIInteractionResearch:
    def __init__(self):
        self.interactions = []

    def log_interaction(self, student_input, ai_suggestion):
        sentiment = self.analyze_sentiment(student_input)
        self.interactions.append({
            "student_input": student_input,
            "ai_suggestion": ai_suggestion,
            "resulting_action": "Accepted" if random.random() > 0.5 else "Rejected",
            "student_sentiment": sentiment
        })

    def analyze_sentiment(self, text):
        blob = TextBlob(text)
        return blob.sentiment.polarity

    def analyze_interactions(self):
        accepted = len([i for i in self.interactions if i["resulting_action"] == "Accepted"])
        rejected = len(self.interactions) - accepted
        avg_sentiment = sum(i["student_sentiment"] for i in self.interactions) / len(self.interactions)
        return {"accepted": accepted, "rejected": rejected, "avg_sentiment": avg_sentiment}

if __name__ == "__main__":
    research = HumanAIInteractionResearch()
    research.log_interaction("The spaceship lands on an alien planet.", "AI suggests exploring the planet's surface.")
    research.log_interaction("The detective examines the clues.", "AI suggests interviewing a witness.")
    print("Interaction Analysis:", research.analyze_interactions())
