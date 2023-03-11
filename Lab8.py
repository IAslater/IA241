#3.1 
def count_word(input_string):
    return len(input_string.split())
    
#3.2
demo_string = "hello world"
print(count_word(demo_string))
#3.3
def find_min(num_list):
    
    min_item = num_list[0]
    
    for num in num_list:
        if min_item >= num:
            min_item = num
    return(min_item)
    
#3.4
demo_list = [1,2,3,4,5,6]
print(find_min(demo_list))
#3.5
mix_list = [1,2,3,4,"a",5,6]
print(find_min(mix_list))
