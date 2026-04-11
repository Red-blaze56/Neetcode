class Solution {
public:
    int findMin(vector<int> &nums) {
        int l = 0, mid=0;
        int h = nums.size()-1;
        for(int i=0; i<nums.size(); i++){
            mid = l+(h-l)/2; //l=[0]=3; mid=[2]=5; h=[5]=2;
            cout<<"beg"<<nums[l]<<" "<<nums[mid]<<" "<<nums[h]<<endl; 
            if(nums[mid]>nums[h]){l=mid;}
            else{if(nums[mid]<nums[l]){h=mid;}
            else{return nums[l];}}
            cout<<nums[l]<<" "<<nums[mid]<<" "<<nums[h]<<endl;
        }
        return nums[h];
    }
};
