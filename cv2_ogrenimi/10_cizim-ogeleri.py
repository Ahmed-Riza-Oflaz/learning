import cv2
import numpy as np

###################--çizim şekillerini anlamak--########################

canvas = np.zeros((512,512,3), dtype=np.uint8 )

                    #canvas tuvalin ingilizcesidir ve buradaki görevi adeta çizim tahtası hükmünde

                    # dtype=np.uint8 çizim için kullandığımız modüldür


cv2.line(canvas, (50,50), (512,512), (255,0,0), thickness=5 )

                    #Bu kod, cv2.line() fonksiyonunu kullanarak bir çizgi oluşturur ve bu çizgiyi belirtilen renkte ve kalınlıkta verilen bir görüntü üzerine çizer. 

                    #cv2.line(): Bu fonksiyon, bir görüntü üzerine bir çizgi çizmek için kullanılır.

                    #canvas: Çizginin çizileceği görüntüdür. Bu, genellikle bir NumPy dizisi olarak temsil edilir.

                    #(50,50): Çizginin başlangıç noktasını belirtir. Bu durumda, çizginin başlangıç noktası (50, 50) koordinatlarındadır.

                    #(512,512): Çizginin bitiş noktasını belirtir. Bu durumda, çizginin bitiş noktası (512, 512) koordinatlarındadır.

                    #(255,0,0): Çizginin rengini belirtir. Bu durumda, çizgi mavi renkte olacaktır. Renk kodları RGB (Red, Green, Blue) formatında üç tamsayıdan oluşur. Burada (255, 0, 0) mavi rengi temsil eder.

                    #thickness: Çizginin kalınlığını belirtir. Bu durumda, çizgi 5 piksel kalınlığında olacaktır.


cv2.line(canvas, (100,50), (200,250), (0,0,255), thickness=5 )






cv2.rectangle(canvas, (20,20),(50,50),(0,255,0), thickness=-1 )

                    #Bu kod, cv2.rectangle() fonksiyonunu kullanarak bir dikdörtgen oluşturur ve bu dikdörtgeni belirtilen renkte ve belirli kalınlıkta verilen bir görüntü üzerine çizer. 

                    #cv2.rectangle(): Bu fonksiyon, bir görüntü üzerine bir dikdörtgen çizmek için kullanılır.

                    #(20,20): Dikdörtgenin sol üst köşesinin koordinatlarını belirtir.
                    
                    #(50,50): Dikdörtgenin sağ alt köşesinin koordinatlarını belirtir.

                    #thickness: Dikdörtgenin kenar kalınlığını belirtir. Negatif bir değer kullanıldığında (thickness=-1), dikdörtgenin içini doldurur.

                    #Bu kod, (20,20) ve (50,50) koordinatları arasında yeşil renkte bir dikdörtgen çizer. Dikdörtgenin içi, thickness=-1 parametresi sayesinde dolu (solid) olarak doldurulur. Bu şekilde, dikdörtgenin içi tamamen renklendirilmiş olur.

cv2.rectangle(canvas, (50,50),(150,150),(0,255,0), thickness=-1 )



cv2.circle(canvas, (250,250), 100, (0,0,255), thickness=-1 )

                    #Bu kod, cv2.circle() fonksiyonunu kullanarak bir daire oluşturur ve bu daireyi belirtilen renkte ve belirli kalınlıkta verilen bir görüntü üzerine çizer.

                    #cv2.circle(): Bu fonksiyon, bir görüntü üzerine bir daire çizmek için kullanılır.

                    #(250,250): Dairenin merkez noktasının koordinatlarını belirtir.

                    #100: Dairenin yarıçapını belirtir.

                    #(0,0,255): Dairenin rengini belirtir. Bu durumda, daire kırmızı renkte olacaktır. Renk kodları RGB (Red, Green, Blue) formatında üç tamsayıdan oluşur. Burada (0, 0, 255) kırmızı rengi temsil eder.

                    #thickness: Dairenin kenar kalınlığını belirtir. Negatif bir değer kullanıldığında (thickness=-1), dairenin içini doldurur.

                    #Bu kod, (250,250) merkez noktası ve 100 piksel yarıçapı olan bir kırmızı daire çizer. Dairenin içi, thickness=-1 parametresi sayesinde dolu (solid) olarak doldurulur. Bu şekilde, dairenin içi tamamen renklendirilmiş olur.


