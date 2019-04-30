import cv2
import argparse

def get_video_in(in_file=None):
    if in_file is None:
        cap = cv2.VideoCapture(0)
    else:
        cap = cv2.VideoCapture(in_file)

    return cap

def draw(frame, obj):
    for (x, y, w, h) in obj:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.putText(frame, f"Objects Detected: {len(obj)}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

def go(in_file=None):

    cap = get_video_in(in_file)

    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    while True:
        if not cap.isOpened():
            print('Unable to load camera.')
            time.sleep(2)
            pass

        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        draw(frame, faces)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=False, help="Path to input file")

    args = vars(ap.parse_args())

    print(args)

    go(args['input'])
