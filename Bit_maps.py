# csv_string = """rowid,student_id,first_name,major,honors
# 0,kingslayer,Jaime,CSE,1
# 1,the_imp,Tyrion,EE,0
# 2,khaleesi,Dany,Other,0
# 3,blackfish,Brynden,Other,1
# 4,young_wolf,Robb,CSE,1
# 5,mountain,Gregor,EE,0"""

# def remove_whitespace(text):
#     return "\n".join(line.strip() 
#         for line in text.splitlines())

# csv_string = remove_whitespace(csv_string)
# ####################
# # This is where I call your function.
# bm = bitmap(csv_string)
# ####################

# result = bm.matching_rows({"major": "CSE", "honors": "1"})
# print("Result:")
# print(result)
# assert "100010" == result

# result = bm.matching_rows({"major": "CSE", "honors": "1"})
# print("Result:")
# print(result)
# assert "100010" == result

# result = bm.get_matching_rows({"major": "CSE", "honors": "1"})
# result = remove_whitespace(result)
# print("Result:")
# print(result)
# print()

# expected = """rowid,student_id,first_name,major,honors
# 0,kingslayer,Jaime,CSE,1
# 4,young_wolf,Robb,CSE,1"""

# expected = remove_whitespace(expected)
# print("Expected:")
# print(expected)
# print()
# self.assertEqual(expected, result)


class Bit_obj:
    
    def __init__(self, row_number, attributes, csv_list):
        self.row = row_number
        self.attributes = attributes
        self.csv_list = csv_list
        
    def get_map(self, *args):
        bit_str = '0' * self.row
        index = self.attributes.index(args[0])
        for i in range(self.row):
            line = self.csv_list[i].split(',')
            if line[index] == args[1]:
                bit_str = bit_str[0:i] + '1' + bit_str[i+1:]
        return bit_str
    
    def matching_rows(self, kwargs):
        result = '1' * self.row
        for ele in kwargs:
            key_val = []
            key_val.append(ele)
            key_val.append(kwargs[ele])
            temp = self.get_map(key_val[0], key_val[1])
            # result = result & temp
            res = ''
            for i in range(len(result)):
                if result[i] == temp[i] == '1':
                    res = res + '1'
                else:
                    res = res + '0'
            result = res
        return result
    
    def get_matching_rows(self, kwargs):
        index = self.matching_rows(kwargs)
        print('index:', index)
        result = ''
        temp = []
        temp.append(','.join(self.attributes))
        for i in range(self.row):
            if index[i] == '1':
                temp.append(self.csv_list[i])

        result = '\n'.join(temp)
        return result
        

def bitmap(csv_string):
    
    csv_list = csv_string.split('\n')
    row_num = len(csv_list) - 1
    attributes = csv_list.pop(0)
    attributes = attributes.split(',')
    
    return Bit_obj(row_num, attributes, csv_list)