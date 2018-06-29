import cv2
import os
import numpy as np
import time

input_path = "D:\jifuku\M2\image proccesing\Binary\sample"
file_number = 2


for i in range(int(file_number)):
    input_file = str(i) + ".mp4"
    print("動画の名前 %s" % input_file)
    # 動画の読み込み。ここで指定したインスタンスが以降の動画操作系のコマンドに継承されていく
    cap = cv2.VideoCapture(input_file)
    # スクリーンキャプチャを保存するdirectory設定
    dir_name = "frame"

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    save_path = os.path.join(input_path, dir_name)

    # 総フレーム数、フレームレートの確認
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(5)

# 一つ目の変数にはフレームが読み込まれているかの確認。
# 二つ目の変数には画像の配列が格納される
ret, frame = cap.read()

# 読み込んだ動画の情報および一枚目を出力
print("フレーム数")
print(frame_count)
print("フレームレート")
print(fps)
print("--------------------------------------------------")
save_name = str(save_path) + "/" + str(i) + ".png"
cv2.imwrite(save_name, frame)
