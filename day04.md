
# Day 4 정리

## ROS Action
### 1. ROS Action이란
```bash
ROS Action은 **시간이 오래 걸리는 작업을 처리하기 위한 통신 방식**이다.

예를 들어

- 로봇이 목적지까지 이동
- 물체를 집는 작업
- 긴 계산 작업

같이 오래 걸리는 작업을 수행할 때 사용한다.
```
```bash
Action은 다음과 같은 특징이 있다.

- 작업 진행 상태를 확인할 수 있다 (Feedback)
- 작업을 취소할 수 있다 (Cancel)
- 작업이 완료되면 결과를 받을 수 있다 (Result)
```
---

### 2. Topic / Service / Action 차이
```bash
| 통신 방식 | 특징 |
|---|---|
| Topic | 지속적인 데이터 전달 |
| Service | 요청 → 응답 구조 |
| Action | 시간이 오래 걸리는 작업 처리 |
```
---

### 3. Action 구조
```bash
Action은 다음과 같은 구조로 이루어져 있다.
Client
│
│ Goal 요청
▼
Server
│
├ Feedback (진행 상황)
│
▼
Result (완료 결과)

구성 요소
- Goal : 클라이언트가 요청하는 작업
- Feedback : 작업 진행 상태
- Result : 작업 완료 후 결과
```
---

## TimeServer

### 1. TimerServer란
```bash
TimerServer는 **Action 서버 예제 노드**이다.

클라이언트로부터 **시간(duration)** 을 받아서  
해당 시간이 지나면 작업을 완료했다고 알려주는 기능을 한다.

즉

> "지정된 시간 동안 타이머를 실행하는 서버"

이다.
```
---

### 2. TimerServer 동작 흐름
```bash
1. TimerClient가 TimerServer에 시간 요청
2. TimerServer가 타이머 시작
3. 진행 상황을 Feedback으로 전달
4. 시간이 끝나면 Result 반환

TimerClient → Goal 요청
↓
TimerServer → 타이머 실행
↓
Feedback 전송
↓
Result 반환
```
---

### 3. TimerServer의 사용 목적
```bash
이 예제는 다음을 이해하기 위해 사용된다.

- ROS Action 구조
- Action Server / Client 통신
- 장시간 작업 처리 방식
```
---

## 오늘 배운 점
```bash
- Action은 오래 걸리는 작업을 처리하기 위한 ROS 통신 방식이다.
- Topic과 Service와는 다른 구조를 가진다.
- Action은 Goal / Feedback / Result 구조로 이루어진다.
- TimerServer는 Action Server의 동작을 이해하기 위한 예제이다.
```