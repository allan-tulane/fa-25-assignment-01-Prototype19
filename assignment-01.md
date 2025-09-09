

# CMPS 2200 Assignment 1

**Name:** Daron Lebaredian


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 

Yes because by using the limit method and evaluating the following limit: $\lim_{n \to \infty} \frac{2^{n+1}}{2^n}$, you will get the the number 2 which means that $2^{n+1} \in \Theta(2^n)$ or just $2^{n+1} \in O(2^n)$.

  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?

No, if you evaluate $2^{2^n}$ to be just $4^n$ and then use the limit method: $\lim_{n \to \infty} \frac{4^n}{2^n}$, the limit will evaulate to $2^\infty$ or $\infty$. This means that $2^{2^n} \in \Omega(2^n)$ and *not* $2^{2^n} \in O(2^n)$.

  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?

No, if you evaluate $n^{1.01}$ to be just $n^{101/100}$ and then use the limit method: $\lim_{n \to \infty} \frac{n^{101/100}}{\mathrm{log}^2 n}$, the limit will evaulate to $\infty$. This means that $n^{1.01} \in \Omega(\mathrm{log}^2 n)$ and *not* $n^{1.01} \in O(\mathrm{log}^2 n)$.

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?

Yes, if you do the same process as in the last problem, you will get $n^{1.01} \in \Omega(\mathrm{log}^2 n)$.

  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?
  
No, if you use the limit method: $\lim_{n \to \infty} \frac{\sqrt{n}}{(\mathrm{log} n)^3}$, the limit will evaulate to $\infty$. This means that $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$ and *not* $\sqrt{n} \in O((\mathrm{log} n)^3)$.

  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  

Yes, if you do the same process as in the last problem, you will get $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$.

2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 

```sparc
foo x =
  if x <= 1 then
    x
  else
    let (ra, rb) = (foo (x - 1)), (foo (x - 2)) in
      ra + rb
    end.
```

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?

This 'foo' function is exactly like the fibonacci function. Basically, what the fibonacci function does is that for an input x it makes two recursive calls, f(x-1) and f(x-2), and add the results of those calls togther. If the input x is 1 or lower, the function will always return 1.
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

Both the work and span of this implementation is O(n).

  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  
.  
.  
.  
.  
.  
.  
.  

