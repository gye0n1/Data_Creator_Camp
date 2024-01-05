import os
image_extensions = ['.jpg']
path = '/Users/dgsw8th42/Desktop/DCC_고등부_데이터셋/train_resized'

# 총 이미지 파일 수를 저장할 변수
total_image_count = 0

# 디렉토리 내의 모든 파일, 하위 디렉토리 검색
for root, dirs, files in os.walk(path):
    for file in files:
        if file.split(".")[-2].split("_")[-1] == "01":
            total_image_count += 1

# 결과
print(f"0000부터 2399까지의 파일에 있는 01로 끝나는 이미지 파일의 총 수: {total_image_count}")