def partition_to_subset_sum(partition_set):
    # Calculate the total sum of numbers in the set
    total_sum = 0
    for value in partition_set:
        total_sum += value

    # Check if the total sum is odd (which makes partitioning impossible)
    if total_sum % 2 != 0:
        raise ValueError("Cannot perform mapping. Total sum is odd.")

    # Target sum for the Subset Sum problem is half of the total sum
    target_sum_subset_sum = total_sum // 2

    # The Subset Sum instance has the same set of numbers as the Partition instance
    subset_sum_set = partition_set

    return subset_sum_set, target_sum_subset_sum

def is_subset_sum(subset_sum_set, target_sum):
    n = len(subset_sum_set)
    memo = {}  # Memoization dictionary to store computed results
    return subset_sum_recursive(n, target_sum, memo)

def subset_sum_recursive(i, curr_sum, memo):
        if i == 0:  # Base case: an empty subset can have a sum of 0
            return curr_sum == 0

        if (i, curr_sum) in memo:
            return memo[(i, curr_sum)]

        if subset_sum_set[i - 1] <= curr_sum:
            # Include the current element or exclude it
            result = subset_sum_recursive(i - 1, curr_sum - subset_sum_set[i - 1], memo) or \
                     subset_sum_recursive(i - 1, curr_sum, memo)
        else:
            # Exclude the current element
            result = subset_sum_recursive(i - 1, curr_sum, memo)

        memo[(i, curr_sum)] = result  # Cache the result
        return result

# Example usage:
partition_set_example = [3, 5, 7, 8, 9]
subset_sum_set, target_sum_subset_sum = partition_to_subset_sum(partition_set_example)

print("Partition Set:", partition_set_example)
print("Subset Sum Set:", subset_sum_set)
print("Target Sum for Subset Sum:", target_sum_subset_sum)
print(is_subset_sum(subset_sum_set, target_sum_subset_sum))