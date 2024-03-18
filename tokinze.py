import re

def count_tokens(code):
   
    token_patterns = [
        r'\b(?:int|return|if|else)\b', 
        r'[\+\-\*\/\%\=\<\>\(\)\{\}\[\]\;]',  
        r'\b[a-zA-Z_]\w*', 
        r'\b\d+\b' 
    ]

    total_count = 0
    for pattern in token_patterns:
        total_count += len(re.findall(pattern, code))
    return total_count

code = '''
using namespace std;

int main () {
    int a;
    a = 25;
    int b = 3;
    b = a + b;
    cout << "b is " << b;
    cout << endl;
    return 0;
}
'''

print("Total tokens:", count_tokens(code))
