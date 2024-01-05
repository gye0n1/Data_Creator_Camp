import os
from PIL import Image

# 이미지 파일들이 있는 디렉토리 경로
input_dir = "/Users/dgsw8th42/Desktop/데크캠/DCC_고등부_데이터셋/valid_resized/"

# 결과 이미지를 저장할 디렉토리 경로
output_dir = "/Users/dgsw8th42/Desktop/데크캠/DCC_고등부_데이터셋/new_valid_resized/"

# 새로운 크기
new_size = (128, 128)

# 입력 디렉토리 내의 모든 이미지 파일에 대해 반복
for filename in os.listdir(input_dir):
    print(filename)
    f = input_dir + filename
    try:
        eachFolder = os.listdir(f)
        for file in eachFolder:
            try:
                input_path = os.path.join(f, file)
                img = Image.open(input_path)
                resized_img = img.resize((128, 128))
                output_filename = file.split('.')[0] + "_축소.jpg"  # 결과 이미지 파일 이름 변경
                output_path = os.path.join(output_dir, output_filename)
                resized_img.save(output_path)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)