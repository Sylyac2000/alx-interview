## 0x00. Pascal's Triangle

## Requirements
* Language: Javascript, Python 3.8.5 (and C )
* OS: Ubuntu 20.04 LTS
* Compiler: python3  (and gcc 9.3.0)
* Version: MySQL  8.0.25
* Style guidelines: [Pycodestyle] (https://github.com/PyCQA/pycodestyle)


## Synopsis
This repository holds some python projects I worked on at ALX SPECIALIZATION.


## Tasks

* 0. Pascal's Triangle

### 0\. Pascal's Triangle

mandatory

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:

*   Returns an empty list if `n <= 0`
*   You can assume `n` will be always an integer

    guillaume@ubuntu:~/0x00$ cat 0-main.py
    #!/usr/bin/python3
    """
    0-main
    """
    pascal_triangle = __import__('0-pascal_triangle').pascal_triangle
    
    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))
    
    
    if __name__ == "__main__":
        print_triangle(pascal_triangle(5))
    
    guillaume@ubuntu:~/0x00$ 
    guillaume@ubuntu:~/0x00$ ./0-main.py
    [1]
    [1,1]
    [1,2,1]
    [1,3,3,1]
    [1,4,6,4,1]
    guillaume@ubuntu:~/0x00$ 
    

**Repo:**

*   GitHub repository: `alx-interview`
*   Directory: `0x00-pascal_triangle`
*   File: `0-pascal_triangle.py`
