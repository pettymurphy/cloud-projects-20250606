
contacts = {
    'number' : 4,
    'students' :
        [
            {'name': 'Derrick Robinson', 'email' : 'derrick.pope75@gmail.com'},
            {'name': 'Petty Murphy', 'email' : 'pettymurphy@petty.com'},
            {'name': 'Mean Joe', 'email' : 'mjoe@mean.com'},
            {'name': 'Mike Jordan', 'email' : 'mike@example.com'}
        ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])