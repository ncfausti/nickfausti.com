def find_max_sum_sub_array(A):
  N = len(A)

  if N < 1:
    return 0

  current_max = A[0]
  global_max = A[0]
  for i in range(1, N):
    # if current_max is negative, stop making it more negative
    # reset it to be value at curzzz
    if current_max < 0:
      current_max = A[i]
    else:
      current_max += A[i]
    
    if current_max > global_max:
      global_max = current_max

  return global_max

v = [-4, 2, -5, 1, 2, 3, 6, -5, 1]
sum = find_max_sum_sub_array(v)
print("Sum of largest subarray: " + str(sum))