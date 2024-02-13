List1 = ["W", "a", "w","b"]
        
List2 = ["e", " ","riting","log"]
new_list = []

new_lst = [i+j for i, j in zip(List1, List2)]
print(new_lst)

sample_str = "Analytics Vidhya"
print(list(sample_str))
print(type(sample_str.strip()))