canvas1 = np.zeros((512,512,3), dtype=np.uint8 ) + 255


p1 = (100,200)
p2 = (50,50)
p3 = (300,300)

cv2.line(canvas1, p1, p2, (0,0,0), 4)
cv2.line(canvas1, p2, p3, (0,0,0), 4)
cv2.line(canvas1, p1, p3, (0,0,0), 4)

                    #Bu kod parçası, üç farklı nokta arasında çizgiler oluşturarak bir üçgen çizer. İlgili kodları açıklayalım:

                    #p1, p2 ve p3 adında üç farklı nokta tanımlanır. Bu noktalar, üçgenin üç köşesini temsil eder.

                    #cv2.line() fonksiyonu, iki nokta arasında bir çizgi oluşturur. Bu durumda, üçgenin kenarlarını oluşturmak için üç farklı çizgi çizilir.

                    #İlk çizgi, p1 ve p2 noktaları arasında çizilir.

                    #İkinci çizgi, p2 ve p3 noktaları arasında çizilir.

                    #Üçüncü çizgi, p1 ve p3 noktaları arasında çizilir.

                    #Her çizgi, siyah renkte ve kalınlığı 4 piksel olan bir çizgi oluşturur.

                    #Bu işlem sonucunda, üç farklı çizgi çizilir ve bu çizgilerin birleşimiyle bir üçgen oluşturulur.

                    #Bu kod parçası, üç farklı nokta arasında çizgiler çizerek bir üçgen oluşturur ve bu üçgeni bir görüntü üzerine çizer.


                # üçgen çizmek için birçok yol bulunur bir diğer yol ise


points = np.array([[100, 400], [300, 100], [500, 400]], np.int32)

                    #np.array(): Bu fonksiyon, bir NumPy dizisi oluşturmak için kullanılır. Bu dizinin elemanları, belirli bir veri tipiyle birlikte belirtilen bir liste veya başka bir dizi olabilir.

                    #[[100, 400], [300, 100], [500, 400]]: Bu, üçgenin köşe noktalarını içeren bir liste. Her bir iç liste, bir köşenin x ve y koordinatlarını içerir. Bu örnekte, üç farklı köşenin koordinatları belirtilmiştir.

                    #np.int32: Bu, dizinin veri tipini belirtir. Bu durumda, tamsayıların 32-bitlik bir türü olan np.int32 kullanılır. Bu, koordinatların tamsayı değerlerini temsil eder.


cv2.polylines(canvas1, [points], isClosed=True, color=(0,255,0), thickness=3)

                    #Bu kod, cv2.polylines() işlevini kullanarak bir çokgen çizer. İlgili parametreleri açıklayalım:

                    #cv2.polylines(): Bu işlev, bir görüntü üzerine bir veya daha fazla çokgen çizmek için kullanılır.

                    #canvas1: Çokgenin çizileceği görüntüdür. Bu, genellikle bir NumPy dizisi olarak temsil edilir.

                    #[points]: Çokgenin köşe noktalarını içeren bir listeyi alır. Bu durumda, points adında bir listeyi alır. points, üçgenin köşe noktalarını içeren bir NumPy dizisidir.

                    #isClosed=True: Bu, çokgenin kapalı bir şekilde mi çizileceğini belirler. Üçgen gibi kapalı bir şekil çiziyorsak, bu parametre True olarak ayarlanır.

                    #color=(0,255,0): Çokgenin rengini belirtir. Bu durumda, yeşil renkte bir çokgen çizilir. Renk kodları RGB (Red, Green, Blue) formatında üç tamsayıdan oluşur. Burada (0, 255, 0) yeşil rengi temsil eder.

                    #thickness=3: Çokgenin kenar kalınlığını belirtir. Bu durumda, çokgenin kenarları 3 piksel kalınlığında çizilir.

                    #Bu kod satırı, points dizisinde belirtilen köşe noktalarıyla bir üçgen çizer ve bu üçgeni yeşil renkte ve 3 piksel kalınlığında bir çizgiyle bir görüntü üzerine çizer.


