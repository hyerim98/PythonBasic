import pickle

# with : 자동으로 파일이 close가 된다

# pickle 파일 데이터 읽기
with open("profile.pickle", "rb") as profile_file :
    print(pickle.load(profile_file))

# 파일 생성
with open("study.txt", "w", encoding="utf8") as study_file :
    study_file.write("study python")

# 파일 데이터 읽기
with open("study.txt", "r") as study_file :
    print(study_file.read())
