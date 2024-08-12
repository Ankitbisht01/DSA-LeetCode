'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

'''
#Solution
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # Initialize the value of k
        self.k = k
        
        # Initialize a min-heap to store the k largest elements
        self.data = nums
        heapq.heapify(self.data)
        
        # Ensure the heap contains exactly k largest elements
        while len(self.data) > k:
            heapq.heappop(self.data)

    def add(self, val: int) -> int:
        # Add the new value to the heap
        heapq.heappush(self.data, val)
        
        # If the size of the heap exceeds k, remove the smallest element
        if len(self.data) > self.k:
            heapq.heappop(self.data)
        
        # Return the smallest element in the heap, which is the kth largest element
        return self.data[0]