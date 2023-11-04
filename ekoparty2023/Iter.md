# Iter

From here we access the /EKO/28 path and find out that it is a never ending abyss of path...

    lpy@lpy-Zephyrus:~$ nc go.ctf.site 10070
    EKO
    128    /EKO/28    go.ctf.site    10070    +
    0ENCRYPTED_1    /EKO/ENCRYPTED_1    go.ctf.site    10070    +
    0ENCRYPTED_2    /EKO/ENCRYPTED_2    go.ctf.site    10070    +
    0GOPHER    /EKO/GOPHER    go.ctf.site    10070    +
    0README    /EKO/README    go.ctf.site    10070    +

Since it is quite difficult and laboring to click on the link manually, I wrote a script to auto enumerate the paths. I noticed that there were crossroads where the path would diverge, the script recursively follows both paths.

Script:

```
from pwn import *
import subprocess

directory = "EKO/28"
num_of_paths = 0

def traverse(directory, path):
    global num_of_paths
    if directory != "":
        print("Path: ", path, "Dir: ", directory)
        r = remote("go.ctf.site", 10070)
        r.sendline(directory)
        directories = r.recvall().decode().split("\t")

        if len(directories) == 5:
            directory = directories[1]
            traverse(directory, path)
        elif len(directories) == 9:
            directory = directories[1]
            traverse(directory, path)
            second_directory = directories[5]
            num_of_paths += 1
            new_path_num = num_of_paths
            traverse(second_directory, new_path_num)

    print("FINAL: ", directory)

traverse(directory, 0)
print("Num of paths", num_of_paths)
```

There were 3 paths in total.

One of them led to a link to the Rick Roll video...

Another was to a fake flag: KEO{this_is_a_trap!!}

```
/EKO/28/30/2c/30/2c/4f/29/28/30/2c/30/2c/4d/29/28/30/2c/30/2c/47/29/28/31/2c/31/2c/47/29/28/33/2c/33/2c/20/29/28/30/2c/30/2c/59/29/28/31/30/2c/31/2c/55/29/28/34/2c/31/2c/41/29/28/30/2c/30/2c/52/29/28/30/2c/30/2c/45/29/28/34/2c/31/2c/43/29/28/30/2c/30/2c/4c/29/28/39/2c/31/2c/53/29/28/36/2c/32/2c/54/29/28/35/2c/31/2c/20/29/28/33/2c/31/2c/48/29/28/37/2c/32/2c/46/29/28/31/33/2c/31/2c/41/29/28/31/2c/31/2c/41/29/28/32/2c/32/2c/47/29/28/33/36/2c/37/2c/43/29/28/32/38/2c/35/2c/43/29/28/36/2c/35/2c/57/29/28/33/2c/31/2c/4c/29/28/31/2c/31/2c/20/29/28/30/2c/30/2c/4e/29/28/31/30/2c/31/2c/57/29/28/34/30/2c/33/2c/49/29/28/31/35/2c/31/2c/20/29/28/33/2c/33/2c/54/29/28/34/38/2c/36/2c/47/29/28/35/2c/31/2c/45/29/28/30/2c/30/2c/4b/29/28/32/32/2c/31/2c/7b/29/28/32/35/2c/31/2c/49/29/28/33/38/2c/31/2c/45/29/28/31/2c/31/2c/45/29/28/33/2c/33/2c/45/29/28/37/2c/37/2c/45/29/28/31/35/2c/31/35/2c/5f/29/28/33/38/2c/33/2c/4f/29/28/32/2c/32/2c/4f/29/28/35/2c/35/2c/4f/29/28/31/31/2c/31/31/2c/4f/29/28/33/2c/33/2c/5f/29/28/36/33/2c/32/33/2c/7d/29/flag.txt
```

Finally, we got the flag: EKO{0mg_h0w_d3eep_1s_th1ssss}
