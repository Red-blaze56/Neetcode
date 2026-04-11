class Solution {
public:
    double findMedianSortedArrays(vector<int>& num1, vector<int>& num2) {
        if(num1.size()>num2.size()){return findMedianSortedArrays(num2,num1);}
        int x=num1.size(), y=num2.size();
        int l=0,r=x;
        while(l<=r){
            int midX=l+(r-l)/2;
            int midY=(x+y+1)/2 - midX;

            int leftmaxX = (midX==0)?INT_MIN:num1[midX-1];
            int rightminX = midX==x?INT_MAX:num1[midX];
            int leftmaxY = (midY==0)?INT_MIN:num2[midY-1];
            int rightminY = (midY==y)?INT_MAX:num2[midY];

            if(leftmaxX<=rightminY && leftmaxY<=rightminX){
                if((x+y)%2==0){
                    return (max(leftmaxX,leftmaxY)+min(rightminX,rightminY))/2.0;
                } else {return max(leftmaxX,leftmaxY);}
            }
            else if(leftmaxX>rightminY){
                r=midX-1;
            } else{l= midX+1;}
        }
        return 0.0;
    }
};
