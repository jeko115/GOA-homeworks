# 1. თუ ასაკი არის 18-ზე ზემოთ ან 50 წლის ქვემოთ, ან თუ ასაკი ნაკლებია 18-ზე და მეტია 50-ზე, 
# გამოტანეთ ის უნდა იყოს ან მოხუცი ან ახალგაზრდა
age = int(input("შეიყვანეთ თქვენი ასაკი: "))

if (age > 18 and age < 50):
    print("თქვენი ასაკი არის ახალგაზრდა.")
elif (age < 18 or age > 50):
    print("თქვენი ასაკი არის მოხუცი.")
else:
    print("არ არსებობს შესაბამისი კატეგორია.")

# 2. გამოვიყენოთ or ოპერატორი, რათა შევამოწმოთ, თუ მოცემული ციფრები არიან 10-ზე მეტი ან 50-ზე ნაკლები
num1 = int(input("შეიყვანეთ პირველი ციფრი: "))
num2 = int(input("შეიყვანეთ მეორე ციფრი: "))

if num1 > 10 or num2 < 50:
    print("ერთ-ერთი ციფრი უფრო დიდია 10-ზე ან ნაკლებია 50-ზე.")
else:
    print("ორივე ციფრი არ აკმაყოფილებს პირობებს.")

# 3. შეამოწმეთ, არის თუ არა მოცემული ციფრი დადებითი ან ნული, თუმცა არ არის უარყოფითი
number = int(input("შეიყვანეთ ციფრი: "))

if number >= 0:
    print("ციფრი არის დადებითი ან ნული.")
else:
    print("ციფრი არის უარყოფითი.")

# 4. გამოიყენეთ or, რათა გაიგოთ, თუ ცხოველი არის კატა თუ თაგვი
animal = input("შეიყვანეთ ცხოველის სახელი: ")

if animal == "კატა" or animal == "თაგვი":
    print("ეს ცხოველი არის კატა ან თაგვი.")
else:
    print("ეს ცხოველი არ არის კატა ან თაგვი.")

# 5. შეამოწმეთ, თუ ერთ-ერთი ციფრი უფრო დიდია 10-ზე ან მეორე ციფრი ნაკლებია 50-ზე
if num1 > 10 or num2 < 50:
    print("ერთი ციფრი უფრო დიდია 10-ზე ან მეორე ციფრი ნაკლებია 50-ზე.")
else:
    print("ორივე ციფრი არ აკმაყოფილებს პირობებს.")

# 6. შეამოწმეთ შეყვანილი სიტყვა hello-ა თუ hello world
word = input("შეიყვანეთ სიტყვა: ")

if word == "hello" or word == "hello world":
    print("შეყვანილი სიტყვა არის ან hello, ან hello world.")
else:
    print("შეყვანილი სიტყვა არ არის hello და არც hello world.")

# 7. კომენტარები:
# 1. აქ შევამოწმეთ ასაკის სიფართოვე: თუ ადამიანი არის 18-ს ზემოთ და 50-ს ქვემოთ - ახალგაზრდა, ან 18-ს ქვემოთ ან 50-ს ზემოთ - მოხუცი.
# 2. or ოპერატორი გამოიყენება იმის შესამოწმებლად, რომ ერთი ციფრი იყოს 10-ზე მეტი ან 50-ზე ნაკლები.
# 3. შევამოწმეთ, არის თუ არა ციფრი დადებითი ან ნული.
# 4. or-ით შევამოწმეთ, არის თუ არა ცხოველი კატა ან თაგვი.
# 5. შევამოწმეთ, თუ ერთი ციფრი დიდი არის 10-ზე ან მეორე ნაკლებია 50-ზე.
# 6. შევამოწმეთ, თუ შეყვანილი სიტყვა იყო "hello" ან "hello world".
