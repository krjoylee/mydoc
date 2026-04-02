# 📋 프로젝트 구체화 실행 계획서 (Implementation Plan)
> **문서 ID:** PLAN-1.004  
> **버전(Version):** v1.0.0  
> **최종 수정(Last Modified):** 2026-04-03  

---

## Phase 0: 프로젝트 초기화 (Initialization) — 🟢 즉시
| # | 작업(Task) | 도구(Tool) | 완료 기준(Done When) |
|---|---|---|---|
| 0.1 | `mydoc` 리포지토리 생성 | `gh repo create` | GitHub에 빈 repo 존재 |
| 0.2 | 로컬 Git 초기화 & 리모트 연결 | `git init`, `git remote add` | `.git/` 생성 완료 |
| 0.3 | MkDocs Material 설치 | `pip install mkdocs-material` | `mkdocs serve` 동작 |
| 0.4 | 기본 디렉토리 구조 생성 | 파일 생성 | 아래 트리 구조 완성 |
| 0.5 | `.gitignore` 생성 | 파일 생성 | Python/Node/MkDocs 패턴 포함 |

### 디렉토리 구조 (Directory Tree)
```
mydoc/
├── .github/
│   └── workflows/
│       ├── deploy.yml          # 배포 워크플로우
│       └── sync-docs.yml       # 문서 동기화 워크플로우
├── docs/
│   ├── SPEC.md                 # 통합 명세서
│   ├── PLAN.md                 # 이 문서
│   ├── TODO.md                 # 진행 체크리스트
│   ├── TEST_PLAN.md            # 테스트 계획서
│   ├── CHANGELOG.md            # 변경 로그
│   ├── index.md                # 메인 랜딩 페이지
│   ├── getting-started.md      # 시작 가이드
│   └── antigravity/            # 원본 동기화 문서 보관
│       └── home.md             # 샘플 동기화 문서
├── scripts/
│   ├── sync_docs.py            # 원본 크롤링 & 번역 스크립트
│   └── merge_markings.py       # Steve 마킹 병합 스크립트
├── overrides/
│   ├── main.html               # MkDocs Material 커스텀 템플릿
│   └── assets/
│       └── stylesheets/
│           └── custom.css      # 커스텀 CSS
├── mkdocs.yml                  # MkDocs 설정 파일
├── requirements.txt            # Python 의존성
├── .gitignore
└── README.md
```

---

## Phase 1: 코어 사이트 구축 (Core Site Build) — 🟡 1시간
| # | 작업(Task) | 설명(Description) | 우선순위 |
|---|---|---|---|
| 1.1 | `mkdocs.yml` 설정 | Material Theme, 한글 검색, 네비게이션 구성 | ⭐⭐⭐ |
| 1.2 | `index.md` 작성 | 랜딩 페이지 — 프로젝트 소개 및 퀵링크 | ⭐⭐⭐ |
| 1.3 | 커스텀 CSS 적용 | 보안 게이트 UI, 편집기 레이아웃, 마킹 스타일링 | ⭐⭐⭐ |
| 1.4 | 커스텀 템플릿 | `main.html` 오버라이드 — JS 비밀번호 게이트 삽입 | ⭐⭐ |
| 1.5 | 샘플 문서 작성 | `antigravity/home.md` — Steve 마킹 예시 포함 | ⭐⭐ |

---

## Phase 2: GitHub Actions CI/CD — 🟡 30분
| # | 작업(Task) | 설명(Description) |
|---|---|---|
| 2.1 | `deploy.yml` 작성 | `main` 브랜치 push 시 `mkdocs gh-deploy` 자동 실행 |
| 2.2 | `sync-docs.yml` 작성 | 월간 크론 + 수동 트리거, Python 스크래핑 실행 |
| 2.3 | GitHub Pages 활성화 | `gh-pages` 브랜치 기반 배포 설정 |
| 2.4 | 초기 배포 테스트 | Push → Actions → Pages URL 확인 |

---

## Phase 3: 동기화 엔진 (Sync Engine) — 🔴 추후
| # | 작업(Task) | 설명(Description) |
|---|---|---|
| 3.1 | `sync_docs.py` 구현 | 원본 HTML 파싱 → 마크다운 변환 → 한글 번역 |
| 3.2 | `merge_markings.py` 구현 | Steve 마킹(Level 3) 감지 및 재부착 알고리즘 |
| 3.3 | 변경량 감지 로직 | 대규모 변경 시 `[Review Needed]` 라벨 자동 생성 |

---

## Phase 4: 라이브 에디터 통합 (Live Editor) — 🔴 추후
| # | 작업(Task) | 설명(Description) |
|---|---|---|
| 4.1 | 인라인 에디터 UI | 중앙 영역 상/하 분할 레이아웃 |
| 4.2 | 실시간 렌더링 | 편집기 입력 → 미리보기 즉시 반영 |
| 4.3 | TOC 동기 스크롤 | 좌측 목차 클릭 시 양측 동시 이동 |

---

## 실행 순서 요약 (Execution Order)
```
Phase 0 (즉시) → Phase 1 (1시간) → Phase 2 (30분) → 🎯 초안 데모 완료
                                                      ↓
                                              Phase 3 & 4 (추후 확장)
```

---

> **End of Document — PLAN-1.004**
