from textblob import TextBlob

class AdaptiveFeedbackSystem:
    def __init__(self):
        self.feedback_log = []

    def provide_feedback(self, contribution):
        feedback = self.analyze_sentiment(contribution)
        self.feedback_log.append(feedback)
        return feedback

    def analyze_sentiment(self, text):
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity
        if sentiment_score > 0:
            feedback = "Great use of positive tone! Keep it up!"
        elif sentiment_score < 0:
            feedback = "Your story seems to have a dark tone. Consider adding some positive elements."
        else:
            feedback = "Neutral tone. Maybe add some emotional highlights?"
        return feedback

    def get_feedback_log(self):
        return self.feedback_log

if __name__ == "__main__":
    feedback_system = AdaptiveFeedbackSystem()
    print(feedback_system.provide_feedback("The dragon soared majestically through the night sky."))
    print(feedback_system.provide_feedback("A shadow loomed over the city, sending chills down everyone's spine."))
    print("Feedback Log:", feedback_system.get_feedback_log())
