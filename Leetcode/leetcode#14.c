char * longestCommonPrefix(char ** strs, int strsSize){
    if (!strsSize)
        return "";
    
    char* ans = strs[0];
    // Compare each word with ans
    for(int i=1; i < strsSize; i++)
    {
        char* p = ans;
        char* temp = strs[i];
        while(*p != '\0' && *temp != '\0')
        {
            if(*p != *temp)
            { // If not same, change ans
                *p = '\0';
                break;
            }
            p++;
            temp++;
        }
        // If string is running out, point current string to ans.
        if(*temp == '\0')
        ans = strs[i];
    }
    return ans;
}