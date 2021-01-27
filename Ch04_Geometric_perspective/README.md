## [Summary]

**After this class,**

- Objective : 세상에 존재하는 어떤 미지의 확률 분포 함수를 모사(approximate) 하자.

- Probabilistic Perspective
    - 확률 분포  P(x)와 P(y|x)로부터 데이터를 수집하여,
    - 해당 데이터를 가장 잘 설명하는 확률 분포 함수의 파라미터를 찾자 : log P(y|x; seta)
        - Maximum Likelihood Estimation
        - Gradient Descent using Back-propagation
    - 또는 두 확률 분포를 비슷하게 만들자.
        - Minimize Cross Entropy(or KL-Divergence)

- Geometric Perspective
    - 데이터란 저차원의 manifold에 분포하고 있으며, 여기에 약간의 노이즈가 추가되어 있는 것

        노이즈란 task(x→y)에 따라서 다양하게 해석 가능할 것

    - 따라서 해당 manifold를 배울 수 있다면, 더 낮은 차원으로 효율적인 맵핑(or project)이 가능

        Non-linear dimension reduction

- Representation Learning, Again

    낮은 차원으로의 표현을 통해, 차원의 저주(curse of dimensionality)를 벗어나 효과적인 학습이 가능

## [파일]
|File|Description|
|:-- |:-- |
|manifold_practice |model, trainer, utils를 이용해 manifold 실습 |
|model| Ch02의 autoencoder의 encoder과 decoder 구조를 짜 놓은 파일 |
|trainer|Ch01에서 구현한 trainer.py와 동일한 파일, train set과 valid set에 대해서 모델을 훈련 |
|utils|Ch01에서 구현한 utils.py와 동일한 파일, 데이터를 로드 |


## Reference

[김기현의 딥러닝을 활용한 자연어처리 입문 올인원 패키지 Online. | 패스트캠퍼스](https://www.fastcampus.co.kr/data_online_dpnlp)






