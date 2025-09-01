# [철푸닥](https://chulfudoc.xyz) AI 백엔드 레포지토리
<div align="center">
  <a href="https://chulfudoc.xyz">
    <img src="https://raw.githubusercontent.com/koreait1/chulfudoc-api/master/img/logo.png" alt="철푸닥" width="500"/>
  </a><br />
</div>

---
## 🔹 구현 기능
- 쓰러진 사람 감지 AI API : 업로드된 이미지/영상에서 쓰러진 사람 여부를 감지
- YOLO 기반 객체 탐지 API : 이미지 내 객체 탐지 및 좌표 반환

### 🛠️ 기능 설명
- detection  
  YOLO 모델(`model.pt`)을 활용하여 이미지 내 쓰러진 사람 여부를 탐지하고 결과 반환  

- predict  
  감지된 객체의 위치 좌표(bounding box) 및 확률(confidence score) 제공



---
### 프론트엔드 레포지토리 : https://github.com/koreait1/chulfudoc-front
### API 백엔드 레포지토리 : https://github.com/koreait1/chulfudoc-api
