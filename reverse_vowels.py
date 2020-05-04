def reverse_vowels(str):
  chars = list(str)
  vowel_idx = []
  
  for i, char in enumerate(chars):
    if char in "aeiouAEIOU":
      vowel_idx.append(i)
  
  mid = len(vowel_idx) // 2
  fwd_i = 0
  bwd_i = -1
  
  while fwd_i < mid:
    chars[vowel_idx[fwd_i]], chars[vowel_idx[bwd_i]] = chars[vowel_idx[bwd_i]], chars[vowel_idx[fwd_i]]
    fwd_i += 1
    bwd_i -= 1
    
  return "".join(chars)      