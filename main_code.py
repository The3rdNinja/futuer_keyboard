#note that this code will only work good for my computer bc of the screen size and the input/output devices. still in process. i will probobly update it so it will fit on every device
#i wrote this code and it took me hours to write it. pls respect and do not steal my idea without pormission!



import pyautogui
import pygame
import speech_recognition as sr
from pygame.locals import *
import threading
from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS
import cv2
import mediapipe as mp
import pulsectl
import time


def set_volume(volume_percentage):
    with pulsectl.Pulse('volume-setting-script') as pulse:
        # Find the default sink (output device)
        sink = pulse.sink_list()[0]

        # Set the volume percentage
        volume = volume_percentage / 100.0
        pulse.volume_set_all_chans(sink, volume)
        
        
def play_audio_file(file_path, tts):
    tts = gTTS(tts)
    tts.save(file_path)
    audio = AudioSegment.from_file(file_path)
    play(audio)


# Print the available microphone devices
print(sr.Microphone.list_microphone_names())

# Specify the desired device index when creating the Microphone instance
microphone = sr.Microphone(device_index=13)

img = 'background1.jpg'

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
SILVER = (192, 192, 192)
GRAY = (128, 128, 128)
MAROON = (128, 0, 0)
OLIVE = (128, 128, 0)
LIME = (0, 128, 0)
AQUA = (0, 255, 255)
TEAL = (0, 128, 128)
NAVY = (0, 0, 128)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
PINK = (255, 192, 203)
BROWN = (165, 42, 42)
GOLD = (255, 215, 0)
SALMON = (250, 128, 114)
TURQUOISE = (64, 224, 208)
VIOLET = (238, 130, 238)
INDIGO = (75, 0, 130)
CORAL = (255, 127, 80)
TOMATO = (255, 99, 71)
KHAKI = (240, 230, 140)
PLUM = (221, 160, 221)
SKY_BLUE = (135, 206, 235)
DARK_GREEN = (0, 100, 0)
STEEL_BLUE = (70, 130, 180)
GAINSBORO = (220, 220, 220)
LIGHT_GRAY = (211, 211, 211)
ROSY_BROWN = (188, 143, 143)
LAVENDER = (230, 230, 250)
PALE_GREEN = (152, 251, 152)
LIGHT_BLUE = (173, 216, 230)
ORCHID = (218, 112, 214)
HOT_PINK = (255, 105, 180)
DARK_ORANGE = (255, 140, 0)
MEDIUM_PURPLE = (147, 112, 219)
DARK_OLIVE_GREEN = (85, 107, 47)
FIREBRICK = (178, 34, 34)
ROYAL_BLUE = (65, 105, 225)
CORNFLOWER_BLUE = (100, 149, 237)
DARK_SLATE_GRAY = (47, 79, 79)
MEDIUM_SLATE_BLUE = (123, 104, 238)
DARK_GOLDENROD = (184, 134, 11)
DARK_TURQUOISE = (0, 206, 209)
CADET_BLUE = (95, 158, 160)
INDIAN_RED = (205, 92, 92)
MEDIUM_VIOLET_RED = (199, 21, 133)
DARK_KHAKI = (189, 183, 107)
DARK_MAGENTA = (139, 0, 139)
DARK_SEA_GREEN = (143, 188, 143)
DODGER_BLUE = (30, 144, 255)
MEDIUM_AQUAMARINE = (102, 205, 170)
DARK_SLATE_BLUE = (72, 61, 139)
DIM_GRAY = (105, 105, 105)
MEDIUM_SEA_GREEN = (60, 179, 113)
MEDIUM_ORCHID = (186, 85, 211)
SIENNA = (160, 82, 45)
MEDIUM_SPRING_GREEN = (0, 250, 154)
FOREST_GREEN = (34, 139, 34)
SLATE_GRAY = (112, 128, 144)
DARK_CYAN = (0, 139, 139)
MEDIUM_BLUE = (0, 0, 205)
DEFAULT = WHITE

# Button Size
BUTTON_WIDTH = 90
BUTTON_HEIGHT = 90

# Initialize Pygame
pygame.init()

# Create the screen
screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Button Example")

the_color = DEFAULT
the_background_color = BLACK
the_button_color = DEFAULT
the_button_border = 10

