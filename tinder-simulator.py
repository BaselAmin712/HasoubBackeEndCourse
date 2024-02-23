person1 = {
  "name": "Basel",
  "gender": "male",
  "age": 28,
  "profession": "programer",
  "favorite_tv_show": "top gear",
  "favorite_food": "hamburger"
}
person2 = {
  "name": "Mike",
  "gender": "male",
  "age": 36,
  "profession": "constructor",
  "favorite_tv_show": "top gear",
  "favorite_food": "pizza"
}
person3 = {
  "name": "Sean",
  "gender": "male",
  "age": 49,
  "profession": "taxi driver",
  "favorite_tv_show": "crazy taxi",
  "favorite_food": "falafel"
}
person4 = {
  "name": "Sara",
  "gender": "female",
  "age": 41,
  "profession": "teacher",
  "favorite_tv_show": "batman",
  "favorite_food": "coocked rice"
}
name, gender, age, profession, favorite_tv_show, favorite_food = input("enter your name, gender, age, profession, favorite tv show and your favorite food separeted with comma.\n").split(',')
person5 = dict(name = name, gender = gender, age = int(age),profession = profession, favorite_tv_show = favorite_tv_show, favorite_food = favorite_food)
rules = [["Mohammad", "Basel", "Yossi", "sara"], ["male"]] + [list(range(25,38))] + [["teacher", "programer", "taxi driver"]] + [["batman","top gear"]] + [["pizza", "hamburger", "salad"]]
if person5["name"] in rules[0] and person5["gender"] in rules[1] and person5["age"] in rules[2] and person5["profession"] in rules[3] and person5["favorite_tv_show"] in rules[4] and person5["favorite_food"] in rules[5]:
    print("OK!")
