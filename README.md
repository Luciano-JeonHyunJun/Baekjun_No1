# Baekjun_No1
백준 온라인 문제풀이 사이트의 문제를 푸는 커밋입니다.

<h1><a href="https://www.acmicpc.net/step/1">입출력과 사칙연산</a></h1>

<h3>HelloWorld 2557</h3><br>
Hello World!를 출력하시오.

<pre>
<code>
print("Hello World!")
</code>
</pre>
<strong>정말 기본적인 출력방법입니다. 다르게 쓰는 방법은 print('Hello World!')입니다.</strong>

<h3>We love kriii 10718</h3><br>
두 줄에 걸쳐 "강한친구 대한육군"을 한 줄에 한 번씩 출력한다.

<pre>
<code>
print("강한친구 대한육군")
print('강한친구 대한육군')
</code>
</pre>

<strong>기본적인 print 출력 방법이지만 시작과끝의 따옴표를 다르게 썻습니다.</strong>

<h3>고양이 10171</h3>
고양이를 출력한다.
<br>
밑에 출력값을 출력하는 문제입니다.

<pre>
<code>
\    /\
 )  ( ')
(  /  )
 \(__)|
</code>
</pre>

<pre>
<code>
print("\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \(__)|")
</code>
</pre>

<strong>첫번째 줄인 코드에서 역슬래쉬를 쓴 이유는 이스케이프 문자에서는 \을 표현하려면 \\ 을 사용해야합니다.</strong>

<h3>강아지 10172</h3>
개를 출력한다.
<br>
밑에 출력값을 출력하는 문제입니다.

<pre>
<code>
|\_/|
|q p|   /}
( 0 )"""\
|"^"`    |
||_/=\\__|
</code>
</pre>

<pre>
<code>
print("|\\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print("||_/=\\\__|")
</code>
</pre>

<strong>첫번째줄에는 \\ 역슬래쉬를 두번하여 하나로 만들었습니다. <br>
        고친것은 없습니다. <br>
        세번째줄에는 코드내부에서 큰 따옴표(")를 사용했기에 작은따옴표(')를 사용했습니다.<br>그리고 이스케이프 문자의 \를 사용하기 위해서 \\로 사용했습니다. <br>
        네번째줄은 내부에서 큰따옴표(")를 사용했어서 내부에서도 작은따옴표(')를 사용했습니다.<br>
        다섯번째줄은 이스케이프 문자를 사용해서 중간에 \\를 사용한뒤 \를 하나 더 추가해서 \\가 출력되게 하였습니다. </strong>
        
<h3>A + B 1000</h3>
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10) , 첫째 줄에 A+B를 출력한다.
<br>

<pre>
<code>
a,b = input().split()
a = int(a)
b = int(b)
print(a+b)
</code>
</pre>

<strong>첫번째줄을 보면 알겟지만 a,b라는 variable을 input으로 동시에 받고 , <br>split() function을 사용하여 두 수를 나누어 줍니다.<br>
          두번째줄과 세번째줄은 a 와 b 를 int로 두는것입니다.
        마지막줄은 a+b를 하는것입니다. 하지만 결과값은 나오지 않습니다.
  
</strong>

<h3>A-B 1001</h3>
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10) , 첫째 줄에 A-B를 출력한다.

<pre>
<code>
a,b = input().split()
a = int(a)
b = int(b)
print(a - b)
</code>
</pre>

<strong>아까 문제와 다른것은 없습니다 단지 마지막줄에서 - 로 바뀐것입니다.</strong>

<h3>A×B 10998</h3>
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10) , 첫째 줄에 A×B를 출력한다. 

<pre>
<code>
a,b = input().split()
a = int(a)
b = int(b)
print(a - b)
</code>
</pre>

<strong>위에 있는 1001번과 1000번의 문제와 다른점은 맨밑에 코드만 다른것입니다. 컴퓨터에서 곱하기는 *로 인식합니다.</strong>

<h3>A/B 1008</h3>
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10) , 첫째 줄에 A/B를 출력한다.<br> 실제 정답과 출력값의 절대오차 또는 상대오차가 10-9 이하이면 정답이다.

<pre>
<code>
a,b = input().split()
a = int(a)
b = int(b)

print(a / b)
</code>
</pre>

<strong>아까와 다른것은 마지막 코드에서 나누기라는 코드는 컴퓨터에서는 \ 로 인식하기 때문에 , \로 사용합니다.</strong>

<h3>사칙연산 10869</h3>
두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000) , 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

<pre>
<code>
A,B = input().split()
A = int(A)
B = int(B)

print(A+B)
print(A-B)
print(A*B)
print(int(A/B))
print(A%B)
</code>
</pre>

<strong>여덟번째줄의 코드는 왜 int(A/B) 라고 썻냐면 , 나중에 나눴을때 소수점으로 나머지가 나올수도 있어서 int로 해둔것입니다.</strong>

<h3>나머지 10430</h3>

<pre>
<code>
a,b,c = map(int,input().split())
print((a+b)%c)
print((a%c + b%c)%c)
print((a*b)%c)
print((a%c * b%c)%c)

</code>
</pre>

<strong>위에 코드들과 다른점이 있다면 위에 코드들은 모두다 a = int(a) 이런식으로 int 라고 선언을 해줬는데 <br>
         이번에는 map 이라는 function을 사용해서 여러개의 데이터를 한번에 다른 형태로 바꿔줬습니다.
  
 <br>
 map의 특징은 
 - 원본 리스트를 변경하지 않고 , 새 리스트를 생성한다. <br>
 - 결과를 리턴하기 때문에 리스트나 튜플 등으로 변환한다.
      
</strong>

<h3>곱셈 2588</h3>
<a href="https://www.acmicpc.net/problem/2588">문제 링크입니다.</a>(예제를 따라 쓸수가 없네요.)
 
 <pre>
 <code>
 a = int(input())
b = list(input())
a1 = a * int(b[2])
a2 = a * int(b[1])
a3 = a * int(b[0])
result = (a1 + (a2*10) + (a3*100))
print(a1, a2 , a3 , result)
</code>
</pre>

<strong>이번 문제는 저도 다 이해를 하지 못해서 https://edudeveloper.tistory.com/13 이 분의 블로그를 보고 참고했습니다.</strong>

# Baekjun_No1 (ENG.Ver)
<h6>All translations inform you that Google Translator was used.</h6>
This is a commit that solves the problem of the Baekjun online problem solving site.

<h1><a href="https://www.acmicpc.net/step/1">Input and output and four arithmetic operations</a></h1>

<h3>HelloWorld 2557</h3><br>
Print Hello World!

<pre>
<code>
print("Hello World!")
</code>
</pre>
<strong>This is a really basic printing method. Another way to write it is print('Hello World!').</strong>

<h3>We love kriii 10718</h3><br>
"Strong Friend Daehan Army" is printed once per line over two lines.

<pre>
<code>
print("Strong Friend Korean Army")
print('Strong Friend Korean Army')
</code>
</pre>

<strong>This is the default print output method, but the start and end quotes are different.</strong>

<h3>Cat 10171</h3>
Print the cat.
<br>
It is a problem of printing the output value below.

<pre>
<code>
\ /\
 ) (')
(/)
 \(__)|
</code>
</pre>

<pre>
<code>
print("\ /\\")
print(") (')")
print("( / )")
print(" \(__)|")
</code>
</pre>

<strong>The reason I used the backslash in the first line of code is that in the escape character, you must use \\ to represent \.</strong>

<h3>Dog 10172</h3>
Print the dog.
<br>
It is a problem of printing the output value below.

<pre>
<code>
|\_/|
|q p| /}
( 0 )"""\
|"^"` |
||_/=\\__|
</code>
</pre>

<pre>
<code>
print("|\\_/|")
print("|q p| /}")
print('( 0 )"""\\')
print('|"^"` |')
print("||_/=\\\__|")
</code>
</pre>

