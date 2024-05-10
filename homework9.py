car = ['BMW', 'MB', 'LADA', 'KIA', 'HONDA']
cars_count = 0
for i in car:
    for j in range(len(car)):
        cars_count += 10
        print(cars_count)
        break
    print('Я езжу на автомобиле марки', i)