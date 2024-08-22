import cv2
import pytesseract
import os
import re

pytesseract.pytesseract.tesseract_cmd = r'D:\\Tesseract OCR\\tesseract.exe'

save_directory = r'D:\\useless'
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

soluongcamtruycap = cv2.VideoCapture(0)
image_counter = 1 

while True:
    ret, frame = soluongcamtruycap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    text = pytesseract.image_to_string(thresh, config='--psm 6')
    print("Text detected:", text)  

    if re.match(r'^\d+(\.\d+)?$', text.strip()):
        image_path = os.path.join(save_directory, f'image{image_counter}.jpg')
        cv2.imwrite(image_path, frame)  
        print(f'Đã lưu ảnh: {image_path}')
        break  

    cv2.imshow("Cửa sổ camera", frame)
    if cv2.waitKey(1) == ord("q"):
        break

soluongcamtruycap.release()
cv2.destroyAllWindows()