smart_type_list = ''

Hebrew_font = 'Varela_Round/VarelaRound-Regular.ttf'
English_font = None

font_lang = English_font

color1 = DEFAULT
said_size = min(screen_width // 30, screen_height // 30)

English = [
    ['esc', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12'],
    ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'backspace'],
    ['tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
    ['caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'enter'],
    ['l-shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'r-shift'],
    ['ctrl', 'windows', 'alt', 'space', 'alt', 'windows', 'FN', 'ctrl']
]

Hebrew = [
    ['esc', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12'],
    [';', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'backspace'],
    ['tab', '/', "'", 'ק', 'ר', 'א', 'ט', 'ו', 'ן', 'ם', 'פ', '[', ']', '\\'],
    ['caps', 'ש', 'ד', 'ג', 'כ', 'ע', 'י', 'ח', 'ל', 'ך', 'ף', ",", 'enter'],
    ['l-shift', 'ז', 'ס', 'ב', 'ה', 'נ', 'מ', 'צ', 'ת', 'ץ', '.', 'r-shift'],
    ['ctrl', 'windows', 'alt', 'space', 'alt', 'windows', 'FN', 'ctrl']
]

def update_languge(lang, lang_font):
    global font, font1, smart_type_font, text1, button_rects, spaciel_button_font
    # Create a font object
    font = pygame.font.Font(lang_font, said_size)
    spaciel_button_font = pygame.font.Font(None, said_size)
    font1 = pygame.font.Font(None, said_size)
    smart_type_font = pygame.font.Font(lang_font, said_size)
    text1 = font1.render('im listening...', True, the_color)

    keys = lang
    # Create the button rectangles
    button_rects = []
    y = -750  # Shifted 300 pixels to the left
    hi = -300  # Shifted 300 pixels up
    for lines in range(len(keys)):
        for x in keys[lines]:
            if x in ['ctrl', 'windows', 'alt', 'FN']:
                button_rect = pygame.Rect(
                    (screen_width - BUTTON_WIDTH) // 2 + y,
                    (screen_height - BUTTON_HEIGHT) // 2 + hi,
                    BUTTON_WIDTH + 40,
                    BUTTON_HEIGHT
                )
                y += 140
            elif x == 'space':
                button_rect = pygame.Rect(
                    (screen_width - BUTTON_WIDTH) // 2 + y,
                    (screen_height - BUTTON_HEIGHT) // 2 + hi,
                    BUTTON_WIDTH + 490,
                    BUTTON_HEIGHT
                )
                y += 590
            elif x in ['l-shift', 'enter']:
                button_rect = pygame.Rect(
                    (screen_width - BUTTON_WIDTH) // 2 + y,
                    (screen_height - BUTTON_HEIGHT) // 2 + hi,
                    BUTTON_WIDTH + 170,
                    BUTTON_HEIGHT
                )
                y += 270
            elif x in ['caps']:
                button_rect = pygame.Rect(
                    (screen_width - BUTTON_WIDTH) // 2 + y,
                    (screen_height - BUTTON_HEIGHT) // 2 + hi,
                    BUTTON_WIDTH + 100,
                    BUTTON_HEIGHT
                )
                y += 200
            elif x in ['backspace']:
                button_rect = pygame.Rect(
                    (screen_width - BUTTON_WIDTH) // 2 + y,
                    (screen_height - BUTTON_HEIGHT) // 2 + hi,
                    BUTTON_WIDTH + 170,
                    BUTTON_HEIGHT
                )
                y += 270
            elif x in ['tab']:
                button_rect = pygame.Rect(
                    (screen_width - BUTTON_WIDTH) // 2 + y,
                    (screen_height - BUTTON_HEIGHT) // 2 + hi,
                    BUTTON_WIDTH + 80,
                    BUTTON_HEIGHT
                )
                y += 180
            elif x in ['\\']:
                button_rect = pygame.Rect(
                    (screen_width - BUTTON_WIDTH) // 2 + y,
                    (screen_height - BUTTON_HEIGHT) // 2 + hi,
                    BUTTON_WIDTH + 90,
                    BUTTON_HEIGHT
                )
                y += 190
            elif x in ['r-shift']:
                button_rect = pygame.Rect(
                    (screen_width - BUTTON_WIDTH) // 2 + y,
                    (screen_height - BUTTON_HEIGHT) // 2 + hi,
                    BUTTON_WIDTH + 200,
                    BUTTON_HEIGHT
                )
                y += 300
            elif x in ['esc', 'F4', 'F8']:
                button_rect = pygame.Rect(
                    (screen_width - BUTTON_WIDTH) // 2 + y,
                    (screen_height - BUTTON_HEIGHT) // 2 + hi,
                    BUTTON_WIDTH,
                    BUTTON_HEIGHT
                )
                y += 190
            else:
                button_rect = pygame.Rect(
                    (screen_width - BUTTON_WIDTH) // 2 + y,
                    (screen_height - BUTTON_HEIGHT) // 2 + hi,
                    BUTTON_WIDTH,
                    BUTTON_HEIGHT
                )
                y += 100
            button_rects.append((x, button_rect, BLACK))

        if lines == 0:
            hi += 120
        else:
            hi += 110
        y = -750  # Reset to -300 for each line

    # Define the position (x, y) for the new buttons
    x = 1440
    y = 80

    # Create new button rectangles at the specified position
    button1_rect = pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)
    button2_rect = pygame.Rect(x + 100, y, BUTTON_WIDTH, BUTTON_HEIGHT)
    button3_rect = pygame.Rect(x + 200, y, BUTTON_WIDTH, BUTTON_HEIGHT)
    button4_rect = pygame.Rect(x - 100, y, BUTTON_WIDTH, BUTTON_HEIGHT)

    # Append the new button rectangles to the button_rects list
    button_rects.append(("voice", button1_rect, BLACK))
    button_rects.append(("volume", button2_rect, BLACK))
    button_rects.append(("scroll", button3_rect, BLACK))
    button_rects.append(("smart", button4_rect, BLACK))



update_languge(Hebrew, Hebrew_font)
# Function to reset button color to black


def voice_fun():
    global voice_on
    voice_on = True


def reset_button_color(button_index):
    button_label, button_rect, _ = button_rects[button_index]
    button_rects[button_index] = (button_label, button_rect, BLACK)


def change_font_size(said_size):
    global font1, font, smart_type_font
    font = pygame.font.Font(None, said_size)
    font1 = pygame.font.Font(None, said_size)
    smart_type_font = pygame.font.Font(None, said_size)

# Function to change the keyboard color


def change_keyboard_color(color):
    global color1
    color1 = color


scroll_lock = threading.Lock()


def scroll(direction):
    with scroll_lock:
        pyautogui.scroll(scroll_increment * direction)


def delay_and_reset_direction():
    global scroll_direction
    time.sleep(scroll_delay)
    scroll_direction = 0
    print("changed to: ", scroll_direction)

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

scroll_increment = 3
scroll_direction = 0
scroll_delay = 1  # Delay in seconds


def cam():
    global scroll_direction
    while True:
        if scroll_on:
            mp_drawing = mp.solutions.drawing_utils
            mp_hands = mp.solutions.hands

            # Set up webcam
            cap = cv2.VideoCapture(1)

            scroll_direction = 0

            with mp_hands.Hands(
                    min_detection_confidence=0.8,
                    min_tracking_confidence=0.8
            ) as hands:
                while cap.isOpened() and scroll_on:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    print(scroll_direction)

                    # Flip the frame horizontally for a mirrored view
                    frame = cv2.flip(frame, 1)

                    # Convert the BGR frame to RGB
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                    # Process the frame with Mediapipe
                    results = hands.process(frame_rgb)

                    # Draw hand landmarks on the frame
                    annotated_frame = frame.copy()
                    if results.multi_hand_landmarks:
                        for hand_landmarks in results.multi_hand_landmarks:
                            mp_drawing.draw_landmarks(
                                annotated_frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                            # Calculate the average hand opening value
                            palm_landmarks = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y
                            finger_landmarks = [
                                hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y,
                                hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y,
                                hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y,
                                hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y,
                                hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y
                            ]
                            avg_landmark = sum(finger_landmarks) / len(finger_landmarks)
                            hand_open_value = (palm_landmarks - avg_landmark) / (
                                    palm_landmarks - hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y)

                            # Get the coordinates of specific hand landmarks
                            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                            middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                            is_index_finger_up = index_finger_tip.y < middle_finger_tip.y
                            is_middle_finger_up = middle_finger_tip.y < index_finger_tip.y

                            if is_index_finger_up and not is_middle_finger_up:
                                print("Scroll up!")
                                if scroll_direction == 0:
                                    scroll_direction = 1
                                    threading.Thread(target=scroll, args=(1,)).start()
                                    threading.Thread(target=delay_and_reset_direction).start()

                            elif not is_index_finger_up and is_middle_finger_up and hand_open_value < 1.4:
                                print("Scroll down!")
                                if scroll_direction == 0:
                                    scroll_direction = -1
                                    threading.Thread(target=scroll, args=(-1,)).start()
                                    threading.Thread(target=delay_and_reset_direction).start()

                            else:
                                scroll_direction = 0
        elif volume_on:
            mp_drawing = mp.solutions.drawing_utils
            mp_hands = mp.solutions.hands

            # Set up webcam
            cap = cv2.VideoCapture(1)

            last_left_check_time = time.time()

            with mp_hands.Hands(
                    min_detection_confidence=0.8,
                    min_tracking_confidence=0.8
            ) as hands:
                while cap.isOpened() and volume_on:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    # Flip the frame horizontally for a mirrored view
                    frame = cv2.flip(frame, 2)

                    # Convert the BGR frame to RGB
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                    # Process the frame with Mediapipe
                    results = hands.process(frame_rgb)

                    # Draw hand landmarks on the frame
                    annotated_frame = frame.copy()
                    if results.multi_hand_landmarks:
                        # Iterate through each detected hand
                        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                            # Check if the detected hand is the left hand
                            if True:
                                # Get the landmarks of the thumb and index finger for left hand
                                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

                                # Calculate the Euclidean distance between thumb and index finger tips
                                left_hand_distance = ((thumb_tip.x - index_finger_tip.x) * 2 + (
                                            thumb_tip.y - index_finger_tip.y) * 2) ** 0.5
                                left_hand_distance = complex(left_hand_distance)  # Convert to complex number
                                left_hand_distance = left_hand_distance.real  # Get the real part (float value)

                                # Detect hand gesture based on distance for left hand
                                if left_hand_distance < 0.05:  # Adjust this threshold based on your hand size
                                    current_left_state = "close"
                                    print("Left hand close")
                                else:
                                    current_left_state = "open"
                                    print("Left hand open")

                                current_time = time.time()
                                # Check if 1 second has passed since the last left hand check
                                if current_time - last_left_check_time >= 1.0:
                                    # Perform volume control action
                                    max_distance = 0.65  # Adjust this value based on your hand size and preference
                                    percentage = min(left_hand_distance / max_distance, 1.0) * 100
                                    set_volume(percentage)

                                    # Update the previous left hand state and the last left hand check time
                                    previous_left_state = current_left_state
                                    last_left_check_time = current_time

                                # Draw hand landmarks on the frame for left hand
                                mp_drawing.draw_landmarks(
                                    annotated_frame,
                                    hand_landmarks,
                                    mp_hands.HAND_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=2),
                                    mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)
                                )


def handle_voice_commands(): # Function to handle voice commands
    global recognized_text, font1, text1, voice_command_on , text, the_color, the_background_color, the_button_color, the_button_border
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    the_color = DEFAULT
    the_background_color = BLACK

    while True:
        if voice_on:
            set_volume(100)
            with microphone as source:
                print("Say something...")
                recognized_text = 'im listening...'
                text1 = font1.render(recognized_text, True, the_color)
                audio = recognizer.listen(source, timeout=5)  # Set the timeout to 5 seconds

            try:
                recognized_text = recognizer.recognize_google(audio)
                print("Recognized text:", recognized_text)

                # Update the text1 surface with the recognized text
                font1 = pygame.font.Font(None, said_size)
                text1 = font1.render(recognized_text, True, the_color)

                if 'goodbye' in recognized_text:
                    recognized_text = ''

                elif 'keyboard' in recognized_text:
                    if 'language' in recognized_text:
                        if 'English' in recognized_text:
                            threading.Thread(target=lambda: play_audio_file('hello.mp3', f'changing the keyboard language to English')).start()
                            update_languge(English, English_font)
                        elif 'Hebrew' in recognized_text:
                            threading.Thread(target=lambda: play_audio_file('hello.mp3', f'changing the keyboard language to Hebrew')).start()
                            update_languge(Hebrew, Hebrew_font)
                    elif 'background' in recognized_text:
                        recognized_text = recognized_text.split(' ')
                        the_background_color = recognized_text[-1]
                        threading.Thread(target=lambda: play_audio_file('hello.mp3', f'changing the background color to {the_background_color}')).start()
                        the_background_color = the_background_color.upper()
                        if the_background_color == 'SCIENCE':
                            the_background_color = 'CYAN'
                        print(the_background_color)
                    elif 'button' in recognized_text:
                        if 'color' in recognized_text:
                            recognized_text = recognized_text.split(' ')
                            the_button_color = recognized_text[-1]
                            threading.Thread(target=lambda: play_audio_file('hello.mp3', f'changing the button color to {the_button_color}')).start()
                            the_button_color = the_button_color.upper()
                            if the_button_color == 'SCIENCE':
                                the_button_color = 'CYAN'
                            print(the_button_color)
                        elif 'border' in recognized_text:
                            recognized_text = recognized_text.split(' ')
                            the_button_border = int(recognized_text[-1])
                            threading.Thread(target=lambda: play_audio_file('hello.mp3', f'changing the button border to {str(the_button_border)}')).start()
                            print(the_button_border)
                    elif 'font' in recognized_text or 'phone' in recognized_text or 'on' in recognized_text:
                        if 'size' in recognized_text:
                            recognized_text = recognized_text.split(' ')
                            num = int(recognized_text[-1])
                            threading.Thread(target=lambda: play_audio_file('hello.mp3', f'changing the font of your keyboard to {num}!')).start()
                            change_font_size(num)
                        elif 'color' in recognized_text:
                            recognized_text = recognized_text.split(' ')
                            the_color = recognized_text[-1]
                            threading.Thread(target=lambda: play_audio_file('hello.mp3', f'changing the font color to {the_color}!')).start()
                            the_color = the_color.upper()
                            if the_color == 'SCIENCE':
                                the_color = 'CYAN'
                            print(the_color)

                    elif 'color' in recognized_text or 'Color' in recognized_text:
                        recognized_text = recognized_text.split(' ')
                        keyboard_color = recognized_text[-1]
                        keyboard_color = keyboard_color.upper()
                        if keyboard_color == 'SCIENCE':
                            keyboard_color = 'CYAN'
                        print(keyboard_color)
                        threading.Thread(target=lambda: play_audio_file('hello.mp3', f'changing the keyboard color to {keyboard_color}!')).start()
                        change_keyboard_color(keyboard_color)
                    else:
                        print("Invalid command")
                        recognized_text = "Invalid command"
                        #play_audio_file('hello.mp3', '"Invalid command"')
            except sr.UnknownValueError:
                if recognized_text != '':
                    recognized_text = "Unable to recognize speech"
                    #play_audio_file('hello.mp3', 'sorry i did not understand')
                    print("Unable to recognize speech")


voice_on = False

# Start a separate thread to handle voice commands
voice_thread = threading.Thread(target=handle_voice_commands)
voice_thread.start()

scroll_on = False
volume_on = False
# Start a separate thread to handle voice commands
cam_thread = threading.Thread(target=cam)
cam_thread.start()
# Load the image
image = pygame.image.load(img)
image = pygame.transform.scale(image, (screen_width, screen_height))

# Run the game loop
caps_on = False
smart_type_on = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONUP:  # Handle mouse button click event
            if event.button == 1:  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()
                for i, (button_label, button_rect, button_color) in enumerate(button_rects):
                    if button_rect.collidepoint(mouse_pos):
                        print("Clicked:", button_label)
                        if button_label == 'smart type' or button_label == 'enter' or button_label == 'l-shift' or button_label == 'r-shift' or button_label == 'windows' or button_label == 'ctrl' or button_label == 'alt' or button_label == 'caps' or button_label == 'FN':
                            pass
                        elif button_label == 'tab':
                            smart_type_list += '   '
                        elif button_label == 'space':
                            smart_type_list += ' '
                        elif button_label == 'backspace':
                            smart_type_list = smart_type_list[:-1]
                        else:
                            smart_type_list += button_label
                        # Change button color from black to gray
                        button_rects[i] = (button_label, button_rect, GRAY)

                        if button_label == 'caps':
                            if not caps_on:
                                threading.Thread(target=lambda: play_audio_file('hello.mp3', 'turning on caps lock!')).start()
                                caps_on = True
                            else:
                                threading.Thread(target=lambda: play_audio_file('hello.mp3', 'turning off caps lock!')).start()
                                # Create a timer to reset button color back to black after 1 second
                                threading.Timer(0.1, reset_button_color, args=(i,)).start()
                                caps_on = False

                        elif button_label == 'volume':
                            if not volume_on:
                                threading.Thread(target=lambda: play_audio_file('hello.mp3', 'turning on finger volume!')).start()
                                volume_on = True
                            else:
                                threading.Thread(target=lambda: play_audio_file('hello.mp3', 'turning off finger volume!')).start()
                                # Create a timer to reset button color back to black after 1 second
                                threading.Timer(0.1, reset_button_color, args=(i,)).start()
                                volume_on = False

                        elif button_label == 'scroll':
                            if not scroll_on:
                                threading.Thread(target=lambda: play_audio_file('hello.mp3', 'turning on finger scrolling!')).start()
                                scroll_on = True
                            else:
                                threading.Thread(target=lambda: play_audio_file('hello.mp3', 'turning off finger scrolling!')).start()
                                # Create a timer to reset button color back to black after 1 second
                                threading.Timer(0.1, reset_button_color, args=(i,)).start()
                                scroll_on = False

                        elif button_label == 'smart':
                            if not smart_type_on:
                                threading.Thread(target=lambda: play_audio_file('hello.mp3', 'turning on smart type!')).start()
                                smart_type_on = True
                                smart_type_list = ''
                            else:
                                threading.Thread(target=lambda: play_audio_file('hello.mp3', 'turning off smart type!')).start()
                                # Create a timer to reset button color back to black after 1 second
                                threading.Timer(0.1, reset_button_color, args=(i,)).start()
                                smart_type_on = False

                        elif button_label == 'voice':
                            if not voice_on:
                                threading.Thread(target=lambda: play_audio_file('hello.mp3', 'im listening and ready to help you!')).start()
                                timer = threading.Timer(3, voice_fun)
                                timer.start()
                            else:
                                threading.Thread(target=lambda: play_audio_file('hello.mp3', 'goodbye till next time!')).start()
                                # Create a timer to reset button color back to black after 1 second
                                threading.Timer(0.1, reset_button_color, args=(i,)).start()
                        else:
                            # Create a timer to reset button color back to black after 1 second
                            threading.Timer(0.1, reset_button_color, args=(i,)).start()

    # Blit the image onto the screen
    screen.blit(image, (0, 0))

    # Draw the buttons
    for button_label, button_rect, button_color in button_rects:
        if button_color == GRAY:
            pygame.draw.rect(screen, GRAY, button_rect, border_radius=the_button_border)
        else:
            button_surface = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT), pygame.SRCALPHA)
            pygame.draw.rect(button_surface, (the_button_color[0], the_button_color[1], the_button_color[2], 0), button_rect, border_radius=the_button_border)
            pygame.draw.rect(screen, button_color, button_rect, width=3, border_radius=the_button_border)

        pygame.draw.rect(screen, color1, button_rect, border_radius=the_button_border, width=3 if button_color != GRAY else 0)
        if caps_on:
            button_label = button_label.upper()  # Convert label to uppercase if caps_on is True
        if button_label == 'smart' or button_label == 'voice' or button_label == 'scroll' or button_label == 'volume':
            text = spaciel_button_font.render(button_label, True, the_color)
        else:
            text = font.render(button_label, True, the_color)
        smart_type_text = smart_type_font.render(smart_type_list, True, the_color)
        smart_type_text_rect = smart_type_text.get_rect(x=100, y=100)
        text_rect = text.get_rect(center=button_rect.center)
        text1_rect = text1.get_rect(x=900, y=100)
        screen.blit(text, text_rect)
        if voice_on:
            screen.blit(text1, text1_rect)
        if smart_type_on:
            screen.blit(smart_type_text, smart_type_text_rect)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
