## Summary

- RNN의 구조와 작동에 대해 배워보았습니다.
- RNN에서의 Back-propagation(BPTT)을 수식적으로 살펴보았습니다.
- LSTM과 GRU의 작동방식을 알아보았습니다.
- MNIST dataset을 Bi-LSTM multi layer를 통해 분류해 보는 실습을 진행합니다.
- Gradient Clipping으로 Exploding gradient 문제를 해결할 수 있습니다.

## File

|File |Description|Folder|
|:-- |:-- |:-- |
|predict|rnn_model을 이용하여 MNIST test set에 대해 예측 및 정확성 측정 | |. |
|train| rnn_model과 gradient clipping 관련 parameter 추가 외 Ch05와 동일| | .|
|data_loader|Ch05와 동일|mnist_classification|
|trainer|gardient clipping 코드 추가 외 Ch05와 동일|mnist_classification|
|utils|Ch05와 동일|mnist_classification|
|cnn_model|Ch06와 동일|mnist_classification/models|
|fc_model|Ch05와 동일|mnist_classification/models|
|rnn_model|Bi-LSTM 4 layers 구현|mnist_classification/models|


## 새롭게 알게 된 내용

### RNN(single layer)

![Untitled](https://user-images.githubusercontent.com/55529617/108085420-a5a0bc00-70b8-11eb-9392-5cca02c5b123.png)

**Input Tensor**

NLP에서 input_size의 단어가 n개 있고, 이 한 문장이 batch_size 만큼 있다.

![Untitled 1](https://user-images.githubusercontent.com/55529617/108085400-a20d3500-70b8-11eb-8a8b-cd8c52ee67a5.png)

**Output Tensor=Hidden state Tensor**

여기서 말하는 output이란 RNN의 마지막 층의 hidden state으로 아직 linear layer와 softmax layer를 거쳐 y_hat이 되지 않은 상태를 이른다.

![Untitled 2](https://user-images.githubusercontent.com/55529617/108085403-a33e6200-70b8-11eb-9e6f-4532296f5ee4.png)

### Multi-layered RNN

![Untitled 3](https://user-images.githubusercontent.com/55529617/108085404-a33e6200-70b8-11eb-8948-ef46dbf98ba0.png)

**Input Tensor**

single layer RNN의 Input Tensor와 동일

**Output Tensor**

위 사진의 3층 layer의 hidden state이자 output

![Untitled 4](https://user-images.githubusercontent.com/55529617/108085407-a3d6f880-70b8-11eb-8a60-fbe85cd46929.png)

**Hidden state Tensor**

한 time step에 대한 Tensor 형태

![Untitled 5](https://user-images.githubusercontent.com/55529617/108085409-a46f8f00-70b8-11eb-83a0-96925d78a3f8.png)

### Bidirectional Multi-layered RNN

![Untitled 6](https://user-images.githubusercontent.com/55529617/108085411-a46f8f00-70b8-11eb-9ace-9bec481e900b.png)

**Input Tensor**

single layer RNN의 Input Tensor와 동일

**Output Tensor**

![Untitled 7](https://user-images.githubusercontent.com/55529617/108085412-a5082580-70b8-11eb-9491-dafe852bbbcf.png)

**Hidden state Tensor**

![Untitled 8](https://user-images.githubusercontent.com/55529617/108085414-a5082580-70b8-11eb-967c-0af747450a1a.png)

### RNN의 활용

1. Non autoregressive(non-generative)

현재 상태가 앞/뒤 상태를 통해 정해지는 경우→Bidirectional RNN 사용 권장

(POS Tagging, Text Classification)

2. Autoregressive(Generative)

현재 상태가 과거 상태에 의존하여 정해지는 경우→Bidirectional RNN 사용 불가

(one-to-many case, Natural Language Generation, machine Translation)

![Untitled 9](https://user-images.githubusercontent.com/55529617/108085416-a5a0bc00-70b8-11eb-9631-ba67d71ac4e2.png)

## Reference

[김기현의 딥러닝을 활용한 자연어처리 입문 올인원 패키지 Online. | 패스트캠퍼스](https://www.fastcampus.co.kr/data_online_dpnlp)
