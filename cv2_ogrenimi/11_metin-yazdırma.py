import cv2
import numpy as np

canvas = np.zeros((512,512,3), dtype=np.uint8 ) + 255

font1 = cv2.FONT_HERSHEY_SIMPLEX


font2 = cv2.FONT_HERSHEY_SIMPLEX # Basit düz bir yazı tipi.

font3 = cv2.FONT_HERSHEY_PLAIN  # Basit tip, fontun kalınlığına sahip değil.

font4 = cv2.FONT_HERSHEY_DUPLEX  # Düz yazı tipi (çift genişlikli).

font5 = cv2.FONT_HERSHEY_COMPLEX  # Karmaşık bir yazı tipi.

font6 = cv2.FONT_HERSHEY_TRIPLEX  # Üçlü genişlikli yazı tipi.

font7 = cv2.FONT_HERSHEY_COMPLEX_SMALL  # Küçük boyutta karmaşık bir yazı tipi.

font8 = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX  # Basit bir el yazısı tarzı.

font9 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX  # Karmaşık bir el yazısı tarzı.



cv2.putText(canvas, "OpenCV", (15,260), font1, 4, (0,0,0), cv2.LINE_AA )

                # canvas: Metnin yazılacağı görüntü.

                # "OpenCV": Yazılacak metin.

                # (15, 260): Metnin konumu, sol üst köşesinin (x, y) koordinatları.

                # font1: Kullanılacak yazı tipi.

                # 4: Yazı boyutu.

                # (0, 0, 0): Metnin rengi. Bu, (B, G, R) renk kanallarının sırasıyla 0-255 aralığında tamsayı değerleridir.

                # cv2.LINE_AA: Düzgün bir çizgi ile yazı yazmayı sağlayan anti-aliasing (kenar yumuşatma) tipi.

cv2.imshow("canvas", canvas )

cv2.waitKey(0)

cv2.destroyAllWindows()