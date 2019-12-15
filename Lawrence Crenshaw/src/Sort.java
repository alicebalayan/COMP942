
class Sort { 
    /*Insertion Sort Class*/
    void sort(int array[]) 
    { 
        /*Organizes and finds the numbers*/       	
        int n = array.length; 
        for (int i = 1; i < n; ++i) { 
            int num = array[i]; 
            int s = i - 1; 

            /*Loop that sorts the numbers*/            
            while (s >= 0 && array[s] > num) { 
                array[s + 1] = array[s]; 
                s = s - 1; 
            } 
            array[s + 1] = num; 
        } 
    } 
}