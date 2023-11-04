# Trimmed

This was the first challenge in a series of gopher protocol related challenges.
We were given this site: `go.ctf.site:10070`

I tried to access it, and accidentally gave it the correct path `EKO`.
The server returned a list of paths I could access further:

    lpy@lpy-Zephyrus:~$ nc go.ctf.site 10070
    EKO
    128    /EKO/28    go.ctf.site    10070    +
    0ENCRYPTED_1    /EKO/ENCRYPTED_1    go.ctf.site    10070    +
    0ENCRYPTED_2    /EKO/ENCRYPTED_2    go.ctf.site    10070    +
    0GOPHER    /EKO/GOPHER    go.ctf.site    10070    +
    0README    /EKO/README    go.ctf.site    10070    +

By checking out /EKO/README, I found the flag: `EKO{g0pher_mod3}`.

I later installed the `Overbite` firefox extension and `lynx` and noticed that in `lynx`, the flag would not appear and would be trimmed. However, it did not affect the `nc` tool.
