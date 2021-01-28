## [Summary]

- Convolution layer에서 합성곱 연산과 특징에 대해 배워봅니다.
- data reduction의 방식으로 Max-pooling과 Stride에 대해 배워봅니다.
- 기존의 신경망 구조에서 model에서 CNN 구조를 추가하여 MNIST data 실습을 진행합니다.

## [파일]

실무에서 사용하듯이 directory를 고려합니다.

|File |Description |Folder|
|:-- |:-- |
|predict |CNN으로 MNIST test data 평가 |. |
|train |get_model이라는 cnn, fc 선택 함수가 추가된 Ch05의 train 파일 |. |
|model.pth |훈련된 모델의 파라미터 |. |
|data_loader |Ch05와 동일 | mnist_calssification|
|trainer |Ch05와 동일 |mnist_calssification|
|utils |Ch05와 동일 |mnist_calssification|
|cnn_model|convolutional block 5개(10층)와 Fc layer 2층, softmax로 출력층을 사용한 모델|mnist_classification/models |
|fc_model|Ch05와 동일 |mnist_classification/models | 

## [새롭게 알게 된 내용]

### Convolution Layer의 특징

- Feature의 위치에 구애받지 않는다.

    즉, FC layer에서는 같은 2이더라도 이미지 상에서 2의 위치가 달라지면 다른 것으로 인지를 하게 되는데, Convolution layer에서는 합성곱 연산을 이용하므로 feature가 어디에 있든 구애받지 않는다.

    (참고 : CNN은 데이터셋의 x와 y의 구성에 따라 자동으로 탐지해야 할 패턴을 추출한다. 따라서 내부 kernel은 해당 패턴을 추출하기 위한 형태로 자동으로 구성된다. )

![KakaoTalk_20210128_225208102](https://user-images.githubusercontent.com/55529617/106149688-e6926880-61bd-11eb-879e-7cd03028fa53.jpg)

- 같은 입출력을 갖는 FC Layer에 비해 더 적은 weight을 가진다.

    아래 예시를 보면, Convolutional layer는 9개의 weight이 필요하지만, FC layer에서는 64개의 weight이 필요한 것을 알 수 있다.

![KakaoTalk_20210128_225225973](https://user-images.githubusercontent.com/55529617/106149694-e7c39580-61bd-11eb-8808-ecf29f728550.jpg)

- 병렬 계산 구성이 쉬우므로 GPU에서의 연산이 매우 빠르다.
- 단점 : FC Layer에 비해 입출력 크기가 계산이 까다로워, 네트워크 구성이 쉽지 않다.

### CNN Architecture

CNN block을 다음 7가지로 구성한 뒤, CNN block을 잇고, 마지막으로 FC layer와 softmax를 이용해 결과를 출력하는 형태이다.

![KakaoTalk_20210128_225649765](https://user-images.githubusercontent.com/55529617/106149697-e7c39580-61bd-11eb-8bab-e7fdd9f2b565.jpg)
