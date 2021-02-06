from random import randint, shuffle
from question_manager import *
#from question_manager_working import *

WIDTH = 800
HEIGHT = 600

topic_box = Rect(0, 0, 760, 50)
main_box = Rect(0, 0, 600, 240)
timer_box = Rect(0, 0, 140, 140)
answer_box1 = Rect(0, 0, 370, 100)
answer_box2 = Rect(0, 0, 370, 100)
answer_box3 = Rect(0, 0, 370, 100)
answer_box4 = Rect(0, 0, 370, 100)

topic_box.move_ip(20, 20)
main_box.move_ip(20, 100)
timer_box.move_ip(640, 140)

answer_box1.move_ip(20, 358)
answer_box2.move_ip(20+370+20, 358)
answer_box3.move_ip(20, 480 )
answer_box4.move_ip(20+370+20, 480)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_to_answer = 11
time_left = time_to_answer

topics = list_topics()
shuffle(topics)
print(topics)

def pick_questions_in_topic():
    global topic, topics, question, questions

    topic = topics.pop(0)
    all_questions = load_topic(topic)
    shuffle(all_questions)
    questions = all_questions[0:5]       # pick five questions

    for q in questions:
        shuffle(q["options"])


pick_questions_in_topic()
question = questions.pop(0)

def draw():
    screen.fill("gray")
    screen.draw.filled_rect(topic_box, "pink")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")

    screen.draw.textbox(convert_filename_to_topic(topic), topic_box, color="black")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")

    screen.draw.textbox(str(time_left), timer_box, color="black")
    screen.draw.textbox(question["statement"], main_box, color="black")

    for index, box in enumerate(answer_boxes):
        screen.draw.textbox(question["options"][index], box, color="black")


def game_over():
    global question, time_left

    message = "Game over. You got %s questions correct." % score
    #question = [message, "-", "-", "-", "-", 5]
    question = {"statement":message, "answer":"", "options":["-","-","-","-"]}
    time_left = 0


def correct_answer():

    global question, questions, score, time_left

    score += 1

    if questions:   # not run out of questions in current topic
        question = questions.pop(0)
        time_left = time_to_answer
    elif topics:    # not run out of topics
        pick_questions_in_topic()
        question = questions.pop(0)
    else:
        print("End of questions")
        game_over()


def on_mouse_down(pos):

    for index, box in enumerate(answer_boxes):
        if box.collidepoint(pos):
            print("Clicked on answer %s " % index)
            if question["options"][index] == question["answer"]:
                print("You got it right!")
                correct_answer()
            else:
                game_over()


def update_time():
    global time_left

    if time_left:
        time_left = time_left - 1
    else:
        game_over()

clock.schedule_interval(update_time, 1.0)
