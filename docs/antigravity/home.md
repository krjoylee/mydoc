# Antigravity Documentation — Home
> **원본 출처(Source):** `https://antigravity.google/docs/home`  
> **데이터 계보(Lineage):** GitHub Actions 자동 동기화 → 한글 병기 번역  
> **최종 동기화(Last Sync):** 2026-04-03  
> **동기화 상태(Sync Status):** ✅ 최신(Up-to-date)  

---

## 개요 (Overview)

**Antigravity**는 Google의 차세대 AI 플랫폼으로, 개발자와 연구자에게 
강력한 도구와 API를 제공합니다.

!!! note "번역 안내"
    이 문서는 원본 영문 문서를 기반으로 한글 번역되었습니다.
    **Bold** 처리는 AI(Level 2) 자동 번역 강조이며,
    ***Bold+Italic*** 처리는 Steve(Level 3)의 개인 마킹입니다.

---

## 주요 기능 (Key Features)

### 모델 API (Model API)
**Antigravity 모델 API**를 사용하면 다양한 AI 모델에 프로그래밍 방식으로 
접근할 수 있습니다. ***이 부분은 Steve가 특별히 중요하다고 표시한 섹션입니다.***

<mark>모델 API는 REST와 gRPC 두 가지 프로토콜을 지원합니다.</mark>

(Steve: 추후 gRPC 성능 비교 테스트 필요)

### 시작하기 (Getting Started)
**빠른 시작 가이드(Quick Start Guide)** 를 통해 5분 안에 첫 번째 API 호출을 
완료할 수 있습니다.

```python
# 예시 코드 (Example Code)
import antigravity

client = antigravity.Client(api_key="YOUR_API_KEY")
response = client.generate(
    model="antigravity-pro",
    prompt="Hello, Antigravity!"
)
print(response.text)
```

### 문서 구조 (Documentation Structure)
| 섹션(Section) | 설명(Description) |
|---|---|
| **Guides** | 단계별 학습 가이드 |
| **API Reference** | 전체 API 레퍼런스 |
| **Tutorials** | 실전 튜토리얼 |
| **Cookbook** | 레시피 모음 |

---

## Steve의 학습 노트 (Steve's Notes)

!!! abstract "개인 메모 영역"
    이 섹션은 Steve의 개인 학습 노트입니다.
    동기화 시 이 섹션은 보존됩니다.

- ***API Key 관리는 환경변수로*** — 코드에 하드코딩 금지
- <mark>Rate Limit: 분당 60회 요청 제한 주의</mark>
- (Steve: Cookbook 섹션의 RAG 예제가 특히 유용함)

---

> **End of Document — Antigravity Home (Synced)**
