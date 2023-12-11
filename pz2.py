import cv2
import numpy as np
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#Выбираем один из трех методов
print ('Выберите фильтр')
print ('1 - Сегментирование объекта с помощью гистограммы')
print ('2 - Фильтр Кэнни')
print ('3 - Метод вычитания')
M=int(input())
###################################################################################################################################################################
if M==3:
    while True:
        #Обработка видео
        ret, frame = cap.read()
        if not ret:
            break
        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #Размываем с помощью метода Гаусса
        blurred = cv2.GaussianBlur( hsv_image, (49, 49), 0)
        #Вычитаем размытое изображение из исходного чтобы установить границы
        edges_subtraction =  hsv_image - blurred
        cv2.imshow('Method3', edges_subtraction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
###################################################################################################################################################################
if M==1:
    while True:
        #Обработка видео:
        ret, frame = cap.read() 
        if not ret:
            break
        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #Вычисляем гистограмму, определяем минимум, максимум, пороговое значение
        h_channel = hsv_image[:, :, 0]
        hist_h = cv2.calcHist([h_channel], [0], None, [256], [0, 256])
        min_peak = np.argmin(hist_h)
        max_peak = np.argmax(hist_h)
        _, binary_image = cv2.threshold(h_channel, min_peak, max_peak, cv2.THRESH_BINARY)
        cv2.imshow('Method1', binary_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
###################################################################################################################################################################
if M==2:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #Размываем с помощью метода Гаусса
        blurred = cv2.GaussianBlur(hsv_image, (19, 19), 0)
        #Фильтр Кэнни для размытия границ
        edges = cv2.Canny(blurred, 100, 300)
        cv2.imshow('Method2', edges)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
##################################################################################################################################################
#Закрываем видео и окна
cap.release()
cv2.destroyAllWindows()

