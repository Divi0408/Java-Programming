import cv2
import time
import os

language = "EN"
gesture = "NO HAND"
sentence = []

last_time = 0

def speak(text):
    global last_time

    # prevent overlapping speech
    if time.time() - last_time < 1.2:
        return

    try:
        os.system(f'say "{text}"')
        last_time = time.time()
    except:
        pass


def build_sentence(lang, words):
    if lang == "EN":
        return "I need water"

    # Tamil (phonetic + correct order)
    if "I" in words and "WATER" in words:
        return "ENNAKU THANEER VENDUM"
    elif "I" in words:
        return "ENNAKU VENDUM"
    elif "WATER" in words:
        return "THANEER VENDUM"

    return " ".join(words)


# ---------------- CAMERA ----------------
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)

    # ---------------- UI ----------------
    if language == "EN":
        display_sentence = "I need water"
    else:
        display_sentence = build_sentence(language, sentence)

    cv2.putText(frame,
                "1=I | 2=NEED | 3=WATER | 4=SPEAK | L=LANG | q=QUIT",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2)

    cv2.putText(frame,
                f"Gesture: {gesture}",
                (50, 120),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.2,
                (0, 255, 0),
                3)

    cv2.putText(frame,
                f"Sentence: {display_sentence}",
                (50, 180),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 200, 255),
                2)

    cv2.putText(frame,
                f"Language: {language}",
                (50, 230),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 200, 0),
                2)

    cv2.imshow("SABDHA FINAL PROTOTYPE", frame)

    key = cv2.waitKey(1) & 0xFF

    # ---------------- INPUT ----------------
    if key == ord('1'):
        gesture = "I"
        sentence.append("I")

    elif key == ord('2'):
        gesture = "NEED"
        sentence.append("NEED")

    elif key == ord('3'):
        gesture = "WATER"
        sentence.append("WATER")

    # ---------------- LANGUAGE TOGGLE ----------------
    elif key == ord('l'):
        language = "TA" if language == "EN" else "EN"

    # ---------------- SPEAK SENTENCE ----------------
    elif key == ord('4'):
        gesture = "SENTENCE"

        if language == "EN":
            full_sentence = "I need water"
        else:
            full_sentence = build_sentence(language, sentence)

        speak(full_sentence)

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()