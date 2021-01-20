# Ch02_Representation learning

## [Summary]

- feature란 샘플을 잘 설명하는 특징으로 머신러닝에서 feature vector를 이용
- categorical value를 사용하기 위해 one-hot encoding을 사용,하지만 더 많은 정보를 포함하기 위해 NLP에서는 차원 축소 및 dense vector로 표현하기도 함
- Autoencoder는 encoder와 decoder를 통해 압축과 해제(복원)를 실행하면서 특징 추출을 자동으로 학습
- Hidden layer에서 나온 모든 결과물을 feature vector라 볼 수 있지만 해석이 어렵기 때문에 bottleneck(encoder의 output)에서 나온 feature vector를 이용해 압축된/정제된 feature를 볼 수 있음
- 이러한 압축된/정제된 feature의 집합을 latent space라 함

## [File]

|File |Description|
|:-- |:-- |
|model.py| autoencoder의 encoder과 decoder 구조를 짜 놓은 파일 |
|trainer.py| Ch01에서 구현한 trainer.py와 동일한 파일, train set과 valid set에 대해서 모델을 훈련|
|utils.py| Ch01에서 구현한 utils.py와 동일한 파일, 데이터를 로드|
|autoencoder_practice.ipynb| model, trainer, utils를 이용해 autoencoder 동작시키고 Latent Space를시각화|

## [새롭게 알게 된 내용들]

인코더에 MNIST dataset을 입력하여 얻은 결과물을 plot으로 그렸을 때, 비슷한 샘플들은 비슷한 곳에 위치함을 확인할 수 있었다.(btl_size=2) 이 때, 이 plot이 뿌려진 공간을 hidden(latent) space라고 부른다.

달리 말하자면 Input space의 MNIST 샘플이 latent space에 embedding 된 것이다.

![캡처](https://user-images.githubusercontent.com/55529617/105206814-2045ec80-5b8a-11eb-834a-a14e2fd2805b.PNG)
