def convert(number):
            str_num = str(number)
            if number < 10:
                str_num = '0' + str_num
            return str_num

def print_filename(name, student_id, week_id, assignment_id):
    # Both week_id and assignment_id are 1 or 2-digit numbers
    limit = range(1, 100)
    id_lst = [student_id, week_id, assignment_id]
    if student_id in limit and week_id in limit and assignment_id in limit :
        w_id = convert(week_id)
        a_id = convert(assignment_id)
        s_id = convert(student_id)   

        print(f'week{w_id}_assignment{a_id}_student{s_id}_{name}.py')
    else:
        print('week id or assignment id is out of range.')


print_filename('PhungThiThuAn', 2, 1, 1)
# week02_assignment01_PhungThiThuAn.py

print_filename('PhungThiThuAn', 19, 1, 8)
# week19_assignment08_PhungThiThuAn.py

print_filename('PhungThiThuAn', 1, 5, 6)
# week id or assignment id is out of range.
