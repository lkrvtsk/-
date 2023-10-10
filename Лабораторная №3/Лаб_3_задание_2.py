with open('salary.txt','r',encoding='utf-8') as file:
    lines = file.readlines()

last_names = []
salaries = []
high_salaries = []

for line in lines:
    prts = line.strip().split()
    if len(prts) == 2:
        last_name = prts[0]   #familia
        salary = float(prts[1])   #oklad
        last_names.append(last_name)
        salaries.append(salary)

for i in range(len(salaries)):
    if salaries[i] > 10000:
        high_salaries.append(last_names[i])

print("Сотрудники с окладом больше 10 тысяч:", high_salaries)

average_salary = sum(salaries) / len(salaries)

print("Средний оклад сотрудников:", average_salary)