import glob
from pprint import pprint

def convert_filename_to_topic(filename):
    """Convert topic filname to topic title (for printing)."""

    return filename.replace(".txt", "").replace("questions/", "").replace("_", " ")


def list_topics():
    """Return list of available question topics."""

    files = glob.glob("questions/*.txt")

    return files


def load_topic(topic):
    """Load all questions for the given topic."""

    questions = []
    with open(topic) as infile:
        for line in infile.readlines():
            data = [d.strip() for d in line.split(",")]
            question = { "statement":data[0], "answer":data[1], "options": data[1:5] }

            questions.append(question)
        pass

    return questions


def save_topic(topic, questions):
    """Save list of questions to the given topic."""

    return


# code to run when testing
if __name__ == "__main__":

    print("Testing question_manager ...")

    print("\nTesting function 'list_topics'  ...")
    topics = list_topics()
    print(topics)

    print("\nTesting function 'convert_filename_to_topic' ...")
    for topic in topics:
        print(topic, "->", convert_filename_to_topic(topic))

    print("\nTesting function 'load_topic' ...")
    topic = topics[0]
    questions = load_topic(topic)
    for question in questions:
        pprint(question)






