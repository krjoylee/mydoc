# Anti-gravity Doc System 🚀

> **원본 동기화(Source Sync)** + **Steve 마킹 보존(Marking Preservation)** + **GitHub Actions CI/CD**

## 🎯 프로젝트 소개 (Introduction)

Anti-gravity Doc-Centric 시스템은 [Antigravity 공식 문서](https://antigravity.google/docs/home)를 
**자동으로 추적·동기화·번역**하고, Steve의 개인 마킹(Marking)을 **안전하게 보존**하는 
하이브리드 문서 관리 시스템입니다.

---

## ✨ 핵심 기능 (Key Features)

<div class="grid cards" markdown>

- :material-sync: **자동 동기화 (Auto Sync)**
  
  GitHub Actions가 매월 원본 문서를 크롤링하여 최신 상태를 유지합니다.

- :material-pencil: **하이브리드 편집 (Hybrid Edit)**
  
  마크다운 소스 편집 + 실시간 미리보기를 하나의 화면에서.

- :material-shield-lock: **보안 게이트 (Security Gate)**
  
  비밀번호 기반 접근 제어로 비공개 문서를 보호합니다.

- :material-tag-multiple: **마킹 보존 (Marking Preservation)**
  
  동기화 시 Steve의 `***강조***`, `<mark>하이라이트</mark>`, `(Steve: 메모)` 마킹이 자동 보존됩니다.

</div>

---

## 🗂️ 프로젝트 문서 (Project Documents)

| 문서 | 설명 |
|---|---|
| [📋 명세서 (Spec)](SPEC.md) | 시스템 통합 명세서 |
| [📐 실행 계획 (Plan)](PLAN.md) | 단계별 구체화 실행 계획 |
| [✅ TODO](TODO.md) | 진행 체크리스트 |
| [🧪 테스트 계획 (Test)](TEST_PLAN.md) | 테스트 케이스 및 결과 |
| [📝 변경 로그 (Changelog)](CHANGELOG.md) | 작업 이력 추적 |

---

## 🏗️ 기술 스택 (Tech Stack)

| 구분 | 기술 |
|---|---|
| Static Site | MkDocs + Material Theme |
| Automation | GitHub Actions |
| Scripting | Python 3.11+ |
| Hosting | GitHub Pages |
| Security | Client-side JS Gate |

---

## 🚀 빠른 시작 (Quick Start)

```bash
# 로컬 개발 서버 실행
mkdocs serve

# 사이트 빌드
mkdocs build

# GitHub Pages 배포
mkdocs gh-deploy
```

---

!!! tip "Steve 마킹 가이드"
    - **Level 2 (AI):** `**Bold Text**` → **Bold Text**
    - **Level 3 (Steve):** `***Bold+Italic***` → ***Bold+Italic***
    - **하이라이트:** `<mark>Important</mark>` → <mark>Important</mark>
    - **메모:** `(Steve: 여기 주목)` → (Steve: 여기 주목)
