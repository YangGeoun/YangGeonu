## TIL
### 2023/7/13
#### Git 명령어를 알아보자

#### 기본명령어

- git init : 저장소 생성

- git add : 수정 또는 작업된 파일 stage area에 추가 

- git commit -m "메시지" : 커밋 

- git log [--graph] : 커밋 로그 확인

- git status :  git 상태 확인

- git branch : 브랜치 확인

- git branch {브랜치이름} : 브랜치 생성

- git switch {브랜치이름} : 브랜치 이동

- git branch [-d | -D] {브랜치이름} : 브랜치 삭제

- git merge {브랜치이름} : 브랜치 병합

#### 원격 저장소(remote repository) 관련 명령어

- git clone : 원격 저장소 로컬에 복사

- git push {원격저장소 이름} {브랜치이름} : 원격 저장소에 업로드

- git pull {원격저장소 이름} {브랜치이름} : 원격 저장소 다운로드

- git remote add {원격저장소이름} {원격저장소주소} : 로컬저장소에 원격저장소 추가하기 (단, 원격저장소가 비어있어야함, commit X, 파일 X)
