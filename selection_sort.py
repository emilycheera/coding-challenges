def selection_sort(nums):

    for i in range(len(nums)):
        min_index = i

        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums


print(selection_sort([44, 5, 3, 7, 5, 6, 3, 4]))
