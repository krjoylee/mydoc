# [1.004] Anti-gravity Doc-Centric 시스템 통합 명세서 (GitHub Actions Integration)
> **문서 ID:** SPEC-1.004  
> **버전(Version):** v1.0.0  
> **최종 수정(Last Modified):** 2026-04-03  
> **작성자(Author):** Steve (Joy)  
> **출처(Origin):** Antigravity Gemini 대화 기반 자동 생성  

---

## 1. 목적 (Objective)
- **원본 동기화(Source Sync):** `https://antigravity.google/docs/home` 최신 데이터 무결성 및 자동 추적.
- **지식 자산화(Knowledge Asset):** 한글(English) 병기 및 Steve 전용 마킹(Marking) 결합.
- **워크플로우(Workflow):** 수동 편집의 유연성과 자동화의 효율성을 결합한 하이브리드 시스템.

---

## 2. 표준 문서 헤더 및 언어 규격 (Document & Language Spec)
| 항목(Item) | 규격(Standard) |
|---|---|
| **헤더(Header)** | 모든 재구축 문서는 원본 출처와 데이터 계보(Lineage)를 최상단에 명시 |
| **언어(Language)** | 기술 용어 및 설명은 **한글(English)** 병기 원칙 |
| **환경(Environment)** | Windows 11 + **WSL2(Ubuntu)** 최적화 명령 및 경로 체계 |

---

## 3. 기능 정의 (Functional Definition)

### 3.1 GitHub Actions 기반 자동화 (CI/CD)
- **동기화(Sync):** 정해진 주기(매월 1회) 혹은 수동 트리거 시 깃허브 서버가 직접 원본 Doc을 크롤링하고 번역
- **배포(Deploy):** Steve가 소스 에디터에서 수정한 내용을 커밋(Commit)하면 즉시 웹 페이지에 반영

### 3.2 하이브리드 편집/렌더링 (Live Editor & Preview)
- **중앙 하단(Bottom):** 마크다운 소스 편집기 — Steve의 `***`, `<mark>`, `Note` 기입
- **중앙 상단(Top):** 실시간 렌더링 뷰어 — 수정 사항 즉시 확인

### 3.3 업데이트 보존 (Update Preservation)
- 깃허브 액션이 새로운 데이터를 가져올 때, Steve의 기존 마킹 계층을 분석하여 새 본문에 자동으로 재부착(Re-attach)

### 3.4 보안 게이트 (Security Gate)
- JS 기반 비밀번호 입력창을 통한 접근 제한(Access Control)

---

## 4. 디자인 및 레이아웃 정의 (Design Spec)

```
┌─────────────────────────────────────────────────────────┐
│  Header: Anti-gravity Doc System          [🔒] [⚙️]    │
├──────────────┬──────────────────────────────────────────┤
│              │                                          │
│  Navigation  │  Rendered Preview (Live)                 │
│  (280px)     │  (760px 기준)                            │
│              │                                          │
│  ──────────  ├──────────────────────────────────────────┤
│              │                                          │
│  TOC         │  Markdown Source Editor                  │
│  (페이지내)  │  (Steve 편집 영역)                       │
│              │                                          │
├──────────────┴──────────────────────────────────────────┤
│  Footer: Status Bar | Last Sync: YYYY-MM-DD            │
└─────────────────────────────────────────────────────────┘
```

- **좌측 영역(Left, 280px 고정):** 글로벌 네비게이션(상) + 페이지 내 목차(하/TOC)
- **중앙 영역(Center, 760px 기준):** 실시간 렌더링 뷰어(상) + 소스 편집기(하)
- **상호작용(Interaction):** TOC 클릭 시 렌더링 뷰어와 편집기가 해당 위치로 동시 스크롤 동기화

---

## 5. 개발 환경 및 기술 스택 (Environment & Stack)

| 구분(Category) | 기술(Technology) | 용도(Purpose) |
|---|---|---|
| Host/Guest | Windows 11 + WSL2 (Ubuntu 22.04+) | 개발 환경 |
| Automation Engine | GitHub Actions (YAML 기반) | CI/CD 워크플로우 제어 |
| Scripting | Python 3.11+ | 스크래핑 & 병합 로직 |
| Web Build | Node.js 18+ | 웹 빌드 |
| Static Site | MkDocs (Material Theme) | 커스텀 UI 기반 문서 사이트 |
| Hosting | GitHub Pages | 정적 사이트 배포 |

---

## 6. 데이터 무결성 및 업데이트 로직 (Update Logic)

1. **[추출(Extract)]:** 깃허브 액션이 원본 HTML 파싱 및 번역 수행
2. **[비교(Compare)]:** 기존 파일 내 Steve의 고유 식별자(`***`, `<mark>`, `Note`) 위치 파악
3. **[병합(Merge)]:** 새로운 본문에 식별자를 앵커(Header ID) 기준으로 재배치
4. **[검토(Review)]:** 변경 사항이 클 경우 `[Review Needed]` 라벨을 생성하여 Steve 최종 컨펌 유도

---

## 7. 매핑 권한 (Mapping Protocol)

| 주체(Actor) | 권한(Permission) | 마킹 레벨(Level) |
|---|---|---|
| AI (사서/GitHub Actions) | 원본 텍스트 추출, 한글 번역 및 `**Bold**` 처리 | Level 2 |
| User (Steve) | `***Bold+Italic***`, `<mark>Highlight</mark>`, `(Steve: Note)` 작성 | Level 3 |

---

## 8. 보안 모델 (Security Model)
- 클라이언트 사이드 JS 비밀번호 게이트 (초기 버전)
- 향후 GitHub OAuth 또는 토큰 기반 인증으로 확장 가능

---

> **End of Document — SPEC-1.004**
