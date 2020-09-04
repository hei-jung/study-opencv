import cv2

img1 = cv2.imread('star.png')  # 배경이 검정색인 별 이미지(그림판에서 직접 그림)
img2 = cv2.imread('cat1.jpg')  # 고양이 이미지(구글검색)

row, col, ch = img1.shape  # 별 이미지의 세로길이, 가로길이, 채널개수 가져오기

roi = img2[0:row, 0:col]  # roi: 고양이 이미지의 (0,0)에서 (row,col)까지의 영역

img2gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  # 별 이미지를 흑백으로
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)  # 배경 추출용 마스크
#cv2.imshow('mask', mask)  # 확인 코드
mask_inv = cv2.bitwise_not(mask)  # 마스크 반전시켜서 내용물(별 모양) 추출
#cv2.imshow('mask_inv', mask_inv)  # 확인 코드

img1_fg = cv2.bitwise_and(img1, img1, mask=mask)  # 별과 배경을 and 연산 ---> 별만 따옴
#cv2.imshow('fg', img1_fg)  # 확인 코드
img2_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)  # 별 마스크를 갖다붙일 영역에 반전 마스크와 and 연산 ---> 별 모양만큼 빠지게 됨
#cv2.imshow('bg', img2_bg)  # 확인 코드

# dst에 별과 배경을 합쳐놓는다
dst = cv2.add(img1_fg, img2_bg)
img2[0:row, 0:col] = dst

# 결과창
cv2.imshow('res', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
