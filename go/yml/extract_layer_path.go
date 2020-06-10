package main

import (
	"fmt"
	"io/ioutil"
	_"reflect"
	_"strings"
	"gopkg.in/yaml.v2"
)

func Parse(data interface{}, prefix string, paths *[]string) {
	value, ok := data.(string)
	if ok {
		p := prefix + "-->" + value
		*paths = append(*paths, p)
		return
	}

	d, ok := data.(map[interface{}]interface{})
	if !ok {
		panic(nil)
	}
	for k, v := range d {
		k := k.(string)
		path := prefix + "." + k
		Parse(v, path, paths)
	}
}

func main() {
	buf, _ := ioutil.ReadFile("path.yml")
	var data interface{}

	if err := yaml.Unmarshal(buf, &data); err != nil {
		panic(err)
	}

	paths := []string{}
	prefix := "root"
	Parse(data, prefix, &paths)

	for _, p := range paths {
		fmt.Println(p)
	}
}

/*
	textKey := "random-exporter/alerts.random_0_too_large.message"
	inFileTextkey := strings.Split(textKey, "/")[1]
	mapKeys := strings.Split(inFileTextkey, ".")
	var cur interface{} = data
	path := []string{}
	for _, k := range mapKeys {
		fmt.Println(k)
		fmt.Println(cur)
		fmt.Println(reflect.TypeOf(cur))
		dict, ok := cur.(map[interface{}]interface{})
		if !ok {
			fmt.Println("not a dict")
			break
		}
		cur, ok = dict[k]
		if !ok {
			fmt.Println("no key")
			break
		}
	}
	str, ok := cur.(string)
	if !ok {
		fmt.Println("not a string")
	}

	fmt.Println(str)
*/