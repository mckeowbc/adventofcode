package main

import (
    "fmt"
    "crypto/md5"
    "io"
    "strconv"
    "strings"
    "os"
)

func main() {
    salt := os.Args[1]
    c := 0
    passwd := ""


    for len(passwd) < 8 {
        h := md5.New()
        hash := fmt.Sprintf("%x", h.Sum(salt + strconv.Itoa(c)))

        if strings.HasPrefix(hash,"00000") {
            passwd += string(hash[5])
        }
        c += 1
    }

    fmt.Println(passwd)
}
