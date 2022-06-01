# pickle : 데이터를 파일 형태로 저장
import pickle

# pickle 파일로 저장
profile_file = open("profile.pickle", "wb") # b : binary 형태
profile = {"name" : "AAA", "age" : 30, "hobby" : ["golf", "coding", "music"]}
print(profile)
# profile에 있는 정보를 file에 저장
pickle.dump(profile, profile_file)
profile_file.close()

# pickle 파일을 읽기
profile_file = open("profile.pickle", "rb")
# file에 있는 정보를 profile에 불러오기
profile = pickle.load(profile_file)
print(profile)
profile_file.close()
