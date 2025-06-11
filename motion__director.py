import cv2  # image
import time  # delay
import imutils  # resize
# Initialize camera
cam = cv2.VideoCapture(0)  # Change to 0 if 1 doesn't work
time.sleep(1)

firstFrame = None
area = 1500  # Minimum area to detect motion

while True:
    _, img = cam.read()  # Read frame from camera
    text = "Normal"

    # Resize and convert to grayscale
    img = imutils.resize(img, width=500)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)

    # Set first frame for comparison
    if firstFrame is None:
        firstFrame = gaussianImg
        continue

    # Calculate difference between first frame and current frame
    imgDiff = cv2.absdiff(firstFrame, gaussianImg)

    # Apply threshold and dilation to highlight motion areas
    threshImg = cv2.threshold(imgDiff, 40, 255, cv2.THRESH_BINARY)[1]
    threshImg = cv2.dilate(threshImg, None, iterations=2)

    # Find contours of the moving objects
    cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # Loop through contours and draw rectangle if area is large enough
    for c in cnts:
        if cv2.contourArea(c) < area:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Moving Object detected"
        print(text)

    # Display the text on the frame
    cv2.putText(img, text, (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Show the frame
    cv2.imshow("cameraFeed", img)

    # Exit on pressing 'q'
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Release resources
cam.release()
cv2.destroyAllWindows()