The first line of <strong> is doubled with a \\ backslash to form one. <br>
        Nothing has been fixed. <br>
        In the third line, I used double quotation marks (") inside the code, so I used single quotation marks (').<br>And I used \\ to use the escape character \. <br>
        In the fourth line, double quotation marks (") are used inside, so single quotation marks (') are used inside.<br>
        The 5th line uses an escape character to display \\ by adding a \\ in the middle and then adding another \. </strong>
        
<h3>A + B 1000</h3>
A and B are given on the first line. (0 <A, B <10), print A+B on the first line.
<br>

<pre>
<code>
a,b = input().split()
a = int(a)
b = int(b)
print(a+b)
</code>
</pre>

<strong>As you can see from the first line, the variables a and b are simultaneously received as input, and the two numbers are divided using the <br>split() function.<br>
          The second and third lines put a and b as ints.
        The last line is a+b. But there is no result.
  
</strong>

<h3>A-B 1001</h3>
A and B are given on the first line. (0 <A, B <10), print A-B on the first line.

<pre>
<code>
a,b = input().split()
a = int(a)
b = int(b)
print(a-b)
</code>
</pre>

<strong>There is nothing different from the previous problem, just changed to-in the last line.</strong>

<h3>A×B 10998</h3>
A and B are given on the first line. (0 <A, B <10), print A×B on the first line.

<pre>
<code>
a,b = input().split()
a = int(a)
b = int(b)
print(a-b)
</code>
</pre>

The difference from the above <strong>1001 and 1000 problems is that only the code at the bottom is different. Multiplication is recognized by the computer as *.</strong>

<h3>A/B 1008</h3>
A and B are given on the first line. (0 <A, B <10), print A/B on the first line.<br> If the absolute or relative error between the actual correct answer and the output value is less than 10-9, the answer is correct.

<pre>
<code>
a,b = input().split()
a = int(a)
b = int(b)

print(a / b)
</code>
</pre>

<strong>The difference from the previous one is that the division in the last code is recognized as \ by the computer, so it is used as \.</strong>

<h3>Fourth arithmetic operation 10869</h3>
Two natural numbers A and B are given. (1 ≤ A, B ≤ 10,000), prints A+B on the first line, A-B on the second line, A*B on the third line, A/B on the fourth line, and A%B on the fifth line.

<pre>
<code>
A,B = input().split()
A = int(A)
B = int(B)

print(A+B)
print(A-B)
print(A*B)
print(int(A/B))
print(A%B)
</code>
</pre>

<strong>The reason why the 8th line of code is written as int(A/B) is that when you divide it later, the remainder may appear as a decimal point, so it is int.</strong>

<h3>The remaining 10430</h3>

<pre>
<code>
a,b,c = map(int,input().split())
print((a+b)%c)
print((a%c + b%c)%c)
print((a*b)%c)
print((a%c * b%c)%c)

</code>
</pre>

<strong>If there is any difference from the above codes, all of the above codes are declared as int in this way: a = int(a) <br>
         This time, we used a function called map to change several data into different forms at once.
  
 <br>
 The characteristic of map is
 -Create a new list without changing the original list. <br>
 -Because it returns the result, it is converted into a list or tuple.
      
</strong>

<h3>Multiplication 2588</h3>
<a href="https://www.acmicpc.net/problem/2588">This is a problem link.</a> (I can't follow the example.)
 
 <pre>
 <code>
 a = int(input())
b = list(input())
a1 = a * int(b[2])
a2 = a * int(b[1])
a3 = a * int(b[0])
result = (a1 + (a2*10) + (a3*100))
print(a1, a2, a3, result)
</code>
</pre>

<strong>I didn't understand this problem either, so I looked at https://edudeveloper.tistory.com/13's blog and referenced it.</strong>


        
        
        
        
        
    
         



