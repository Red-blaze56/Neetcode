class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        for (auto& row : matrix) {

            if (target < row.front() || target > row.back())
                continue;

            int l = 0;
            int r = row.size() - 1;

            while (l <= r) {
                int mid = l + (r - l) / 2;

                if (row[mid] == target)
                    return true;
                else if (row[mid] < target)
                    l = mid + 1;
                else
                    r = mid - 1;
            }
        }
        return false;
    }
};
