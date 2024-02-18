# input
student_score = 80

# Process: Your Solution Code Here
if 80<=student_score<=100:
    print(f'Nilai A')
elif 65<=student_score<=79:
    print(f'Nilai B+')
elif 50<=student_score<=64:
    print(f'Nilai B')
elif 35<=student_score<=49:
    print(f'Nilai C')
elif 0<=student_score<=34:
    print(f'Nilai D')
else:
    print(f'Score yang anda masukan salah') 
# Output "Nilai A"