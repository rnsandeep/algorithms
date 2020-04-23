
def merge_sort(num):
    if len(num) <= 1:
       return num

    middle = int(len(num)/2)
    first_half = merge_sort(num[:middle])
    second_half = merge_sort(num[middle:])

    i = 0 
    j = 0
    numbers = []
    while( i < len(first_half) and j < len(second_half)):
          if first_half[i] < second_half[j]:
             numbers.append(first_half[i])
             i = i +1
          else:
             numbers.append(second_half[j])
             j = j +1

    if (i < len(first_half)):
         numbers += first_half[i:]

    if (j < len(second_half)):
         numbers += second_half[j:]

    return numbers
    

numbers = [15, 20, 3, 1, 24, 32]

final = merge_sort(numbers)

print(final)
