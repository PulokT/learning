len_2 = string_len(latter);
len_1 = string_len(former);
flag = 0;
result_string = "";
for(i=len_2-1;i>=0;i--)
{
    for(k=len_1;k>=0;k--)
    {
        a = alphabet_to_integer(latter[i]);
        b = alphabet_to_integer(former[k]);
        c = a*b;
        c = c * 10 + flag;

        flag = c/10;
        ch = integer_to_alphabet(c%10);
        result_string = concat(ch,result_string);
    }
}