# Naomi Tesla
# https://codingbat.com/prob/p110166

def array_front9(nums):
  for i in nums[0:4]:
    if i == 9:
      return True
  return False
