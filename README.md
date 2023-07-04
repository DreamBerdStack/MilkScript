<div align="center">
<img src="res/MILK%20SCRIPT.png" width=200 height=200 alt="milkscript logo" style="border-radius: 10px;">
<br><br>
<h1>MilkScript</h1>
<i>An overall tutorial on how to use it.</i>
<br><br>
<h1>FOR CONTRIBUTORS</h1>
For those who want to upgrade the code within the
MilkScript repo (since I am a horrid programmer)
it's best I go over the git repo. The following
describes each directory:<br><br>


    examples/ - This is a folder where all the example files go in.
    parser/ - This is an upcoming version of the parser, written in Go.
    res/ - Just resources for stuff like the README file.
    test_parser/ - A beta/alpha version of the parser, written in Python.


<h1>FOR DEVELOPERS</h1>
<i>Just saying, since all text is aligned to the center, the example code looks weird. Sorry!</i><br><br>
MilkScript is stack-based, so a majority
of data you wish to save will be thrown
on there. To push to the stack, use the
<code>pour</code> command to pour data
onto the stack.<br>Here's an example:<br><br>


    pour(Hello, world!);


To read from a stack register, use the <code>read</code>
command and call them by address:<br><br>


    pour(melkey is coming for you);
    read(0);


Also, every program must end with 'exit()' to declare the
end of the program:<br><br>


    pour(melkey is coming for you);
    read(0);
    exit();


</div>
