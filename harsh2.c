#include <stdio.h>

// Function to merge two subarrays arr[low..mid] and arr[mid+1..high]
void merge(int arr[], int low, int mid, int high) {
    int i, j, k;
    int n1 = mid - low + 1;
    int n2 = high - mid;

    // Create temporary arrays
    int left[n1], right[n2];

    // Copy data to temporary arrays left[] and right[]
    for (i = 0; i < n1; i++)
        left[i] = arr[low + i];
    for (j = 0; j < n2; j++)
        right[j] = arr[mid + 1 + j];

    // Merge the temporary arrays back into arr[low..high]
    i = 0;   // Initial index of first subarray
    j = 0;   // Initial index of second subarray
    k = low; // Initial index of merged subarray

    while (i < n1 && j < n2) {
        if (left[i] <= right[j]) {
            arr[k] = left[i];
            i++;
        } else {
            arr[k] = right[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of left[], if there are any
    while (i < n1) {
        arr[k] = left[i];
        i++;
        k++;
    }

    // Copy the remaining elements of right[], if there are any
    while (j < n2) {
        arr[k] = right[j];
        j++;
        k++;
    }
}

// Main function to perform merge sort on arr[low..high]
void mergeSort(int arr[], int low, int high) {
    if (low < high) {
        // Same as (low + high) / 2, but avoids overflow for large low and high
        int mid = low + (high - low) / 2;

        // Recursively sort the first and second halves
        mergeSort(arr, low, mid);
        mergeSort(arr, mid + 1, high);

        // Merge the sorted halves
        merge(arr, low, mid, high);
    }
}

// Utility function to print an array
void printArray(int A[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
}

// Driver program to test the merge sort functions
int main() {
    int arr[] = {14, 15, 12, 11, 13, 8, 5, 6, 7, 9};
    int arr_size = sizeof(arr) / sizeof(arr[0]);

    printf("Given array is \n");
    printArray(arr, arr_size);

    // Perform merge sort
    mergeSort(arr, 0, arr_size - 1);

    printf("Sorted array is \n");
    printArray(arr, arr_size);

    return 0;
}