canvas2 = np.zeros((512,512,3), dtype=np.uint8 )

points1 = np.array([[[110, 200], [330, 200], [290,220] ,[100, 100]]], np.int32)

cv2.polylines(canvas2, [points1], isClosed=True, color=(0,255,0), thickness=3)

                    #Bu kod parçası, daha karmaşık bir çokgenin köşe noktalarını içeren bir NumPy dizisi oluşturur ve bu çokgeni çizer. İlgili parametreleri açıklayalım:

                    #np.array(): Bu fonksiyon, bir NumPy dizisi oluşturmak için kullanılır.

                    #isClosed=True parametresi, çizilen çokgenin kapalı bir şekilde mi çizileceğini belirtir. Kapalı bir şekilde çizilen bir çokgen, son köşe noktası ile ilk köşe noktası arasında bir çizgiyle tamamlanır. Bu parametrenin True olarak ayarlanması, çokgenin kapalı bir şekilde çizileceğini belirtir.

                    #[[[110, 200], [330, 200], [290,220] ,[100, 100]]]: Bu, çokgenin köşe noktalarını içeren bir liste. Her bir iç liste, bir köşenin x ve y koordinatlarını içerir. Bu örnekte, dört farklı köşenin koordinatları belirtilmiştir.

                    #np.int32: Bu, dizinin veri tipini belirtir. Bu durumda, tamsayıların 32-bitlik bir türü olan np.int32 kullanılır. Bu, koordinatların tamsayı değerlerini temsil eder.

                    #Bu kod parçası, karmaşık bir çokgenin köşe noktalarını içeren bir NumPy dizisi oluşturur ve bu çokgeni cv2.polylines() işlevini kullanarak bir görüntü üzerine çizer. Çokgenin köşe noktalarını belirtmek için points1 dizisi kullanılır. Çokgenin rengi yeşil olarak belirlenmiş ve kenar kalınlığı 3 piksel olarak ayarlanmıştır.


cv2.ellipse(canvas2, (300,300), (80,20), 10, 900, 360, (255,255,0), -1 )

                    #Bu kod, cv2.ellipse() işlevini kullanarak bir elips oluşturur ve bu elipsi belirtilen renkte ve belirli kalınlıkta bir görüntü üzerine çizer. İlgili parametreleri açıklayalım:

                    #cv2.ellipse(): Bu işlev, bir görüntü üzerine bir elips çizmek için kullanılır.

                    #canvas2: Elipsin çizileceği görüntüdür. Bu, genellikle bir NumPy dizisi olarak temsil edilir.

                    #(300,300): Elipsin merkez noktasının koordinatlarını belirtir.

                    #(80,20): Elipsin uzunluğunu ve genişliğini belirtir. Bu, bir tuple olarak verilir. İlk değer, elipsin yarı uzunluğunu, ikinci değer ise elipsin yarı genişliğini belirtir.

                    #10: Elipsin eğim açısını belirtir.

                    #900, 360: Bu, elipsin çizim açısını belirtir. İlk değer başlangıç açısını, ikinci değer ise bitiş açısını belirtir.

                    #(255,255,0): Elipsin rengini belirtir. Bu durumda, elips sarı renkte olacaktır. Renk kodları RGB (Red, Green, Blue) formatında üç tamsayıdan oluşur. Burada (255, 255, 0) sarı rengi temsil eder.

                    #-1: Elipsin doluluk derecesini belirtir. Negatif bir değer kullanıldığında (-1), elipsin içi dolu (solid) olur.


                    #Bu kod, (300,300) merkez noktası, 80 birim yarı uzunluğu, 20 birim yarı genişliği olan ve eğim açısı 10 derece olan bir sarı renkli elipsi, belirtilen görüntü üzerine çizer. Elipsin içi dolu (solid) olarak çizilir.



cv2.imshow("canvas2", canvas2)

cv2.imshow("canvas1",canvas1)

cv2.imshow("canvas", canvas )


cv2.waitKey(0)
cv2.destroyAllWindows()