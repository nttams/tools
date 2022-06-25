<link rel="stylesheet" href="styles.css">

### GOLANG
hi
___
### NOTES
Test-driven development (TDD)

___
### BOOKS
tôi nói gì khi nói về chạy bộ

___
### VSCODE
workbench.action.terminal.focus  
workbench.action.focusActiveEditorGroup

"editor.quickSuggestions": {  
    "other": false,  
    "comments": false,  
    "strings": false  
},

addin: LiveServer

___
### LINUX
rename files: for i in lessEnglish_Chapter*;do mv "$i" "${i/lessEnglish_Chapter/''}"; done;

Ctrl * \: split window  
Ctrl * tab: switch windows  
Ctrl * shift * O: explore outline

___
### HTML/CSS/JS
* import js at the end of html file
* import css/less at the begining
* import less BEFORE js for less

___
#### STATIC IPs
network:  
    version: 2  
    renderer: networkd  
    ethernets:  
    eno1:  
        dhcp4: false  
        dhcp6: false  
        addresses:  
            - 192.168.1.10/24  
        routes:  
            - to: default  
            via: 192.168.1.1  
        nameservers:  
            addresses: [8.8.8.8,8.8.4.4]

___
### GITHUB
git config --get remote.origin.url  
git push -u origin second_branch

#### create a new repository on the command line
echo "# test_git" >> README.md  
git init  
git add README.md  
git commit -m "first commit"  
git branch -M main  
git remote add origin https://github.com/nttam000/test_git.git  
git push -u origin main  

#### push an existing repository from the command line  
git remote add origin https://github.com/nttam000/test_git.git  
git branch -M main  
git push -u origin main

___
#### GIT CACHING
git config --global credential.helper cache

___
### HASHING
Characteristics of a good hash function

* The hash value is fully determined by the data being hashed.
* The hash function uses all the input data.
* The hash function "uniformly" distributes the data across the entire set of possible hash values.
* The hash function generates very different hash values for similar strings.

___
### C++
* When using c+* template, remember to add implemenation for that template, otherwise you wil get "undefined reference to..."

___
### RUST

#### Tips
use Vec<u8> as buffer for network reading rather than array

#### Expression
* Calling a function is an expression.
* Calling a macro is an expression.
* A new scope block created with curly brackets is an expression
* if is an expression

#### Stack & Heap
All data stored on the stack must have a known, fixed size. Data with an unknown size at compile time or a size that might change must be stored on the heap instead.  
There’s a design choice that’s implied by this: Rust will never automatically create “deep” copies of your data. Therefore, any automatic copying can be assumed to be inexpensive in terms of runtime performance.

#### Here are some of the types that implement Copy:
* All the integer types, such as u32.
* The Boolean type, bool, with values true and false.
* All the floating point types, such as f64.
* The character type, char.
* Tuples, if they only contain types that also implement Copy. For example, (i32, i32) implements Copy, but (i32, String) does not.

#### Ownership passing to function
datatype does not implement COPY ()
--> pass whole stack value (it may contain pointer to heap memory that actually contain data)
--> when the variable goes out of scope, drop() function is called
--> if variable is already moved (e.g to a function), nothing happens when that variable goes out of scope. It is not valid anymore
--> drop() and copy() can not be implemented together. Only one of them.
--> Use reference instead if you don't want to give up ownership of a variable to a function

datatype does implement COPY () --> pass whole stack value

#### Reference
* Unlike a pointer, a reference is guaranteed to point to a valid value of a particular type
* You can have only ONE mutable reference to a particular piece of data at a time

#### Debug info
* println!("{:?}", rect);
* println!("{:#?}", rect);
* with #[derive(Debug)] before the struct defination

#### Function and method
Associated functions that aren’t methods are often used for constructors that will return a new instance of the struct.

#### String
let s1 = String::from("tic");  
let s2 = String::from("tac");  
let s3 = String::from("toe");  
let s = format!("{}-{}-{}", s1, s2, s3);

#### Error handling
Rust groups errors into two major categories:
* recoverable
* unrecoverable

Rust doesn’t have exceptions.  
* The type Result<T, E> for recoverable errors  
* The panic! macro that stops execution when the program encounters an unrecoverable error.  

Result.up_wrap: print the ERR message  
Result.expect: print your own message  
--> using unwrap in multiple places, it can take more time to figure out exactly which unwrap is causing the panic because all unwrap calls that panic print the same message.

#### Trait
pub fn notify(item1: &impl Summary, item2: &impl Summary) {  
}  
//If we wanted to force both parameters to have the same type, -->  
pub fn notify<T: Summary>(item1: &T, item2: &T) {  
}

___
### INTERVIEW
* Prepare:
* Tell me about yourself
* What are you strengths and weaknesses
* Do you have any question about us?
* Do mock interviews
* Practise algorithmns on paper
* HASH TABLE
* Remember the key information from the interviewers --> write them down: Big, Not special case, Use real, valid number, string

#### Steps
* Listen
* Example
* Bruce force
* Optimize
* Trust your brain, let your brain solve the problem naturally, and then reverse-engineer it.
* Start with simple problem, solve it, then adapt it to orginal problem
* Base case first (read CTCI)
* Walk through
* Implement: Good variable names
* Test

___
### Sayings
* Write code that is easy to delete, not easy to extend.
* done is better than perfect
* Impatience makes smart people do stupid things
* Test ideas by experiment and observation. Build on those ideas that pass the test, reject the ones that fail, follow the evidence where ever it leads and question everything.

___
### VIM
:g/^$/d		delete all empty lines

~/.config/nvim/init.vim

___
### DATA STRUCTURES
#### Linked list
* Good for inserting and removing element
* Not good for accessing and sorting

#### Binary tree
* Good for ordering

#### Hash table
* Very important

#### Tree
* Balanced or NOT
* Binary search tree or NOT
* Equality (duplicated or NOT)
* Please be COMFORTABLE with traversal binary tree (in-order, post-order, pre-order)

#### Graph
* BFS: breadth first search: is NOT recursive

___
### SOFTWARES
* VirtualBox
* Wireshark
* NeoVim
* PostMan
* VsCode
* Notepad++
* FoxitReader
* git, net-tools, htop, nload
* MobaXTerm
* Hercules

___
### LIST OF MISTAKES
* Forget edge cases
* Code before think

___
### File converter
* ffmpeg -i input.mkv -codec copy output.mp4  
* for i in *.mkv; do ffmpeg -i "$i" -codec copy  "${i%.*}.mp4"; done

___
### APACHE2
You'll have to edit  
* /etc/apache2/sites-available/000-default.conf: to change the document root of apache (from /var/www/html/ to whatever you want)  
* /etc/apache2/apache2.conf: to grant permission  

___
# The end