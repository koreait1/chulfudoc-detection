# [철푸닥](https://chulfudoc.xyz) AI 백엔드 레포지토리
<div align="center">
  <a href="https://chulfudoc.xyz">
    <img src="https://raw.githubusercontent.com/koreait1/chulfudoc-api/master/img/logo.png" alt="철푸닥" width="500"/>
  </a><br />
</div>

---
## 🔹 구현 기능
- 쓰러진 사람 감지 API : 업로드된 이미지에서 쓰러진 사람 여부를 감지
- YOLO 모델 예측 기능 : 이미지 내 객체 감지 및 좌표 반환

### 🛠️ 기능 설명
- detection  
  `predict.py` 스크립트를 통해 YOLO 모델(`model.pt`)을 사용하여 이미지를 분석  
  - `model.predict("C:/data/3.jpg", conf=0.3)` 형태로 사용
  - 신뢰도(confidence) 0.3 이상인 객체만 반환

- 결과 반환  
  - 각 객체의 bounding box 좌표 및 confidence 값 출력  
  - API 서버에서는 업로드된 이미지를 받아 위와 같은 처리 후 JSON 형태로 반환



---
### 프론트엔드 레포지토리 : https://github.com/koreait1/chulfudoc-front
### API 백엔드 레포지토리 : https://github.com/koreait1/chulfudoc-api
