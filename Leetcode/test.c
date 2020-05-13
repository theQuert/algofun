/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

int CompareByIncrease(const void* a, const void* b)
{
	return *(int*)a - *(int*)b;
}

int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){
	*returnSize = 0;

	if(numsSize < 3)
	{
		return NULL;
	}

	int cur = 0;
	int low = cur + 1;
	int high = numsSize - 1;

	int** reutrnArray = (int**)malloc(sizeof(int*) * (numsSize) * (numsSize));
	*returnColumnSizes = (int*)malloc(sizeof(int*) * (numsSize) * (numsSize)); // un-usable
	// Sort
	qsort(nums, numsSize, sizeof(int), CompareByIncrease);
 
	// while((nums[cur] <= 0) && (low < high))
	while((nums[cur] <= 0) && (cur + 1 < numsSize - 1))
	{
		// Update
		low = cur + 1;
		high = numsSize - 1;
		// Ensure low is left to high
		while(low < high)
		{
			if(0 == (nums[low] + nums[high] + nums[cur]))
			{
				returnArray[*returnSize] = (int*)malloc(sizeof(int) * 3); // When find a group, allocate 3 memory address
				(*returnColumnSizes)[*returnSize] = 3; // Record Column size
				returnArray[*returnSize][0] = nums[cur];
				returnArray[*returnSize][1] = nums[low];
				returnArray[*returnSize][2] = nums[high];
				*returnSize++;
			// Remove repeated elements (low, high)
			while( (nums[low] == nums[++low]) && (low < high) ); 
			while( (nums[high] == nums[--high]) && (low < high));
			}

			else if(0 < nums[low] + nums[high] + nums[cur])
			{
				high --;
			}
			else
			{
				low++;
			}

		}
		// Remove repeated elements (cur)
		while((nums[cur] == nums[++cur]) && (cur + 1 < numsSize - 1) );

	}

	return returnArray;
	/*
		get memory address: pointner, or & // &arr[i] = ptr + i
		get variable: variable or *pointer // arr[i] = *(ptr + i)
	*/


}
