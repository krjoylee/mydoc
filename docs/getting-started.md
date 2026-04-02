# 📖 시작 가이드 (Getting Started)
> **원본 출처(Source):** Anti-gravity Doc System 내부 문서  
> **데이터 계보(Lineage):** 프로젝트 초기 생성  

---

## 1. 사전 요구사항 (Prerequisites)

| 도구(Tool) | 버전(Version) | 설치 확인(Check) |
|---|---|---|
| Python | 3.11+ | `python --version` |
| pip | 최신 | `pip --version` |
| Git | 최신 | `git --version` |
| GitHub CLI | 최신 | `gh --version` |

---

## 2. 설치 (Installation)

```bash
# 1. 리포지토리 클론 (Clone Repository)
git clone https://github.com/YOUR_USERNAME/mydoc.git
cd mydoc

# 2. Python 의존성 설치 (Install Python Dependencies)
pip install -r requirements.txt

# 3. 로컬 서버 실행 (Run Local Server)
mkdocs serve
```

---

## 3. 문서 편집 방법 (How to Edit)

### 3.1 일반 편집 (General Edit)
1. `docs/` 폴더 내 `.md` 파일을 텍스트 에디터로 연다.
2. 마크다운 문법으로 내용을 수정한다.
3. `mkdocs serve`로 실시간 미리보기를 확인한다.

### 3.2 Steve 전용 마킹 (Steve's Marking)

| 마킹 유형 | 마크다운 문법 | 렌더링 결과 |
|---|---|---|
| **Bold (Level 2, AI)** | `**텍스트**` | **텍스트** |
| ***Bold+Italic (Level 3, Steve)*** | `***텍스트***` | ***텍스트*** |
| ==하이라이트(Highlight)== | `==텍스트==` 또는 `<mark>텍스트</mark>` | ==하이라이트== |
| (Steve: 메모) | `(Steve: 메모 내용)` | 그대로 표시 |

!!! warning "주의사항"
    `***`, `<mark>`, `(Steve:` 패턴은 동기화 엔진이 감지하는 고유 식별자입니다.
    이 패턴을 원본 번역 본문에 사용하지 마세요.

---

## 4. 배포 (Deployment)

```bash
# 수동 배포 (Manual Deploy)
mkdocs gh-deploy

# 자동 배포 (Auto Deploy)
# main 브랜치에 push하면 GitHub Actions가 자동으로 배포합니다.
git add .
git commit -m "docs: 문서 업데이트"
git push origin main
```

---

## 5. 문서 동기화 (Sync)

!!! info "동기화 방법"
    - **자동:** 매월 1일, GitHub Actions가 원본 문서를 크롤링하여 업데이트합니다.
    - **수동:** GitHub Actions 탭에서 `Sync Docs` 워크플로우를 수동 실행합니다.

---

> **End of Document — Getting Started Guide**
