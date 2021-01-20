# Ch01_MNIST classification

## Summary

선수강 과목인 "PyTorch로 배우는 딥러닝 입문"의 내용 중 MNIST Classification 구현을 복습하는 강의이다.  
실무에서 아래 사진과 같이 코드를 짜며 실제로 여러 class를 통해 짜임새 있게 코드를 쓰는 법을 배울 수 있었다.  

![KakaoTalk_20210119_000212051](https://user-images.githubusercontent.com/55529617/104931373-a7a82a00-59e9-11eb-9c7b-77c7107515cb.jpg)


## File

### model

| Fn | Description |
|:-- |:-- |
| __init__ | input_size, output_size를 인수로 받아 nn.Sequential을 쌓음|
| forward | __init__에서 쌓은 모델에 입력데이터를 넣어서 output을 얻는 순전파 과정|

### trainer

| Fn | Description |
|:-- |:-- |
| __init__ | model, optimizer, crit를 인수로 받음 |
| _train | train data를 shuffle+batch size로 나눔, 그리고 한 epoch에 대한 평균 손실을 구함|
| _validate | valid data를 shuffle+batch size로 나눔, 그리고 한 epoch에 대한 평균 손실을 구함|
| train | _train, _validate를 이용하여 최적의 모델을 선정하고 매개변수를 저장|


### train

| Fn | Description |
|:-- |:-- |
| define_argparser | cmd 명령어 설정 및 gpu 여부, batch_size 등의 하이퍼파라미터 설정 |
| main | model과 trainer를 불러와 모델의 훈련을 담당하고 훈련된 모델은 저장|


### utils

| Fn | Description |
|:-- |:-- |
| load_mnist| MNIST dataset에서 신경망의 구조에 맞게 data를 변형하여 가져오는 함수 |

### predict

| Fn | Description |
|:-- |:-- |
| load | 훈련이 끝나 저장된 모델에 접근하는 함수|
| plot| MNIST data를 이미지로 보여주는 함수|
| test| model의 accuracy를 측정하고, plot을 이용해 이미지를 보여주는 함수|

## Reference

[김기현의 딥러닝을 활용한 자연어처리 입문 올인원 패키지 Online. | 패스트캠퍼스](https://www.fastcampus.co.kr/data_online_dpnlp)











