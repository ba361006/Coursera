# Week_2

- Huffman coding

    ![Huffman_coding](./Image/Huffman_coding.jpg)

    snipped from coursera

    This is a sort of prefix-free code which will simplify the process of reconstructuring the original signal. 
    
    For example, look at the code, and you might notice that there is always a digit that is different from the other digits for each column. when decoder receives the first digit that is one, then it should know that its no need to wait for another digit to identify which symbol it is. 
    
    Otherwise, in the same context, if the first digit that decoder receives is zero, then it should wait for another digit to determine whether it should stop waiting or not. And so on, until we are able to indentify every symbol in the list.

