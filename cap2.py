import cv2
import numpy as np
import pyautogui
import time

cap = cv2.VideoCapture(0)
counter = 1



while True:
    success, img = cap.read()
    if not success:
        break
    cv2.imshow("img", img)
    
    k = cv2.waitKey(1)
    
    if k == 27:  # Exit if 'Esc' key is pressed
        break
    elif k == ord('s'):  # Save image if 's' key is pressed
        pyautogui.press('s')
        filename = f"image{counter}.jpg"
        cv2.imwrite(filename, img)
        print(f"Saved {filename}")
        counter += 1  # Increment the counter for the next image
        

cap.release()
cv2.destroyAllWindows()
