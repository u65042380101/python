import cv2
import math
from cvzone.HandTrackingModule import HandDetector
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# เปิดกล้อง
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

# ตั้งค่าควบคุมเสียง
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# กำหนดระยะที่ใช้ในการปรับเสียง
min_distance = 20
max_distance = 180

while True:
    success, img = cap.read()
    if not success:
        continue

    hands, img = detector.findHands(img)
    
    if hands:
        hand = hands[0]
        hand_type = hand["type"]  # ตรวจสอบว่าเป็นมือซ้ายหรือขวา
        thumb_tip = hand["lmList"][4]
        index_tip = hand["lmList"][8]

        # คำนวณระยะห่างระหว่างปลายนิ้วโป้งและนิ้วชี้
        distance = math.hypot(thumb_tip[0] - index_tip[0], thumb_tip[1] - index_tip[1])
        distance = max(min_distance, min(distance, max_distance))

        # คำนวณสเกลเสียง
        volume_scalar = (distance - min_distance) / (max_distance - min_distance)
        volume.SetMasterVolumeLevelScalar(volume_scalar, None)

        # คำนวณเปอร์เซ็นต์เสียง
        volume_percent = int(volume_scalar * 100)

        # วาดเส้นระหว่างนิ้วโป้งและนิ้วชี้
        color = (0, 255, 0) if hand_type == "Right" else (255, 0, 0)  # มือขวา = เขียว, มือซ้าย = น้ำเงิน
        cv2.line(img, (thumb_tip[0], thumb_tip[1]), (index_tip[0], index_tip[1]), color, 3)

        # แสดงค่าเปอร์เซ็นต์เสียงบนหน้าจอ
        position = (50, 50) if hand_type == "Right" else (50, 100)  # มือซ้ายแสดงที่ตำแหน่งต่ำกว่า
        cv2.putText(img, f'Volume: {volume_percent}%', position,
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    # แสดงผล
    img = cv2.resize(img, (960, 720))
    cv2.imshow("Image", img)

    # กด 'q' เพื่อออกจากโปรแกรม
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
