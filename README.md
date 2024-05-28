# Samba_de_Koalav2
So what if your friend is a double monitor abuser...

That means there is another room for the koala to take over!

This repository is a refined version of the previous one.

The program uses pillow (PIL), numpy, and screeninfo. If these are not installed in your (or your friend's) computer, the program will not operate properly. Please make sure that these libraries are installed (if the computer does not have python, you will need to start from downloading python).
```
pip install pillow
pip install numpy
pip install screeninfo
```

This time, the datetime package is not commented out. The program will pop out a window when it becomes 1pm on the device. One hour later, the program will create another window that fills up the second monitor (my intention is not to build a virus so the program will not produce more windows after the second one).

If you happen to browse through this code, you will realize that the window will pop out in fullscreen. *Do not problem!* You can tab out and stop the program by the classic "Control-c" on the terminal. Otherwise, you may try the several options I added which will terminate the running program. The options are "Control-w", "Control-q", and "Escape" (all of them are keyboard input).

**How to run the program on terminal (not complex):**
```
python imAsleep.py
```

The gif is from https://tenor.com/view/marionritzenjanssen-gif-19358479.

<p align="center">
  <img src=https://github.com/nykie738/Samba_de_Koala/blob/main/taniecK.gif alt="animated" />
</p>
