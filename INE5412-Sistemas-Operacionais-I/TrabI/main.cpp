#include <iostream>
#include <algorithm>
#include <array>
#include <vector>

using namespace std;


typedef struct job {
    vector<int>& start;
    vector<int>& end;
    vector<int>& profit;
} job_t;


int partition(const job_t* job, const int low, const int high) {
    const int pivot = job->profit[high];
    int i = low - 1;
    for (int j = low; j <= high - 1; j++) {
        if (job->profit[j] > pivot) {
            i++;
            swap(job->start[i], job->start[j]);
            swap(job->end[i], job->end[j]);
            swap(job->profit[i], job->profit[j]);
        }
    }
    swap(job->start[i + 1], job->start[high]);
    swap(job->end[i + 1], job->end[high]);
    swap(job->profit[i + 1], job->profit[high]);
    return i + 1;
}


void quicksort(const job_t* job, const int low, const int high) {
    if (low < high) {
        const int pivot = partition(job, low, high);
        quicksort(job, low, pivot - 1);
        quicksort(job, pivot + 1, high);
    }
}

int jobScheduling(vector<int> &startTime, vector<int> &endTime, vector<int> &profit) {
    const job_t jb = {startTime, endTime, profit};
    quicksort(&jb, 0, profit.size() - 1);

    for (int i = 0; i < profit.size(); i++) {
        int totalProfit = 0;
        for (int j = i; j < profit.size(); j++) {
            
        }
    }


    return 0;
}


int main() {
    vector<int> startTime = {1,2,3,4,6};
    vector<int> endTime = {3,5,10,6,9};
    vector<int> profit = {20,20,100,70,60};
    cout << jobScheduling(startTime, endTime, profit) << '\n';
}
