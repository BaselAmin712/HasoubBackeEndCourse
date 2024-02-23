plant1_like_sun = True
plant2_like_sun = False
plant3_like_sun = True
plant1_like_wind = False
plant2_like_wind = True
plant3_like_wind = False
plant1_water_amount = 100
plant2_water_amount = 200
plant3_water_amount = 150
plant1_max_snow = 10
plant2_max_snow = 20
plant3_max_snow = 30
sunny,wind,precipitation_number,snow = input("describe the weather today - sunny?,wind?,precipitation number?,snow amount?.").split()
if plant1_like_sun == bool(sunny) and plant1_like_wind == bool(wind) and plant1_water_amount <= int(precipitation_number) :
    print('plant 1 likes this condition.')
if plant2_like_sun == bool(sunny) and plant2_like_wind == bool(wind) and plant2_water_amount <= int(precipitation_number) :
    print('plant 2 likes this condition.')
if plant3_like_sun == bool(sunny) and plant3_like_wind == bool(wind) and plant3_water_amount <= int(precipitation_number) :
    print('plant 3 likes this condition.')
if int(snow) > plant1_max_snow:
    print('plant 1 is dead due to the snow.')
if int(snow) > plant2_max_snow:
    print('plant 2 is dead due to the snow.')
if int(snow) > plant3_max_snow:
    print('plant 3 is dead due to the snow.')
print(sunny,wind,precipitation_number,snow)