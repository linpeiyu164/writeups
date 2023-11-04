# UUEncrypted

Access the first encrypted string:
```
lpy@lpy-Zephyrus:~$ nc go.ctf.site 10070
/EKO/ENCRYPTED_1
begin 644 ENCRYPTED
M2$D@6D523R!)32!44EE)3D<@02!.15<@14Y#4EE05$E/3@H*14M/>U5514Y#
0,$1%1%]%3D-265!4140_?0``
`
```

By searching online for the `begin 644 ENCRYPTED` header, I found out the type of encoding it used. After decoding it online, I got the flag:

```
HI ZERO IM TRYING A NEW ENCRYPTION

EKO{UUENC0DED_ENCRYPTED?}
```

# References
- https://zh.wikipedia.org/zh-tw/Uuencode