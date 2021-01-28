## [Summary]

- dataset과 dataloader를 통해 이전 data_loader 파일에서 구현했던 데이터 split, 전처리, shuffle+mini batch 구현을 더 간단히 해볼 수 있었다.
- PyTorch Ignite을 통해 짧고 간단하면서도 여러 모델 또는 상황에 적용 가능한 Boilerplate을 만들 수 있었다.

## [File]

|File |Description |
|:-- |:-- |
|custom_dataset_practice |dataset, dataloader을 이용해 이진분류 실습 |
|data_loader |MNIST dataset, load_mnist, get_loader을 이용해 train/valid/test set 분할 및 mini batch 만듦 |
|model | LeakyReLU, BatchNorm, softmax를 사용한 DNN|
|train |argparser, main 함수로 신경망의 학습을 시작 |
|trainer | PyTorch Ignite으로 구현되어 process function과 동작순서가 저장|
|utils|parameter, gradienr의 L2 norm을 구하는 함수 |

## [새롭게 알게 된 내용들]

기존에 신경망을 구현할 때, 표준적으로 사용하는 파일이 아래와 같다.

이번 쳅터에서는 각 파일은 같지만, 몇몇 파일의 안의 구성이 달라졌는데, 아래와 같은 변경이 있었다.

- Data Loader : dataset, dataloader를 활용
- Trainer : Ignite을 이용하여 체계적으로 코드 구현

![KakaoTalk_20210128_172516478](https://user-images.githubusercontent.com/55529617/106111457-5fc69700-618f-11eb-8d99-dc8a0238c7b9.jpg)

PyTorch의 Ignite이 어떻게 동작하는지를 요약한 그림으로,

 빨간색 : event로 일종의 스위치로 껐다 켰다 할 수 있음

초록색 : process function, 직접 우리가 코드를 작성해 주어야 하는 부분으로 한 번 작성하면 재사용 가능

(참고로, 1번의 epoch 동안 일어나는 일들이다.)

![KakaoTalk_20210128_172516015](https://user-images.githubusercontent.com/55529617/106111459-605f2d80-618f-11eb-851e-8b46bb017011.jpg)

순서를 나타낸 표로,

1. dataset에서 data를 적재하고, dataloader를 통해 mini batch와 shuffle 옵션을 설정
2. Train engine에 train data를 넣고, 일련의 process를 거친 뒤, 중간과정을 확인하기 위한 loss, p_norm 등을 출력한다.
3. 1번의 epoch이 끝난 뒤, validation set을 Validation engine에 넣어 일련의 process를 거친 뒤, 마찬가지로 중간과정을 확인하기 위한 loss, p_norm 등을 출력한다.
4. 이 외에도 loss를 이전것과 비교하여 best loss를 갱신하고, 학습한 model의 파라미터들을 저장한다.

(훈련시킨 모델을 이용해 Test set을 평가하는 과정은 따로 해준다.)

![KakaoTalk_20210128_172516202](https://user-images.githubusercontent.com/55529617/106111460-60f7c400-618f-11eb-9e0f-43bc26c8110d.jpg)

## Reference

[김기현의 딥러닝을 활용한 자연어처리 입문 올인원 패키지 Online. | 패스트캠퍼스](https://www.fastcampus.co.kr/data_online_dpnlp)


