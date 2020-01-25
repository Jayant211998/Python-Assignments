import pickle
phonebook={'jayant':'555-11111','mihir':'848-85788','himanshu':'555-33333'}
output_file=open("phonebook.dat",'wb')
pickle.dump(phonebook,output_file)
output_file.close()
input_file=open("phonebook.dat",'rb')
pickle.load(input_file)
print(input_file.read())